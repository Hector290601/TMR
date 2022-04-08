#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback_Laser2(msg):
    #si la distancia a un obstaculo en frente es mayor de 1 metro, el robot se mueve enfrente
    if msg.ranges[0]>1:
        move.linear.x = 0.5
        move.angular.z =0.0

     #si la distancia es mnor a 1 metro, te paras
    print "No. of Ranges", len (msg.ranges)
    print "Reading at position 0:", msg.ranges [0]

    if msg.ranges[0]<1:
	move.linear.x = 0.0
	move.angular.z = 0.0
    pub.publish(move)

def listener():

    rospy.init_node ('software_obstacle_detector', anonymous=True)
    rospy.Subscriber("/scan", LaserScan, callback_Laser2)
    pub = rospy.Publisher ('/cmd_vel', Twist)
    rospy.spin()
def main():
    listener()
    print("Initializing node.....")

main()
