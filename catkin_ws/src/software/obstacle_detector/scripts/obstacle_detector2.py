#!/usr/bin/env python
import rospy
import numpy as np
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

   
    #interes=np.array(data.ranges[left:right]).astype(int) #recorta solo el interes, convierte arreglo a entero     
    
    #interes = str(interes)[1:-1]#quitar losparentesis 
    
    
   
    #voto= interes.find("0")
    voto= 0
    for i in data.ranges[left:right]: 
        if i < 1:
            voto +=1

    if voto > 40:
        print("Estorba")
        noTope=True
    else:
        noTope=False
        print("Todo libre")
    #print(interes.find("0 0 0"))
    #print(voto)
    #print(interes)


def listener():
    rospy.init_node ('software_obstacle_detector', anonymous=True)
    rospy.Subscriber("/scan", LaserScan, callback_Laser2)
    rospy.spin()

def main():
    print("Initializing node.....")
    listener()

main()
