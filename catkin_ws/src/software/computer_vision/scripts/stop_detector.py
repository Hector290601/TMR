#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

upper_color = [179, 233, 255]
lower_color = [170, 72, 127]

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
    for cnt in contours:
        area = cv2.contourArea(cnt) 
        if area > 30000 and area < 60000:
            M = cv2.moments(cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            frame = cv2.circle(frame, (cx, cy), 20, (255, 255, 255))
            print(cv2.contourArea(cnt))
            approx = cv2.convexHull(cnt)
            (x,y),radius = cv2.minEnclosingCircle(cnt)
            center = (int(x),int(y))
            radius = int(radius)
            cv2.circle(frame, center, radius, (0, 0, 255), 2)
            cv2.drawContours(frame, cnt, -1, (0,255,0), 3)
    cv2.imshow('mask', thresh)
    cv2.imshow('original', frame)
    cv2.waitKey(1)

def main():
    rospy.init_node('raw_img_subscriber', anonymous = True)
    rospy.Subscriber('/raw_image', Image, callback_raw_image)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

