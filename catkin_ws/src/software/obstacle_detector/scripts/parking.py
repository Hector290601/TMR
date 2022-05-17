#!/usr/bin/env python
import rospy
import numpy as np
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import Bool
import ros_numpy
import os
import math

def callback_cloud(msg):
    arr = ros_numpy.point_cloud2.pointcloud2_to_array(msg)
    x_pos = 0
    y_pos = 0
    z_pos = 0
    n_pos = 0
    for i  in range(0, len(arr), 20):
        point = arr[i]
        x = point[0]
        y = point[1]
        z = point[2]
        if 0.0 < x < 4.0 and -2.0 < z < 2.0 and -1.5 < y < 0.5:
            n_pos += 1
            x_pos += x
            y_pos += y
            z_pos += z
    if n_pos > 0:
        x_pos /= n_pos
        y_pos /= n_pos
        z_pos /= n_pos
    print([x_pos, y_pos, z_pos])

def main():
    print("Initializing node.....")
    rospy.init_node ('software_obstacle_detector',anonymous=True)
    rospy.Subscriber("/point_cloud", PointCloud2, callback_cloud)
    print("Nodo exitosoooo!!.....")
    rospy.spin()

main()

