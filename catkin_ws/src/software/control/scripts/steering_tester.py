#!/usr/bin/env python
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float64
import math

def main():
    print("INITIALIZING STEERING TESTER NODE...")
    rospy.init_node('steering_tester', anonymous=True)
    steering = rospy.Publisher('/steering', Float64, queue_size=10)
    loop = rospy.Rate(60)
    angle = 1.5708
    flag = True
    while not rospy.is_shutdown():
        if flag:
            angle += 0.01
            if angle >= 2.0944:
                flag = False
            steering.publish(angle)
            print(angle)
        else:
            angle -= 0.01
            if angle <= 1.0472:
                flag = True
            steering.publish(angle)
            print(angle)
        loop.sleep()
main()

