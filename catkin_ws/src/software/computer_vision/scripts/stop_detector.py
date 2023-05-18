#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
from std_msgs.msg import Bool

stop = None
kernel = None


lower_color = [0, 198, 96] 
upper_color = [3, 227, 112]


def callback_raw_image(data):
    global upper_color, lower_color, kernel
    brdg = CvBridge()
    frame = brdg.imgmsg_to_cv2(data)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, np.array(lower_color), np.array(upper_color))
    #result = cv2.bitwise_and(frame, frame, mask = mask)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=1)
    #imgray = cv2.cvtColor(img_dilation, cv2.COLOR_BGR2GRAY)
    #thresh = cv2.adaptiveThreshold(img_dilation,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) < 1:
        stop.publish(False)
        return
    area = max([cv2.contourArea(cnt) for cnt in contours])
    print(area)
    if area > 500:# and area < 7000:
        stop.publish(True)
    else:
        stop.publish(False)
    """
    for cnt in contours:
        area = cv2.contourArea(cnt) 
        #print(area)
        if area > 7000:# and area < 7000:
            M = cv2.moments(cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            frame = cv2.circle(frame, (cx, cy), 20, (255, 255, 255))
            #approx = cv2.convexHull(cnt)
            (x,y),radius = cv2.minEnclosingCircle(cnt)
            center = (int(x),int(y))
            radius = int(radius)
            #cv2.circle(frame, center, radius, (0, 0, 255), 2)
            #cv2.drawContours(frame, cnt, -1, (0,255,0), 3)
            stop.publish(True)
        else:
            stop.publish(False)
    cv2.imshow('mask', mask)
    #cv2.imshow('original', frame)
    cv2.waitKey(1)
    """

def main():
    global stop, kernel
    #kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    kernel = np.ones((5, 5), np.uint8)
    rospy.init_node('raw_img_subscriber', anonymous = True)
    rospy.Subscriber('/raw_image', Image, callback_raw_image)
    rospy.Subscriber('/raw_image', Image, callback_raw_image)
    stop = rospy.Publisher("/stop", Bool, queue_size=10)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

