#!/usr/bin/env python
"""
This node finds lanes using a Canny edge detector and Hough transform.
It is intended to detect right and left lane borders always as straight lines. 
Curves are also detected as straight lines under the assumption that curvature
is small enough.
Detected lines are published in normal form (rho, theta) as 2-float arrays.
rho is measured in pixels and theta in radians
"""
import math
import cv2
import numpy
import rospy
import numpy as np
from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

kernel = np.ones((5, 5), np.uint8)
lower_color = [0, 0, 253] 
upper_color = [90, 4, 255]

#
# Converts a line given by two points to the normal form (rho, theta) with
# rho, the distance to origin and theta, the angle wrt positive x-axis
#
# To normal form {{{
def to_normal_form(x1, y1, x2, y2):
    A = y2 - y1
    B = x1 - x2
    C = A*x1 + B*y1
    theta = math.atan2(B,A)
    rho   = C/math.sqrt(A*A + B*B)
    if rho < 0:
        theta += math.pi
        rho = -rho
    return numpy.asarray([rho, theta])
# }}}

#
# In image coordinates, origin is in the top-left corner, nevertheless,
# for lane detection purposes, it is more useful to have coordinates taking
# as origin the center of the car-hood, which corresponds to the bottom-center
# point in the image. This function makes such transformation.
#
#Translate lines to bottom center{{{
def translate_lines_to_bottom_center(lines, x_center, y_center):
    if lines is None:
        return None
    new_lines = []
    for x1, y1, x2, y2 in lines:
        nx1 = x1 - x_center
        nx2 = x2 - x_center
        ny1 = y_center - y1
        ny2 = y_center - y2
        new_lines.append([nx1, ny1, nx2, ny2])
    return new_lines
# }}}

#
# Draws a line given in normal form, in coordinates wrt car's hood.
#
# Draw normal line{{{
def draw_normal_line(rho, theta, length, img,color):
    if rho == 0 or theta == 0:
        return
    a  = math.cos(theta)
    b  = math.sin(theta)
    x1 = int(a*rho - b*length + img.shape[1]/2)
    y1 = int(img.shape[0] - (b*rho + a*length))
    x2 = int(a*rho + b*length + img.shape[1]/2)
    y2 = int(img.shape[0] - (b*rho - a*length))
    delta = 3
    """
    pts = np.array(
            [
                [
                    x1-delta, y1-delta
                ],[
                    x1+delta, y1+delta
                ],[
                    x2+delta, y2+delta
                ],[
                    x2-delta, y2-delta
                ]
            ],
            np.int32)
    img = cv2.polylines(img, [pts], True, color, 2)
    """
    cv2.line(img, (x1, y1), (x2, y2), color, 3, cv2.LINE_AA)
    cv2.line(img, (x1 - delta, y1), (x2 - delta, y2), color, 3, cv2.LINE_AA)
    cv2.line(img, (x1 + delta, y1), (x2 + delta, y2), color, 3, cv2.LINE_AA)
    """
    mask = np.zeros(img.shape, np.uint8)
    cv2.drawContours(mask, c, -1, 255, -1)
    mean = cv.mean(frame, mask=mask)
    """
#}}}

#
# Convert to grayscale              
# Apply blur filter to reduce noise 
# Canny edge detector               
#
# Detect edges{{{
def detect_edges(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) 
    blur = cv2.GaussianBlur(gray, (5, 5), 0)       
    canny = cv2.Canny(blur, 50, 150)               
    return canny
#}}}

#
# This function removes all lines with slopes near to horizontal al vertical lines.
# It returns lines in two sets: left-border lines and right-border lines.
# Classification is made based only on angle theta
#
# filter lines {{{
def filter_lines(lines):
    left_lines  = []
    right_lines = []
    for x1, y1, x2, y2 in lines:
        rho, theta = to_normal_form(x1, y1, x2, y2)
        if (theta > -(math.pi/2-0.3) and theta < -0.1) or (theta > 0.1 and theta < (math.pi/2 - 0.3)):
            right_lines.append([x1, y1, x2, y2])
        if (theta > (math.pi/2 + 0.3) and theta < math.pi*0.9) or (theta > -0.9*math.pi and theta < -(math.pi/2 + 0.3)):
            left_lines.append([x1, y1, x2, y2])
    left_lines  = left_lines  if len(left_lines)  > 0 else None
    right_lines = right_lines if len(right_lines) > 0 else None
    return left_lines, right_lines
#}}}

#
# Calculates a weighted average of all lines detected. Longer lines have greater weight.
# Average is calculated using lines in normal form. 
#
# Wighted average{{{
def weighted_average(lines):
    if lines is None or len(lines) == 0:
        return 0, 0
    weights = numpy.asarray([math.sqrt((x2 - x1)**2 + (y2 - y1)**2) for x1, y1, x2, y2 in lines])
    weights = weights/sum(weights)
    weighted_average = numpy.asarray([0.0,0.0])
    for i in range(len(lines)):
        x1, y1, x2, y2 = lines[i]
        rho, theta = to_normal_form(x1, y1, x2, y2)
        weighted_average[0] += rho*weights[i]
        weighted_average[1] += theta*weights[i]
    return weighted_average[0], weighted_average[1]
#}}}

