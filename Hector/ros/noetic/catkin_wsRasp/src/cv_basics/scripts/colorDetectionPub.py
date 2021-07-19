#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def publishImage(img):
    pub = rospy.Publisher('videoFramecolorDetection', Image, queue_size=10)
    br = CvBridge()
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
    rospy.loginfo('Publicando video en colorDetection')
    pub.publish(br.cv2_to_imgmsg(frame))

def callback(data):
    br = CvBridge()
    rospy.loginfo('Recibiendo imagen del video para republicar en colorDetection')
    currentFrame = br.imgmsg_to_cv2(data)
    publishImage(currentFrame)

def reciveMessage():
    rospy.init_node('videoSubPycolorDetection', anonymous = True)
    rospy.Subscriber('videoFrames', Image, callback)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    reciveMessage()

