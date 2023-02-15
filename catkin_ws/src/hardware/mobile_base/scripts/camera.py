#!/usr/bin/env python
#-*- coding: utf-8 -*-

import cv2
import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

steering = 0
speed = 0
rbc = None

def main():
    global steering, speed
    print("INITIALIZING CAMERA PUBLISHER NODE...")
    rospy.init_node("mobile_base")
    img_publisher = rospy.Publisher("/raw_image", Image, queue_size=10)
    loop = rospy.Rate(60)
    cap = cv2.VideoCapture(0)
    brdg = CvBridge()
    print("CAMERA PUBLISHER NODE INITIALIZED SUCCESFULLY")
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret == True:
            img_publisher.publish(brdg.cv2_to_imgmsg(frame))
        loop.sleep()

if __name__ == '__main__':
    main()

