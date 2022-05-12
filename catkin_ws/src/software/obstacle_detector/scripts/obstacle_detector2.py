#!/usr/bin/env python
import rospy
import numpy as np
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import Bool
import ros_numpy

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

#noTope.publish(bandera)

"""def listener():
    rospy.init_node ('software_obstacle_detector', anonymous=True)
    rospy.Subscriber("/scan", LaserScan, callback_Laser2)
    rospy.spin()"
"def talker():
    pub =rospy.Publisher("hola",LaserScan, queue_size=10)
    rospy.init_node('talker',anonymous=True)
    while not rospy.is_shutdown():
       pub.publish()
"""

def callback_cloud(msg):
    # print(msg.width)
    arr = ros_numpy.point_cloud2.pointcloud2_to_array(msg)
    print(arr[10000])
    
def main():
    global noTopePub
    print("Initializing node.....")
    rospy.init_node ('software_obstacle_detector',anonymous=True)
    #rospy.Suscriber("/point_cloud", LaserScan, callback_Laser2)
    rospy.Subscriber("/point_cloud", PointCloud2, callback_cloud)
    noTopePub = rospy.Publisher("/obstacle_detected",Bool,queue_size=10)
    print("Nodo exitosoooo!!.....")
    rospy.spin()

main()
