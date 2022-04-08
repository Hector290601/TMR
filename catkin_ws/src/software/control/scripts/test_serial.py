#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float32
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
import math
from datetime import datetime

def main():
    print("INITIALIZING LANES CONTROL NODE...")
    rospy.init_node('hardware_control', anonymous=True)
    speed = rospy.Publisher('/speed', Float32, queue_size=10)
    steering = rospy.Publisher('/steering', Float32, queue_size=10)
    loop = rospy.Rate(60)
    print("NODE INITIALIZED SUCCESFULLY")
    while not rospy.is_shutdown():
        value = input("ingresa los valores: ")
        value = value.split(",")
        speed.publish(float(value[0]))
        steering.publish(float(value[1]))
        loop.sleep()
    speed.publish(0.0)
    steering.publish(0.0)

main()

