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

def crop_frame(frame_cannied):
    regioned_frame = frame_cannied[345:428, :, :]
    return regioned_frame

def callback_raw_image(data):
    global lanes_to_publish
    brdg = CvBridge()
    raw_frame = brdg.imgmsg_to_cv2(data)
    coppied_frame = np.copy(raw_frame)
    gray_frame = cv2.cvtColor(raw_frame, cv2.COLOR_BGR2GRAY)
    interest_frame = crop_frame(raw_frame) #15
    cv2.imshow("raw_frame", interest_frame)
    cv2.waitKey(1)

def main():
    global lanes_to_publish
    rospy.init_node('raw_img_subscriber', anonymous = True)
    rospy.Subscriber('/raw_image', Image, callback_raw_image)
    loop = rospy.Rate(10)
    while not rospy.is_shutdown():
        loop.sleep()

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

