#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan 
def callback_Laser(data):
    print((data.ranges ))
    #rospy.loginfo(rospy.get_caller_id() + "ranges:", .data)     
def listener():
     rospy.init_node('software_obstacle_detector', anonymous=True) 
     rospy.Subscriber("/scan", LaserScan, callback_Laser)
     # spin() simply keeps python from exiting until this node is stopped
     rospy.spin() 
def main():
    listener()
    print ("INITIALIZING NODE...........")
    
main()

