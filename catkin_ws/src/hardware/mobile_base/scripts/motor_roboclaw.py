#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
import math
import rospy
from std_msgs.msg import Float32
from roboclaw import Roboclaw

speed = 0

def callback_speed(msg):
    global speed, new_data
    speed = int(msg.data * 127.0) #Speed in percentage
    if speed > 127:
        speed = 127
    elif speed < -127:
        speed = -127
    new_data = True

def main():
    global speed, new_data
    new_data = False
    print("INITIALIZING MOTOR CONTROL NODE...")
    rospy.init_node("motor_roboclaw")
    rospy.Subscriber("/speed", Float32, callback_speed)
    RATE = 60
    loop = rospy.Rate(RATE)
    time_out = int(0.5 * RATE)
    speed = 0
    main_motor = Roboclaw("/dev/mhaRC15", 115200)
    i = 0
    while main_motor.Open() == 0:
        print("ERROR")
        i += 1
        if i ==10:
            return False
    print("ALL SUCCESFULLY INITIALIZED")
    while not rospy.is_shutdown():
        if new_data:
            time_out = int(RATE * 0.5)
            new_data = False
        time_out -= 1
        if time_out <= 0:
            main_motor.ForwardM1(0x80, 0)
            time_out = 0
        else:
            if speed == 0:
                main_motor.ForwardM1(0x80, 0)
            elif speed > 0:
                main_motor.ForwardM1(0x80, speed)
            elif speed < 0:
                main_motor.BackwardM1(0x80, 127-speed)
        loop.sleep()

if __name__ == '__main__':
    main()

