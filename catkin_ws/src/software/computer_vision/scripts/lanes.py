#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
import cv2
import numpy as np
import math

lanes_to_publish = ""

def canny_frame(frame_gray):
    blured_frame = cv2.GaussianBlur(frame_gray, (5, 5), 0)
    cannied_frame = cv2.Canny(blured_frame, 10, 350)
    return cannied_frame

def crop_frame(frame_cannied):
    polygon = np.array(
            [
                [
                    (0, 410),
                    (640, 410),
                    (640, 330),
                    (0, 330)
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
                50, 115, 110
                ]
            )
    color_min = np.array(
            [
                0, 25, 60
                ]
            )
    color_mask = cv2.bitwise_and(frame_color, frame_color, mask=frame_interest)
    ranged_frame = cv2.inRange(color_mask, color_min, color_max)
    return ranged_frame

def callback_raw_image(data):
    global lanes_to_publish
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
    lines = []
    if possible_lines is not None:
        for line in possible_lines:
            for points in line:
                for number in points:
                    lines.append(number)
    lanes_to_publish = np.array(lines, dtype=np.float32)
    cv2.imshow("interest_frame", interest_frame)
    cv2.waitKey(1)

def main():
    global lanes_to_publish
    rospy.init_node('raw_img_subscriber', anonymous = True)
    rospy.Subscriber('/raw_image', Image, callback_raw_image)
    lanes_publisher = rospy.Publisher("/raw_lanes", numpy_msg(Floats), queue_size=10)
    loop = rospy.Rate(10)
    while not rospy.is_shutdown():
        lanes_publisher.publish(lanes_to_publish)
        loop.sleep()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

