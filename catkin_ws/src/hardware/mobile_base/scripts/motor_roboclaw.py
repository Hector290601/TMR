#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
import math
import rospy
from std_msgs.msg import Float32
from roboclaw import Roboclaw

steering = 0
speed = 0

def callback_speed(msg):
    global speed
    speed = int(msg.data) #Speed in percentage
    if speed > 127:
        speed = 127
    elif speed < 0:
        speed = 0

def main():
    global steering, speed
    print("INITIALIZING MOTOR CONTROL NODE...")
    rospy.init_node("motor_roboclaw")
    rospy.Subscriber("/speed", Float32, callback_speed)
    loop = rospy.Rate(60)
    speed = 0
    main_motor = Roboclaw("/dev/ttyACM0", 115200)
    if main_motor.Open() == 0:
        return False
    print("ALL SUCCESFULLY INITIALIZED")
    while not rospy.is_shutdown():
        main_motor.ForwardM1(0x80, speed)
        loop.sleep()

if __name__ == '__main__':
    main()

