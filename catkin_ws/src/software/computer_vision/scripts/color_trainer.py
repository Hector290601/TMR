#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
import os

pts = []
flag = False

def mouse_event(event, x, y, flags, param):
    global pts, flag
    if event == cv2.EVENT_LBUTTONDOWN:
        pts.append([x, y])
    elif event == cv2.EVENT_RBUTTONDOWN:
        pts.append([x, y])
        flag = not flag

def callback_raw_image(data):
    global pts, flag
    brdg = CvBridge()
    raw_frame = brdg.imgmsg_to_cv2(data)
    if flag:
        #cv2.polylines(raw_frame, [np.array(pts)], True, (255, 0, 0))
        os.system("clear")
        rect = cv2.boundingRect(np.array(pts))
        x, y, w, h = rect
        cv2.rectangle(raw_frame, (x - 2, y - 2), (x + w + 2, y + h + 2), (255, 0, 0), 1)
        interest = raw_frame[y:y+h, x:x+w, :]
        print("Mean B: " + str(int(interest[:,:,0].mean()))
                + " Max B: " + str(interest[:,:,0].max())
                + " Min B: " + str(interest[:,:,0].min())
                + " Max Recomended B: " + str(int(interest[:,:,0].mean() + (np.std(interest[:,:,0]) * 2)))
                + " Min Recomended B: " + str(int(interest[:,:,0].mean() - (np.std(interest[:,:,0]) * 2)))
            )
        print("Mean G: " + str(int(interest[:,:,1].mean()))
                + " Max G: " + str(interest[:,:,1].max())
                + " Min G: " + str(interest[:,:,1].min())
                + " Max Recomended G: " + str(int(interest[:,:,1].mean() + (np.std(interest[:,:,1]) * 2)))
                + " Min Recomended G: " + str(int(interest[:,:,1].mean() - (np.std(interest[:,:,1]) * 2)))
            )
        print("Mean R: " + str(int(interest[:,:,2].mean()))
                + " Max R: " + str(interest[:,:,2].max())
                + " Min R: " + str(interest[:,:,2].min())
                + " Max Recomended R: " + str(int(interest[:,:,2].mean() + (np.std(interest[:,:,2]) * 2)))
                + " Min Recomended R: " + str(int(interest[:,:,2].mean() - (np.std(interest[:,:,2]) * 2)))
            )
        flag = False
    cv2.imshow("camera", raw_frame)
    cv2.setMouseCallback('camera', mouse_event)
    cv2.waitKey(1)

def main():
    rospy.init_node('raw_img_subscriber', anonymous = True)
    rospy.Subscriber('/raw_image', Image, callback_raw_image)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

