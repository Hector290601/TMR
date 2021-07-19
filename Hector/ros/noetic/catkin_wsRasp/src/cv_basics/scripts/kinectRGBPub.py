#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import freenect
import numpy as np

def publishImage():
    pub = rospy.Publisher('videoFrames', Image, queue_size=10)
    rospy.init_node('kinectPub', anonymous = True)
    rate = rospy.Rate(30)
    cap = cv2.VideoCapture(0)
    br = CvBridge()
    while not rospy.is_shutdown():
        rgbVideo, _ = freenect.sync_get_video()
        bgrVideo = cv2.cvtColor(rgbVideo, cv2.COLOR_RGB2BGR)
        frame = bgrVideo.astype(np.uint8)
        rospy.loginfo('Publicando video')
        pub.publish(br.cv2_to_imgmsg(frame))
        rate.sleep()

if __name__ == '__main__':
    try:
        publishImage()
    except rospy.ROSInterruptException:
        pass
