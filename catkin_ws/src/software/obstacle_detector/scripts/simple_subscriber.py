#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool
import numpy

def callback_scan(msg):
    global obstacle
    #print(dir(msg))
    #print(type(msg.ranges))
    #print(msg.ranges)
    ranges = msg.ranges
    center = len(msg.ranges) // 2
    ranges = ranges[center-20 : center + 20]
    print(ranges)
    #print(ranges)
    #obstacle = len(ranges[(ranges > 0.2) & (ranges < 0.65)])
    #obstacle = obstacle > 15

def main():
    global obstacle
    obstacle = False
    rospy.init_node('scan_sub', anonymous=True)
    rospy.Subscriber('/scan', LaserScan, callback_scan)
    pub_obstacle = rospy.Publisher("/obstacle", Bool, queue_size=10)
    loop = rospy.Rate(10)
    while not rospy.is_shutdown():
        loop.sleep()
        pub_obstacle.publish(obstacle)

if __name__ == '__main__':
    main()
