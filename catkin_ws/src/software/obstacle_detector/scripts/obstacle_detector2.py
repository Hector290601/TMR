#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan

def callback_Laser2(data):
    longitud= len(data.ranges)/2
    #print(longitud)#363
    #hayamos la mitad del arreglo
    #ahora calculamos y casteamos par aobtener el numero de lecturas de 363 hacia los lados
    lecturas= int(0.5/data.angle_increment)#81
    #print(lecturas)
    left= longitud-lecturas
    right=longitud+lecturas
    #print(left)#282
    #print(right)#444
    noTope=True
    #while noTope:
    for i in range(left,right,lecturas):#start,stop,step
        if data.ranges[i]>1:
            noTope=False
            
        else:
            print(data.ranges[i])

def listener():
    rospy.init_node ('software_obstacle_detector', anonymous=True)
    rospy.Subscriber("/scan", LaserScan, callback_Laser2)
    rospy.spin()

def main():
    print("Initializing node.....")
    listener()

main()
