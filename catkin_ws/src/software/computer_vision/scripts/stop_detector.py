#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

upper_color = [175, 233, 198]
lower_color = [171, 170, 160]

def callback_raw_image(data):
    global upper_color, lower_color
    brdg = CvBridge()
    kernel = np.ones((5, 5), np.uint8)
    frame = brdg.imgmsg_to_cv2(data)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array(lower_color), np.array(upper_color))
    result = cv2.bitwise_and(frame, frame, mask = mask)
    img_erosion = cv2.erode(result, kernel, iterations=2)
    img_dilation = cv2.dilate(result, kernel, iterations=2)
    imgray = cv2.cvtColor(img_dilation, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    im2, contours, hierarchy= cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    #print(contours)
    cv2.imshow('mask', thresh)
    #cv2.imshow('result', result)
    cv2.imshow('original', frame)
    cv2.waitKey(1)

def main():
    rospy.init_node('raw_img_subscriber', anonymous = True)
    rospy.Subscriber('/raw_image', Image, callback_raw_image)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

