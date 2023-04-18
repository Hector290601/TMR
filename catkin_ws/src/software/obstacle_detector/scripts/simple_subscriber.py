#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool
import numpy

def callback_scan(msg):
    global obstacle
    ranges = numpy.array(msg.ranges)
    center = len(msg.ranges) // 2
    ranges = ranges[234:400]
    obstacle = len(ranges[(ranges > 0.2) & (ranges < 0.65)])
    print(obstacle)
    obstacle = obstacle > 20

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
