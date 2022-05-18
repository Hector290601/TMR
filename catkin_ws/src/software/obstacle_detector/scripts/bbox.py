#!/usr/bin/env python
import rospy
import numpy as np
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import Bool
import ros_numpy
import os
import math

flag = 0
last = 0
delta = 0
count = 0
pub = 0

def bounding_box(
        x_max, x_min,
        y_max, y_min,
        z_max, z_min,
        data, steps = 20
        ):
    grad_x = grad_y = grad_z = 0
    n = 0
    for i in range(0, len(data), steps):
        x, y, z = data[i]
        if x_min < x < x_max and y_min < y < y_max and z_min < z < z_max:
            grad_x += x
            grad_y += y
            grad_z += z
            n += 1
    if n > 0:
        grad_x /= n
        grad_y /= n
        grad_z /= n
    else:
        grad_x = 0
        grad_y = 0
        grad_z = 0
    return grad_x, grad_y, grad_z

def callback_cloud(msg):
    global flag, delta, last, count, pub
    arr = ros_numpy.point_cloud2.pointcloud2_to_array(msg)
    x_pos = 0
    y_pos = 0
    z_pos = 0
    n_pos = 0
    x_pos, y_pos, z_pos = bounding_box(
            1.5, -1.5,
            -1.5, -1.7,
            -1.5, -30,
            arr
            )
    print(z_pos)
    distance = -20.0
    if distance < z_pos < 0:
        pub.publish(True)
    else:
        pub.publish(False)

def main():
    global pub
    print("Initializing node.....")
    rospy.init_node ('software_obstacle_detector',anonymous=True)
    rospy.Subscriber("/point_cloud", PointCloud2, callback_cloud)
    pub = rospy.Publisher("/obstacle_flag", Bool, queue_size=10)
    loop = rospy.Rate(60)
    print("Nodo exitosoooo!!.....")
    while not rospy.is_shutdown():
        loop.sleep
    rospy.spin()

main()

