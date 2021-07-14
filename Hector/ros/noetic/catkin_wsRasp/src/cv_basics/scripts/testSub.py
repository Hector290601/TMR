#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def callback(data):
    br = CvBridge()
    rospy.loginfo('Recibiendo video en test')
    currentFrame = br.imgmsg_to_cv2(data)
    cv2.imshow("cameraEntest", currentFrame)
    cv2.waitKey(1)

def reciveMessage():
    rospy.init_node('videoReSubPytest', anonymous = True)
    rospy.Subscriber('videoFrametest', Image, callback)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    reciveMessage()


