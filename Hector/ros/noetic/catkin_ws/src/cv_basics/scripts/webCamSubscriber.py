#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def callBack(data):
    br = CvBridge()
    rospy.loginfo("reciving video frame")
    currentFrame = br.imgmsg_to_cv2(data)
    cv2.imshow("camera", currentFrame)
    cv2.waitKey(1)

def reciveMessage():
    rospy.init_node('videoSubPy', anonymous = True)
    rospy.Subscriber('videoFrames', Image, callBack)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    reciveMessage()
