#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def callback(data):
    br = CvBridge()
    rospy.loginfo('Recibiendo imagen del video en grises')
    currentFrame = br.imgmsg_to_cv2(data)
    cv2.imshow("camera", currentFrame)
    cv2.waitKey(1)

def reciveMessage():
    rospy.init_node('videoReSubPy', anonymous = True)
    rospy.Subscriber('videoFramesGray', Image, callback)
    #rospy.Subscriber('video_frames', Image, callback)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    reciveMessage()

