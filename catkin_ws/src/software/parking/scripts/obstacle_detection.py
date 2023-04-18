#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import Header
from geometry_msgs.msg import PointStamped
from sensor_msgs.msg import LaserScan

def callback(laser_scan):
    xy = np.array([[0.0, 0.0] for i in range(len(laser_scan.ranges))])
    ranges = np.array(laser_scan.ranges)
    angles = np.linspace(laser_scan.angle_min, laser_scan.angle_max, len(ranges))
    xy[:,0] = ranges*np.cos(angles)
    xy[:,1] =  ranges*np.sin(angles)
    xy = xy[np.logical_not(np.isnan(xy[:,0]))]
    xy = xy[(xy[:,0]>-0.15) & (xy[:,0]<0.34) & (xy[:,1]>-0.6) & (xy[:,1]<-0.2)]
    if len(xy) < 25:
        publish_point_cloud(0, 0)
    else:
        centroid = np.mean(xy, axis=0)
        publish_point_cloud(centroid[0], centroid[1])

def publish_point_cloud(x, y):
    global point_cloud_publisher
    header = Header()
    header.stamp = rospy.Time.now()
    header.frame_id = 'laser'
    p = PointStamped()
    p.header = header
    p.point.x = x
    p.point.y = y
    point_cloud_publisher.publish(p)

def main():
    global point_cloud_publisher
    print("INITIALIZING OBSTACLE DETECTION NODE...")
    rospy.init_node('obstacle_detection')
    point_cloud_publisher = rospy.Publisher('/obstacles', PointStamped, queue_size=10)
    rospy.wait_for_message('/scan', LaserScan)
    rospy.Subscriber('/scan', LaserScan, callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except:
        rospy.ROSInterruptException
        pass
