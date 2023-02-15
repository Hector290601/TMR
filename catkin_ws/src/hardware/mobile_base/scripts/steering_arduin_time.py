#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
import math
import rospy
import serial
from std_msgs.msg import Float32

steering = 0

def callback_steering(msg):
    global steering, new_data
    steering = msg.data #Speed in radians
    if steering > 1.4:
        steering = 1.4
    elif steering < 0.5:
        steering = 0.5
    new_data = True

def main():
    global steering, new_data
    new_data = False
    print("INITIALIZING MOTOR CONTROL NODE...")
    rospy.init_node("servo_arduino")
    rospy.Subscriber("/steering", Float32, callback_steering)
    RATE = 1
    loop = rospy.Rate(RATE)
    time_out = int(RATE * 0.5)
    steering = 0.96817
    direction = serial.Serial("/dev/ttyUSB0", 115200)
    print("ALL SUCCESFULLY INITIALIZED")
    while not rospy.is_shutdown():
        """
        if new_data:
            time_out = int(RATE * 0.5)
            new_data = False
        time_out -= 1
        if time_out <= 0:
        direction.write(('d0.96817\n').encode())
            time_out = 0
        else:
            direction.write(('d' + str(steering) + '\n').encode())
        """
        direction.write(('d' + str(steering) + '\n').encode())
        loop.sleep()

if __name__ == '__main__':
    main()

