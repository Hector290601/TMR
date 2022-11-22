#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float32
import math

def main():
    global msgJoy, speed, steering
    print("INITIALIZING JOY READER NODE...")
    rospy.init_node('speed_talker', anonymous=True)
    steering = rospy.Publisher('/steering', Float32, queue_size=10)
    loop = rospy.Rate(2)
    while not rospy.is_shutdown():
        for i in range(70, 120, 1):
            steering.publish(i)
            loop.sleep()
        for i in range(120, 70, -1):
            steering.publish(i)
            loop.sleep()
main()

