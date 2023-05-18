#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from std_msgs.msg import Bool
import matplotlib.pyplot as plt
import numpy as np

def callback_scan(msg):
    global obstacle
    xy = np.array([[0.0, 0.0] for i in range(len(msg.ranges))])
    ranges = np.array(msg.ranges)
    angles = np.linspace(msg.angle_min, msg.angle_max, len(ranges))
    xy[:,0] = ranges*np.cos(angles)
    xy[:,1] =  ranges*np.sin(angles)
    xy = xy[(xy[:,0]>0.2) & (xy[:,0]<1.2) & (xy[:,1]>-0.4) & (xy[:,1]<0.4)]
    #plt.plot(xy[:,0], xy[:, 1])
    #plt.show()
    """
    print(len(xy))
    counter = 0
    for point in xy:
        if point[0] > 0.2 and point[0] < 0.1:
            counter += 1
    #print(counter)
    """
    obstacle = len(xy) > 10

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