#
#
#
# Color filter{{{
def color_filter(frame):
    global kernel, result, lower_color, upper_color
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array(lower_color), np.array(upper_color))
    result = cv2.bitwise_and(frame, frame, mask = mask)
    return result
#}}}

#
#
#
# 
def box_finder(img):
    local_kernel = np.ones((5, 5), np.uint8)
    imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    ret,thresh = cv2.threshold(imgray,125,255,0)
    im2, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    c = max(contours, key=cv2.contourArea)
    rect = cv2.minAreaRect(c)
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    return box

#
#
#
# New zone{{{
def new_zone(img):
    box = []
    left_img = np.zeros_like(img)
    right_img = np.zeros_like(img)
    left_img[:, :int(0.5 * img.shape[1]), :] = img[:, :int(0.5 * img.shape[1]), :]
    right_img[:, int(0.5 * img.shape[1]):, :] = img[:, int(0.5 * img.shape[1]):, :]
    left_box = box_finder(left_img)
    right_box = box_finder(right_img)
    return left_box, right_box
    #print(box)
#}}}

#
#
#
# New color filters{{{
def new_color_filters(img, l_box, r_box):
    global lower_color, upper_color
    mask = np.zeros(img.shape[:2], np.uint8)
    cv2.drawContours(mask, [l_box], -1, 255, -1)
    cv2.drawContours(mask, [r_box], -1, 255, -1)
    mean, stdev = cv2.meanStdDev(cv2.cvtColor(img, cv2.COLOR_BGR2HSV), mask)
    channel = 1
    for channel in [0, 1, 2]:
        lower = int(mean[channel][0] - (2 *stdev[channel][0]))
        upper = int(mean[channel][0] + (2 * stdev[channel][0]))
        if lower < 0:
            lower = 0
        if upper > 255:
            upper = 255
        lower_color[channel] = lower
        print("Changed lower value:{}".format(lower_color))
        upper_color[channel] = upper
        print("Changed upper value:{}".format(upper_color))
#}}}

#
# Image callback. For detecting lane borders, the following steps are performed:
# - Crop image to consider only the part below horizon
# - Conversion to grayscale, gaussian filtering and Canny border detection
# - Detect lines from borders using Hough transform
# - Filter lines to keep only the ones which are more likely to be a lane border
# - Perform a weighted average
# - Publish detected lanes
#
# Image callback{{{
def callback_rgb_image(msg):
    global pub_left_lane, pub_right_lane
    global debug, img_publisher, brdg
    global result
    bridge = CvBridge()
    print("Bridge")
    img   = bridge.imgmsg_to_cv2(msg, 'bgr8')
    img   = img[int(0.4*img.shape[0]):int(0.9*img.shape[0]) ,:,:]
    frame = img.copy()
    img = color_filter(img)
    canny = detect_edges(img)
    print("canny")
    lines = cv2.HoughLinesP(canny, 2, numpy.pi/180, 80, minLineLength=80, maxLineGap=100)[:,0]
    lines = translate_lines_to_bottom_center(lines, img.shape[1]/2, img.shape[0])
    left_lines, right_lines = filter_lines(lines)
    mean_rho_l, mean_theta_l = weighted_average(left_lines)
    mean_rho_r, mean_theta_r = weighted_average(right_lines)
    msg_left_lane  = Float64MultiArray()
    msg_right_lane = Float64MultiArray()
    msg_left_lane.data  = [mean_rho_l, mean_theta_l]
    msg_right_lane.data = [mean_rho_r, mean_theta_r]
    pub_left_lane.publish(msg_left_lane)
    pub_right_lane.publish(msg_right_lane)
    draw_normal_line(mean_rho_l, mean_theta_l, frame.shape[0], frame, (255,0,0))
    draw_normal_line(mean_rho_r, mean_theta_r, frame.shape[0], frame, (0,0,255))
    l_box, r_box = new_zone(img)
    new_color_filters(frame, l_box, r_box)
    cv2.drawContours(img, [l_box], 0, (255, 0, 0), 2)
    cv2.drawContours(img, [r_box], 0, (0, 0, 255), 2)
    img_msg = brdg.cv2_to_imgmsg(img)
    img_msg.encoding = "bgr8"
    img_publisher.publish(img_msg)
    if debug:
        cv2.imshow("New region of interest", frame)
        cv2.imshow("New filter", img)
        cv2.waitKey(1)
#}}}

#
# Main{{{
def main():
    global pub_left_lane, pub_right_lane
    global debug, img_publisher, brdg
    print("INITIALIZING LANE DETECTION DEMO...")
    rospy.init_node("lane_detector")
    rospy.Subscriber('/toxic/main_camera', Image, callback_rgb_image)
    img_publisher = rospy.Publisher("/lane_image", Image, queue_size=10)
    debug = False
    brdg = CvBridge()
    if rospy.has_param('~debug'):
        if rospy.get_param('~debug') == 1:
            debug = True
    pub_left_lane  = rospy.Publisher("/demo/left_lane" , Float64MultiArray, queue_size=10)
    pub_right_lane = rospy.Publisher("/demo/right_lane", Float64MultiArray, queue_size=10)
    rate = rospy.Rate(30)
    while not rospy.is_shutdown():
        rate.sleep()
#}}}

if __name__ == "__main__":
    main()
