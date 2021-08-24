#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np

def publishImage(img):
    pub = rospy.Publisher('videoFramemorph', Image, queue_size=10)
    br = CvBridge()
    puntos1 = np.float32(
                [
                    [0, 400],
                    [640, 400],
                    [420, 240],
                    [100, 240]
                ]
            )
    puntos2 = np.float32(
                [
                    [0, 0],
                    [0, 480],
                    [640, 480],
                    [640, 0]
                ]
            )
    m = cv2.getPerspectiveTransform(puntos1, puntos2)
    transformada = cv2.warpPerspective(img, m, (640, 480))
    izquierda = transformada[:150, :300, :]
    derecha = transformada[300:480, :300, :]
    kernel = np.ones((20, 20), np.uint8)
    gradientI = cv2.morphologyEx(izquierda, cv2.MORPH_GRADIENT, kernel)
    topI = cv2.morphologyEx(izquierda, cv2.MORPH_TOPHAT, kernel)
    blackI = cv2.morphologyEx(izquierda, cv2.MORPH_BLACKHAT, kernel)
    superPosI = cv2.addWeighted(gradientI, 0.5, topI, 0.5, 0)
    superPosI = cv2.addWeighted(superPosI, 0.5, blackI, 0.5, 0)
    gradientD = cv2.morphologyEx(derecha, cv2.MORPH_GRADIENT, kernel)
    topD = cv2.morphologyEx(derecha, cv2.MORPH_TOPHAT, kernel)
    blackD = cv2.morphologyEx(derecha, cv2.MORPH_BLACKHAT, kernel)
    superPosD = cv2.addWeighted(gradientD, 0.5, topD, 0.5, 0)
    superPosD = cv2.addWeighted(superPosD, 0.6, blackD, 0.4, 0)
    frame = np.concatenate((superPosI, superPosD), axis = 0)
    rospy.loginfo('Publicando video en morph')
    pub.publish(br.cv2_to_imgmsg(frame))

def callback(data):
    br = CvBridge()
    rospy.loginfo('Recibiendo imagen del video para republicar en morph')
    currentFrame = br.imgmsg_to_cv2(data)
    publishImage(currentFrame)

def reciveMessage():
    rospy.init_node('videoSubPymorph', anonymous = True)
    rospy.Subscriber('videoFrames', Image, callback)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    reciveMessage()

