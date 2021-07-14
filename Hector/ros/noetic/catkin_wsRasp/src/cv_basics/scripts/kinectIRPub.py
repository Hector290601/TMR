#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import freenect
import numpy as np

def getVideo():
    array, _ = freenect.sync_get_video(0, freenect.VIDEO_IR_10BIT)
    return array

def prettyDept(depth):
    np.clip(depth, 0, 2**10-1, depth)
    depth >>= 2
    depth = depth.astype(np.uint8)
    return depth

def publishImage():
    pub = rospy.Publisher('videoFrames', Image, queue_size=10)
    rospy.init_node('kinectIRPub', anonymous = True)
    rate = rospy.Rate(30)
    cap = cv2.VideoCapture(0)
    br = CvBridge()
    while not rospy.is_shutdown():
        frame = getVideo()
        frame = prettyDept(frame)
        rospy.loginfo('Publicando video')
        pub.publish(br.cv2_to_imgmsg(frame))
        rate.sleep()

if __name__ == '__main__':
    try:
        publishImage()
    except rospy.ROSInterruptException:
        pass
