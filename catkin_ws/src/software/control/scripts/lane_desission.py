#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float32
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
import math

def callback_joy(msg):
    global speed, steering
    print(msg.data)

def main():
    global msgJoy, speed, steering
    print("INITIALIZING JOY READER NODE...")
    rospy.init_node('hardware_control', anonymous=True)
    speed = rospy.Publisher('/speed', Float32, queue_size=10)
    steering = rospy.Publisher('/steering', Float32, queue_size=10)
    rospy.Subscriber("/raw_lanes", Floats, callback_joy)
    loop = rospy.Rate(10)
    while not rospy.is_shutdown():
        loop.sleep()
main()

