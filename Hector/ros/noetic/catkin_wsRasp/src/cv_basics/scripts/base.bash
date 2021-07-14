#!bin/bash

if [ -n "$1" ]; then
	touch $1Pub.py
	touch $1Sub.py
	touch ../launch/$1.launch
	echo "#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def publishImage(img):
    pub = rospy.Publisher('videoFrame$1', Image, queue_size=10)
    br = CvBridge()
    frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    rospy.loginfo('Publicando video en $1')
    pub.publish(br.cv2_to_imgmsg(frame))

def callback(data):
    br = CvBridge()
    rospy.loginfo('Recibiendo imagen del video para republicar en $1')
    currentFrame = br.imgmsg_to_cv2(data)
    publishImage(currentFrame)

def reciveMessage():
    rospy.init_node('videoSubPy$1', anonymous = True)
    rospy.Subscriber('videoFrames', Image, callback)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    reciveMessage()
">$1Pub.py
	echo "#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

def callback(data):
    br = CvBridge()
    rospy.loginfo('Recibiendo video en $1')
    currentFrame = br.imgmsg_to_cv2(data)
    cv2.imshow(\"cameraEn$1\", currentFrame)
    cv2.waitKey(1)

def reciveMessage():
    rospy.init_node('videoReSubPy$1', anonymous = True)
    rospy.Subscriber('videoFrame$1', Image, callback)
    rospy.spin()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    reciveMessage()

">$1Sub.py
	echo "<launch>
        <node
                pkg=\"cv_basics\"
                type=\"webCamPub.py\"
                name=\"webCamPub\"
                output=\"screen\"
        />
        <node
                pkg=\"cv_basics\"
                type=\"webCamSub.py\"
                name=\"webCamSub\"
                output=\"screen\"
        />
        <node
                pkg=\"cv_basics\"
                type=\"$1Pub.py\"
                name=\"$1Pub\"
                output=\"screen\"
        />
        <node
                pkg=\"cv_basics\"
                type=\"$1Sub.py\"
                name=\"$1Sub\"
                output=\"screen\"
        />
</launch>
">../launch/$1.launch
	chmod +x $1Pub.py
	chmod +x $1Sub.py

else
	echo "Faltan parametros, ejecutar: bash base.bash nombreNuevoNodo"
fi
