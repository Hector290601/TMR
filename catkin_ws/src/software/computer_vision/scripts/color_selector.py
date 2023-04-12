#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

frame = None

upper_color = [0, 0, 0]
lower_color = [255, 255, 255]

def mouse_click(event, x, y, 
                flags, param):
    global points, frame, upper_color, lower_color, hsv
    if event == cv2.EVENT_LBUTTONDOWN:
        h, s, v = hsv[y, x][0], hsv[y, x][1], hsv[y, x][2]
        uh, us, uv = upper_color
        lh, ls, lv = lower_color
        if h > uh:
            upper_color[0] = h
            print("Upper H channel changed from {} to {}".format(uh, h))
        if s > us:
            upper_color[1] = s
            print("Upper S channel changed from {} to {}".format(us, s))
        if v > uv:
            upper_color[2] = v
            print("Upper V channel changed from {} to {}".format(uv, v))
        if h < lh:
            lower_color[0] = h
            print("Lower H channel changed from {} to {}".format(lh, h))
        if s < ls:
            lower_color[1] = s
            print("Lower S channel changed from {} to {}".format(ls, s))
        if v < lv:
            lower_color[2] = v
            print("Lower V channel changed from {} to {}".format(lv, v))
    if event == cv2.EVENT_RBUTTONDOWN:
        points = []
        upper_color = [0, 0, 0]
        lower_color = [255, 255, 255]

def callback_raw_image(data):
    global points, frame, hsv
    global upper_color, lower_color
    brdg = CvBridge()
    frame = brdg.imgmsg_to_cv2(data)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    mask = cv2.inRange(hsv, np.array(lower_color), np.array(upper_color))
    result = cv2.bitwise_and(frame, frame, mask = mask)
    #cv2.imshow('mask', mask)
    cv2.imshow("hsv", hsv)
    cv2.imshow('result', result)
    cv2.imshow('original', frame)
    #cv2.setMouseCallback('camera', mouse_click)
    #cv2.setMouseCallback('mask', mouse_click)
    cv2.setMouseCallback('result', mouse_click)
    cv2.setMouseCallback('original', mouse_click)
    cv2.setMouseCallback('hsv', mouse_click)
    k = cv2.waitKey(1)
    if k == ord('q'):
        exit()
    elif k == ord('p'):
        uh, us, uv = upper_color
        lh, ls, lv = lower_color
        print("Lower: (H:{},S:{},V:{})\nUpper: (H:{},S:{},V:{})".format(
            lh, ls, lv,
            uh, us, uv
            )
        )

def main():
    rospy.init_node('raw_img_subscriber', anonymous = True)
    rospy.Subscriber('/raw_image', Image, callback_raw_image)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

