#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
import math
import rospy
import serial
from std_msgs.msg import Float32

steering = 0
speed = 0

def callback_steering(msg):
    global steering
    steering = int(msg.data) #Speed in percentage
    if steering > 125:
        steering = 125
    elif steering < 65:
        steering = 65

def main():
    global steering
    print("INITIALIZING MOTOR CONTROL NODE...")
    rospy.init_node("servo_arduino")
    rospy.Subscriber("/steering", Float32, callback_steering)
    loop = rospy.Rate(60)
    steering = 95
    direction = serial.Serial("/dev/ttyACM1", 115200)
    print("ALL SUCCESFULLY INITIALIZED")
    while not rospy.is_shutdown():
        direction.write(chr(steering).encode())
        loop.sleep()

if __name__ == '__main__':
    main()

