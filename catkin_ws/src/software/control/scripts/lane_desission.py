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
    e = ( 1/2 * (370 - rho_left) ) + ( 1/2 * (200 - rho_right) )
    return e

def error_theta(theta_left, theta_right):
    e = ( 1/2 * (1.33 - theta_left) ) + ( 1/2 * (1.9 - theta_right) )
    return e

def decide():
    global left_lines, right_lines, const, speed_value, steering_value
    spd_tmp = 9.0
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
    if len(right_lines) == 2:
        rho_right = right_lines[0]
        theta_right = right_lines[1]
        grad_right = theta_right * const
    if rho_left != 0 and rho_right != 0:
        e_rho = ( 2.17737162539248 - error_rho(rho_left, rho_right) ) * 0.1
        e_theta = ( 0.006019229902828 - error_theta(theta_left, theta_right) )
        print(str(e_rho) + ", " + str(e_theta))
        with open("values.csv", 'a') as f:
            f.write(str(e_rho) + ", " + str(e_theta) + "\n")
            f.close()
        strng = (- ( e_rho + e_theta )) % .44
        print("steering: " + str(strng))
        spd = spd_tmp + .1
    elif rho_left != 0:
        e_rho = ( 2.17737162539248 - error_rho(rho_left, rho_left) ) * 0.1
        e_theta = ( 0.006019229902828 - error_theta(theta_left, theta_left) )
        print(str(e_rho) + ", " + str(e_theta))
        with open("values.csv", 'a') as f:
            f.write(str(e_rho) + ", " + str(e_theta) + "n")
            f.close()
        strng = -( (( e_rho + e_theta ) * .1) % .44)
        print("steering l: " + str(strng))
        spd = spd_tmp
    elif rho_right != 0:
        e_rho = ( 2.17737162539248 - error_rho(rho_right, rho_right) ) * 0.1
        e_theta = ( 0.006019229902828 - error_theta(theta_right, theta_right) )
        print(str(e_rho) + ", " + str(e_theta))
        with open("values.csv", 'a') as f:
            f.write(str(e_rho) + ", " + str(e_theta) + "n")
            f.close()
        strng = -( ( ( e_rho + e_theta )  * .1) % .44)
        print("steering r: " + str(strng))
        spd = spd_tmp
    else:
        strng = 0
        spd = spd_tmp
    return spd, strng


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
        speed_value, steering_value = decide()
        speed.publish(speed_value)
        steering.publish(steering_value)
        loop.sleep()
    speed.publish(0.0)
    steering.publish(0.0)

main()

