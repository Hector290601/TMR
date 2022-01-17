#!/usr/bin/env python3
#-*- coding: utf-8 -*-

"""
axes[
    -0.0 LX
    -0.0 LY
    1.0 LT
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

import rospy
from sensor_msgs.msg import Joy
from std_msgs.msg import Float32
import math

joyLeft = ""
speed = ""
steering = ""
pwm = 0

def callback_joy(msg):
    global speed, pwm
    if msg.axes[-1] == 1.:
        pwm += 0.01
    elif msg.axes[-1] == -1.:
        pwm -= 0.01
    print(msg.axes[-1])
    speed.publish(pwm)

def main():
    global msgJoy, speed, steering
    print("INITIALIZING JOY READER NODE...")
    rospy.init_node('speed_talker', anonymous=True)
    speed = rospy.Publisher('/speed', Float32, queue_size=10)
    rospy.Subscriber("/joy", Joy, callback_joy)
    loop = rospy.Rate(10)
    while not rospy.is_shutdown():
        loop.sleep()
main()

