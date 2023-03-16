#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import time
import sys
import time

writer = None
count = 0
n_frames = int(sys.argv[1])

def callback_raw_image(data):
    global writer, count, n_frames
    """
    brdg = CvBridge()
    raw_frame = brdg.imgmsg_to_cv2(data)
    if writer == None:
        size = (raw_frame.shape[1], raw_frame.shape[0])
        writer = cv2.VideoWriter('mha@' + str(time.time()) + '.avi' , 
                cv2.VideoWriter_fourcc(*'MJPG'),
                30, size)
    writer.write(raw_frame)
    """
    n_frames -=1

def main():
    global writer, n_frames
    rospy.init_node('raw_img_subscriber', anonymous = True)
    rospy.Subscriber('/raw_image', Image, callback_raw_image)
    rate = rospy.Rate(30)
    start = time.time()
    while n_frames > 0:  #not rospy.is_shutdown() and n_frames > 0:
        rate.sleep()
    end = time.time()
    print(end - start)
if __name__ == "__main__":
    main()

