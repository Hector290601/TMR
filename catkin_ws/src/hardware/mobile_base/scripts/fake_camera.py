#!/usr/bin/env python
#-*- coding: utf-8 -*-

import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def main():
    global steering, speed
    print("INITIALIZING CAMERA PUBLISHER NODE...")
    rospy.init_node("camera")
    img_publisher = rospy.Publisher("/toxic/main_camera", Image, queue_size=10)
    loop = rospy.Rate(30)
    cap = cv2.VideoCapture("/home/hector/video_test.avi")
    brdg = CvBridge()
    print("CAMERA PUBLISHER NODE INITIALIZED SUCCESFULLY")
    if (cap.isOpened()== False):
        print("Error opening video file")
    frame_counter = 0
    cv2.namedWindow("fake_video", cv2.WINDOW_AUTOSIZE)
    continue_flag = True
    while not rospy.is_shutdown():
        if continue_flag:
            ret, frame = cap.read()
            frame_counter += 1
        else:
            ret = True
        if ret == True:
            img_msg = brdg.cv2_to_imgmsg(frame)
            img_msg.encoding = "bgr8"
            img_publisher.publish(img_msg)
            k = cv2.waitKey(1)
            if k == ord('q') or k == 27:
                break
            elif k == ord('-'):
                cap.set(cv2.CAP_PROP_POS_FRAMES, frame_counter)
                _, frame = cap.read()
                frame_counter -= 1
                continue_flag = False
            elif k == ord('+'):
                cap.set(cv2.CAP_PROP_POS_FRAMES, frame_counter)
                _, frame = cap.read()
                frame_counter += 1
                continue_flag = False
            elif k == ord('c'):
                continue_flag = True
            elif k == ord('p'):
                continue_flag = not continue_flag
            elif k == ord('r'):
                cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                _, frame = cap.read()
                frame_counter = 0
                continue_flag = False
            cv2.imshow("fake_video", frame)
        else:
            cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        loop.sleep()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

