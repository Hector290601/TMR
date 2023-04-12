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
max_speed =  0.15
max_steering = 0.6

def callback_joy(msg):
    global joyLeft, pub, speed, steering
    velocidad = msg.axes[4]
    turbo = msg.axes[5]
    to_publish = 0.0
    if velocidad > 0:
        to_publish = (max_speed * velocidad) + ((1 - max_speed)*((1-turbo) / 2.0))
        #speed.publish((0.1 * velocidad) + (0.9 * (0.5 * ( 1 - turbo))))
    elif velocidad < 0:
        to_publish = (max_speed * velocidad) - ((1 - max_speed)*((1-turbo) / 2.0))
        #speed.publish((0.1 * velocidad) - (0.9 * (0.5 * ( 1 - turbo))))
        #speed.publish((max_speed * velocidad) - ((1 - max_speed)*((1*turbo) / 2.0)))
    else:
        to_publish = 0.0
    speed.publish(to_publish)
    steering.publish(( msg.axes[3] * max_steering ))

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

