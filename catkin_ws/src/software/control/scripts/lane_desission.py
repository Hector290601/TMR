#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float32
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
import math

left_lines = ""
right_lines = ""
const = 180/math.pi
steering_value = Float32(0)
speed_valie = Float32(0)

def error_rho(rho_left, rho_right):
    e = ( 1/2 * (409 - rho_left) ) + ( 1/2 * (247 - rho_right) )
    return e

def error_theta(theta_left, theta_right):
    e = ( 1/2 * (1.36 - theta_left) ) + ( 1/2 * (1.87 - theta_right) )
    return e

def decide():
    global left_lines, right_lines, const, speed_value, steering_value
    speed_value = 0.1
    steering_value = 0.0
    rho_left = 0
    theta_left = 0
    rho_right = 0
    theta_right = 0
    if len(left_lines) == 2:
        rho_left = left_lines[0]
        theta_left = left_lines[1]
        grad_left = theta_left * const
        print("left: " + str([grad_left, theta_left, rho_left]))
    if len(right_lines) == 2:
        rho_right = right_lines[0]
        theta_right = right_lines[1]
        grad_right = theta_right * const
        print("right: " + str([grad_right, theta_right, rho_right]))
    if rho_left != 0 and rho_right != 0:
        e_rho = error_rho(rho_left, rho_right)
        e_theta = error_theta(theta_left, theta_right)
        print("errores: " + str([e_rho, e_theta]))


def callback_left(msg):
    global left_lines
    left_lines = msg.data

def callback_right(msg):
    global right_lines
    right_lines = msg.data

def main():
    global speed_value, steering_value
    print("INITIALIZING LANES CONTROL NODE...")
    rospy.init_node('hardware_control', anonymous=True)
    speed = rospy.Publisher('/speed', Float32, queue_size=10)
    steering = rospy.Publisher('/steering', Float32, queue_size=10)
    rospy.Subscriber("/raw_lanes_left", Floats, callback_left)
    rospy.Subscriber("/raw_lanes_right", Floats, callback_right)
    loop = rospy.Rate(60)
    print("NODE INITIALIZED SUCCESFULLY")
    while not rospy.is_shutdown():
        decide()
        speed.publish(speed_value)
        steering.publish(steering_value)
        loop.sleep()
main()

