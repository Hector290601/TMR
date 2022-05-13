#!/usr/bin/env python
import rospy
import numpy as np
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import Bool
import ros_numpy

def callback_cloud(msg):
    print(msg.width)
    #arr = ros_numpy.point_cloud2.pointcloud2_to_array(msg)
    #print(arr[10000])

def main():
    print("Initializing node.....")
    rospy.init_node ('software_obstacle_detector',anonymous=True)
    rospy.Subscriber("/point_cloud", PointCloud2, callback_cloud)
    print("Nodo exitosoooo!!.....")
    rospy.spin()

main()

