#!/usr/bin/env python
#-*- coding: utf-8 -*-

"""
axes[
    -0.0 LX     0
    -0.0 LY     1
    1.0 LT      2
    -0.0 RX     3
    -0.0 RY     4
    1.0 RT      5
    0.0 CX      6
    0.0 CY      7
    ]
buttons[
    0 A
    0 B
    0 X
    0 Y
    0 LB
    0 RB
    0 BACK
    0 START
    0 HOME
    0 RC
    0 LC
    ]
"""

import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float32
from std_msgs.msg import Float64
import math

joyLeft = ""
speed = ""
steering = ""

def callback_joy(msg):
    global joyLeft, pub, speed, steering
    joyLeft = msg.axes[:2]
    speed.publish((0.3 * msg.axes[4]) + (0.7 * (0.5 * ( 1 - msg.axes[5]))))
    steering.publish(1.5 + ( msg.axes[3] * 0.4 ))

def main():
    global msgJoy, speed, steering
    print("INITIALIZING JOY READER NODE...")
    rospy.init_node('speed_talker', anonymous=True)
    speed = rospy.Publisher('/speed', Float32, queue_size=10)
    steering = rospy.Publisher('/steering', Float64, queue_size=10)
    rospy.Subscriber("/joy", Joy, callback_joy)
    loop = rospy.Rate(10)
    while not rospy.is_shutdown():
        loop.sleep()
main()

