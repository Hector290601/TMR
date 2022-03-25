#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Float32
from rospy.numpy_msg import numpy_msg
from rospy_tutorials.msg import Floats
import math
from datetime import datetime
now = datetime.now()
filename = now.strftime("%d-%m-%Y-%H-%M-%S") + ".csv"
left_lines = ""
right_lines = ""
const = 180/math.pi
steering_value = Float32(0)
speed_value = Float32(0)

def error_rho(rho_left = 343.5, rho_right = 172.130432128906,):
    e = ( 1/2 * (343.5 - rho_left) ) + ( 1/2 * (172.130432128906 - rho_right) )
    return round(e, 3)

def error_theta(theta_left = 1.33517694473267, theta_right = 1.82576608657837):
    e = ( 1/2 * (1.32712506916856 - theta_left) ) + ( 1/2 * (1.82540516519209 - theta_right) )
    return round(e, 3)

def save_data(filename, data):
    """
    data tiene que ser algo como:
    data = [
            left_lines_rho,
            left_lines_theta,
            right_lines_rho,
            right_lines_theta,
            e_rho,
            e_theta,
            sentido,
            strng,
            spd
            ]
    Ejemplo:
    [
        366.70001220703125,
        1.3255774974822998,
        208.63636779785156,
        1.8222824335098267,
        0.4289279584376855,
        -0.02798258780041906,
        C,
        0.4155103862285614,
        9.5
        ]

    para el sentido, así se dividen:
      c: centro
      l: izquierda
      r: derecha
    """
    with open(filename, 'a') as f:
        for d in data:
            f.write(str(d) + ",")
        f.write("\n")
        f.close()

def decide():
    global left_lines, right_lines, const, speed_value, steering_value, filename
    spd_tmp = 9
    speed_value = 0.2
    steering_value = 0.0
    rho_left = 0
    theta_left = 0
    rho_right = 0
    theta_right = 0
    data = []
    sentido = ""
    if len(left_lines) == 2:
        rho_left = left_lines[0]
        theta_left = left_lines[1]
        grad_left = theta_left * const
    if len(right_lines) == 2:
        rho_right = right_lines[0]
        theta_right = right_lines[1]
        grad_right = theta_right * const
    if rho_left != 0 and rho_right != 0:
        e_rho = error_rho(rho_left, rho_right) * 0.1
        e_theta = error_theta(theta_left, theta_right)
        strng = -( e_rho + (e_theta -0.010685840594791) ) * 12
        if strng >= .44:
            strng = .44
        elif strng <= -.44:
            strng = -.44
        spd = spd_tmp
        sentido = "C"
    elif rho_left != 0:
        e_rho = error_rho(rho_left) * 0.00072
        e_theta = error_theta(theta_left)
        strng = -( e_rho + e_theta -0.010685840594791) * 5
        if strng >= .44:
            strng = .44
        elif strng <= -.44:
            strng = -.44
        spd = spd_tmp
        sentido = "L"
    elif rho_right != 0:
        e_rho = error_rho(rho_right = rho_right) * 0.00072
        e_theta = error_theta(theta_left = theta_right)
        strng = -( e_rho + e_theta -0.010685840594791) * 5
        if strng >= .44:
            strng = .44
        elif strng <= -.44:
            strng = -.44
        spd = spd_tmp
        sentido = "R"
    else:
        e_rho = 0
        e_theta = 0
        strng = 0
        spd = spd_tmp
    if len(left_lines) == 2 and len(right_lines) == 2:
        data = [
                left_lines[0],
                left_lines[1],
                right_lines[0],
                right_lines[1],
                e_rho,
                e_theta,
                sentido,
                strng,
                spd
                ]
    save_data(filename, data)
    return spd, strng


def callback_left(msg):
    global left_lines
    left_lines = msg.data

def callback_right(msg):
    global right_lines
    right_lines = msg.data

def main():
    global speed_value, steering_value, filename
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

