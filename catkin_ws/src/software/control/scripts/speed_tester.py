#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float32
import math

def main():
    global msgJoy, speed, steering
    print("INITIALIZING JOY READER NODE...")
    rospy.init_node('speed_talker', anonymous=True)
    speed = rospy.Publisher('/speed', Float32, queue_size=10)
    loop = rospy.Rate(10)
    while not rospy.is_shutdown():
        for i in range(0, 50, 1):
            speed.publish(i)
            loop.sleep()
        for i in range(50, 0, -1):
            speed.publish(i)
            loop.sleep()
main()

