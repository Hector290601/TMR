#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def callback_raw_image(data):
    brdg = CvBridge()
    raw_frame = brdg.imgmsg_to_cv2(data)
    cv2.imshow("camera", raw_frame)
    cv2.waitKey(1)

def main():
    rospy.init_node('raw_img_subscriber', anonymous = True)
    rospy.Subscriber('/raw_image', Image, callback_raw_image)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

