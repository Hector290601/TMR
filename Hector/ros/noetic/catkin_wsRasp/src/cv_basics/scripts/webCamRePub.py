#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def publishImage(img):
    pub = rospy.Publisher('videoFramesGray', Image, queue_size=10)
    br = CvBridge()
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rospy.loginfo('Publicando video en grises')
    pub.publish(br.cv2_to_imgmsg(frame))

def callback(data):
    br = CvBridge()
    rospy.loginfo('Recibiendo imagen del video para republicar')
    currentFrame = br.imgmsg_to_cv2(data)
    publishImage(currentFrame)

def reciveMessage():
    rospy.init_node('videoSubPy', anonymous = True)
    rospy.Subscriber('videoFrames', Image, callback)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    reciveMessage()

