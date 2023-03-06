#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

writer = None

def callback_raw_image(data):
    global writer
    brdg = CvBridge()
    raw_frame = brdg.imgmsg_to_cv2(data)
    if writer == None:
        size = (raw_frame.shape[1], raw_frame.shape[0])
        writer = cv2.VideoWriter('filename.avi', 
                cv2.VideoWriter_fourcc(*'MJPG'),
                30, size)
    writer.write(raw_frame)

def main():
    global writer
    rospy.init_node('raw_img_subscriber', anonymous = True)
    rospy.Subscriber('/raw_image', Image, callback_raw_image)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

