#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
import cv2
import numpy as np
import math
import os

lanes_to_publish_left = ""
lanes_to_publish_right = ""

def canny_frame(frame_gray):
    blured_frame = cv2.GaussianBlur(frame_gray, (5, 5), 0)
    cannied_frame = cv2.Canny(blured_frame, 10, 350)
    return cannied_frame

def crop_frame(frame_cannied):
    polygon = np.array(
            [
                [
                    (0, 428),
                    (640, 428),
                    (640, 355),
                    (0, 355)
                    ]
                ]
            )
    zeros = np.zeros_like(frame_cannied)
    cv2.fillPoly(zeros, polygon, 255)
    regioned_image = cv2.bitwise_and(frame_cannied, frame_cannied, mask = zeros)
    return regioned_image

def color_seg(frame_color, frame_gray, frame_interest):
    color_max = np.array(
            [
                203, 196, 193
                ]
            )
    color_min = np.array(
            [
                21, 22, 16
                ]
            )
    color_mask = cv2.bitwise_and(frame_color, frame_color, mask=frame_interest)
    ranged_frame = cv2.inRange(color_mask, color_min, color_max)
    return ranged_frame

def averaged_slope_intercept(intercept_frame, intercept_lines):
    left_fit = []
    right_fit = []
    for line in intercept_lines:
        rho = line[0][0]
        theta = line[0][1]
        a = math.cos(theta)
        b = math.sin(theta)
        x1 = a * rho
        y1 = b * rho
        pt1 = (int(x1 + 1000 * (-b)), int(y1 + 1000 * (a)))
        pt2 = (int(x1 - 100 * (-b)), int(y1 - 100 * (a)))
        params = np.polyfit(pt1, pt2, 1)
        slope = params[0]
        intercept = params[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
    left_average = np.average(left_fit, axis = 0)
    right_average = np.average(right_fit, axis = 0)
    left_line = make_coordinates(intercept_frame, left_average) # 67
    right_line = make_coordinates(intercept_frame, right_average) # 67
    return np.array([left_line, right_line])

def make_coordinates(coordinates_frame, line_params):
    try:
        slope, intercept = line_params
        y1 = coordinates_frame.shape[0]
        y2 = int(y1*(3/5))
        x1 = int((y1-intercept)/slope)
        x2 = int((y2-intercept)/slope)
        return np.array([x1, y1, x2, y2])
    except:
        return np.array([0, 0, 0, 0])

def callback_raw_image(data):
    global lanes_to_publish_left, lanes_to_publish_right
    brdg = CvBridge()
    raw_frame = brdg.imgmsg_to_cv2(data)
    coppied_frame = np.copy(raw_frame)
    gray_frame = cv2.cvtColor(raw_frame, cv2.COLOR_BGR2GRAY)
    cannied_frame = canny_frame(gray_frame) #10
    interest_frame = crop_frame(cannied_frame) #15
    color_frame = color_seg(coppied_frame, gray_frame, interest_frame) #31
    possible_lines_p = cv2.HoughLinesP(color_frame, 1, np.pi/180, 50, 
            minLineLength=20, maxLineGap=50)
    possible_lines = cv2.HoughLines(color_frame, 1, np.pi/180, 50)
    linesL = []
    linesR = []
    if possible_lines is not None:
        os.system("clear")
        print(possible_lines)
        for line in possible_lines:
            rho = line[0][0]
            theta = line[0][1]
            a = math.cos(theta)
            b = math.sin(theta)
            x1 = a * rho
            y1 = b * rho
            pt1 = (int(x1 + 1000 * (-b)), int(y1 + 1000 * (a)))
            pt2 = (int(x1 - 1000 * (-b)), int(y1 - 1000 * (a)))
            if rho <= 340:
                cv2.line(raw_frame, pt1, pt2, (255, 0, 0), 3)
            elif rho >= 340:
                cv2.line(raw_frame, pt1, pt2, (0, 255, 0), 3)
        """
        averaged_lines = averaged_slope_intercept(raw_frame, possible_lines)# 50
        left = averaged_lines.reshape(8)[:4]
        for line in left:
                linesL.append(line)
        right = averaged_lines.reshape(8)[4:]
        for line in right:
                linesR.append(line)
        cv2.line(raw_frame, right[:2], right[2:], (0, 255, 0), 3)
        """
    #lanes_to_publish_left = np.array(linesL, dtype=np.float32)
    #lanes_to_publish_right = np.array(linesR, dtype=np.float32)
    cv2.imshow("raw_frame", raw_frame)
    cv2.waitKey(1)

def main():
    global lanes_to_publish_left, lanes_to_publish_right
    rospy.init_node('raw_img_subscriber', anonymous = True)
    rospy.Subscriber('/raw_image', Image, callback_raw_image)
    lanes_publisherL = rospy.Publisher("/raw_lanes_left", numpy_msg(Floats), queue_size=10)
    lanes_publisherR = rospy.Publisher("/raw_lanes_right", numpy_msg(Floats), queue_size=10)
    loop = rospy.Rate(10)
    while not rospy.is_shutdown():
        lanes_publisherL.publish(lanes_to_publish_left)
        lanes_publisherR.publish(lanes_to_publish_right)
        loop.sleep()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

