#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import rospy
from std_msgs.msg import Float32
from sensor_msgs import Joy
#import joy

"""
    axes[
    0.0 LX
    0.0 LY
    0.0 LT
    -0.0 RX
    -0.0 RY
    1.0 RT
    0.0 CX
    0.0 CY
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

msgJoy = ""
speed = 0

def callback_joy(msg):
    global msgJoy
    print(msg)
    msgJoy = msg.data


def main():
    global speed, msgJoy
    print("INITIALIZING JOY READER NODE...")
    rospy.init_node("joy_node_reader")
    rospy.Subscriber("/joy", Joy, callback_joy)
    loop = rospy.Rate(10)
    while not rospy.is_shutdown():
        print(msgJoy)
        loop.sleep()

main()

