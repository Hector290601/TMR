#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def publishImage():
    pub = rospy.Publisher('videoFrames', Image, queue_size=10)
    rospy.init_node('videoPub', anonymous = True)
    rate = rospy.Rate(30)
    cap = cv2.
    
    br = CvBridge()
    while not rospy.is_shutdown():
        ret, frame = cap.read()
        if ret == True:
            rospy.loginfo('Publicando video')
            pub.publish(br.cv2_to_imgmsg(frame))
            rate.sleep()

if __name__ == '__main__':
    try:
        publishImage()
    except rospy.ROSInterruptException:
        pass
