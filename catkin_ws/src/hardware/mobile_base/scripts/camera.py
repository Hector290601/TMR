#!/usr/bin/env python
#-*- coding: utf-8 -*-

import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main():
    global steering, speed
    print("INITIALIZING CAMERA PUBLISHER NODE...")
    rospy.init_node("camera")
    img_publisher = rospy.Publisher("/raw_image", Image, queue_size=10)
    loop = rospy.Rate(60)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FPS, 30)
    brdg = CvBridge()
    print("CAMERA PUBLISHER NODE INITIALIZED SUCCESFULLY")
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret == True:
            img_msg = brdg.cv2_to_imgmsg(frame)
            img_msg.encoding = "bgr8"
            img_publisher.publish(img_msg)
        loop.sleep()

if __name__ == '__main__':
    main()

