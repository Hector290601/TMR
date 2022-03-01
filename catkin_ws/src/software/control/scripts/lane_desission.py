#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float32
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
import math

left_lines = ""
right_lines = ""

def decide():
    global left_lines, right_lines
    left = (left_lines[0] + left_lines[2])
    right = (right_lines[0] + right_lines[2])
    summed = right - left
    if summed >= 1.7 or summed <= 1.5:
        print(summed)
        if right <= -0.11:
            #publish steering like 0.5
        elif 

def callback_left(msg):
    global left_lines
    left_lines = msg.data

def callback_right(msg):
    global right_lines
    right_lines = msg.data

def main():
    print("INITIALIZING LANES CONTROL NODE...")
    rospy.init_node('hardware_control', anonymous=True)
    speed = rospy.Publisher('/speed', Float32, queue_size=10)
    steering = rospy.Publisher('/steering', Float32, queue_size=10)
    rospy.Subscriber("/raw_lanes_left", Floats, callback_left)
    rospy.Subscriber("/raw_lanes_right", Floats, callback_right)
    loop = rospy.Rate(10)
    while not rospy.is_shutdown():
        loop.sleep()
main()

