#!/usr/bin/env python
import math
import cv2
import numpy
import rospy
from std_msgs.msg import Float64MultiArray
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

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

def draw_normal_line(rho, theta, length, img,color):
    if rho == 0 or theta == 0:
        return
    a  = math.cos(theta)
    b  = math.sin(theta)
    x1 = int(a*rho - b*length + img.shape[1]/2)
    y1 = int(img.shape[0] - (b*rho + a*length))
    x2 = int(a*rho + b*length + img.shape[1]/2)
    y2 = int(img.shape[0] - (b*rho - a*length))
    cv2.line(img, (x1, y1), (x2, y2), color, 3, cv2.LINE_AA)

def detect_edges(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY) 
    blur = cv2.GaussianBlur(gray, (5, 5), 0)       
    canny = cv2.Canny(blur, 50, 150)               
    return canny

def filter_lines(lines):
    left_lines  = []
    right_lines = []
    extra_lines = []
    for x1, y1, x2, y2 in lines:
        rho, theta = to_normal_form(x1, y1, x2, y2)
        if (theta > -(math.pi/2-0.3) and theta < -0.1) or (theta > 0.1 and theta < (math.pi/2 - 0.3)):
            right_lines.append([x1, y1, x2, y2])
        elif (theta > (math.pi/2 + 0.3) and theta < math.pi*0.9) or (theta > -0.9*math.pi and theta < -(math.pi/2 + 0.3)):
            left_lines.append([x1, y1, x2, y2])
        else:
      	    extra_lines.append([x1, y1, x2, y2])
    left_lines  = left_lines  if len(left_lines)  > 0 else None
    right_lines = right_lines if len(right_lines) > 0 else None
    extra_lines = extra_lines if len(extra_lines) > 0 else None
    return left_lines, right_lines, extra_lines

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

def color_filter(frame):
    lower_color = [0, 0, 203] 
    upper_color = [115, 23, 254]
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(lab, numpy.array(lower_color), numpy.array(upper_color))
    result = cv2.bitwise_and(frame, frame, mask = mask)
    return result

def callback_rgb_image(msg):
    global pub_left_lane, pub_right_lane, pub_parking_lane, img_pub
    bridge = CvBridge()
    img   = bridge.imgmsg_to_cv2(msg, 'bgr8')
    img = color_filter(img)
    canny = detect_edges(img)
    try:
        lines = cv2.HoughLinesP(canny, 2, numpy.pi/180, 80, minLineLength=80, maxLineGap=100)[:,0]
        lines = translate_lines_to_bottom_center(lines, img.shape[1]/2, img.shape[0])
        left_lines, right_lines, extra_lines = filter_lines(lines)
        mean_rho_l, mean_theta_l = weighted_average(left_lines)
        mean_rho_r, mean_theta_r = weighted_average(right_lines)
        mean_rho_e, mean_theta_e = weighted_average(extra_lines)
        msg_left_lane  = Float64MultiArray()
        msg_right_lane = Float64MultiArray()
        msg_parking_lane = Float64MultiArray()
        msg_left_lane.data  = [mean_rho_l, mean_theta_l]
        msg_right_lane.data = [mean_rho_r, mean_theta_r]
        msg_parking_lane.data = [mean_rho_e, mean_theta_e]
        pub_left_lane.publish(msg_left_lane)
        pub_right_lane.publish(msg_right_lane)
        pub_parking_lane.publish(msg_parking_lane)
        draw_normal_line(mean_rho_l, mean_theta_l, img.shape[0], img, (255,0,0))
        draw_normal_line(mean_rho_r, mean_theta_r, img.shape[0], img, (0,0,255))
        draw_normal_line(mean_rho_e, mean_theta_e, img.shape[0], img, (0,255,255))
        ros_img = bridge.cv2_to_imgmsg(img, encoding="passthrough")
        img_pub.publish(ros_img)
    except:
        pass

def main():
    global pub_left_lane, pub_right_lane, pub_parking_lane, img_pub
    print("INITIALIZING LANE DETECTION NODE...")
    rospy.init_node("lane_detector")
    rospy.wait_for_message('/raw_image', Image)
    rospy.Subscriber('/raw_image', Image, callback_rgb_image)
    img_pub = rospy.Publisher('/camera/rgb/lanes', Image, queue_size=10)
    pub_left_lane  = rospy.Publisher("/left_lane" , Float64MultiArray, queue_size=10)
    pub_right_lane = rospy.Publisher("/right_lane", Float64MultiArray, queue_size=10)
    pub_parking_lane = rospy.Publisher("/parking_lane", Float64MultiArray, queue_size=10)
    rate = rospy.Rate(10)
    rospy.spin()
    

if __name__ == "__main__":
    try:
        main()
    except:
        rospy.ROSInterruptException
        pass

    

