#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def main():
    pub = rospy.Publisher("video_frames", Image, queue_size=10)
    rospy.init_node("sample_image")
    rate = rospy.Rate(10)
    cap = cv2.imread("test.jpeg")
    br = CvBridge()
    while True:
        pub.publish(br.cv2_to_imgmsg(cap))
        rate.sleep()

if __name__ == "__main__":
    main()
