#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def main():
    pub = rospy.Publisher("/raw_image", Image, queue_size=10)
    rospy.init_node("sample_image")
    rate = rospy.Rate(10)
    cap = cv2.VideoCapture(0)
    br = CvBridge()
    while True:
        ret, frame = cap.read()
        if ret:
            pub.publish(br.cv2_to_imgmsg(frame))
        rate.sleep()

if __name__ == "__main__":
    main()
