#!/usr/bin/env python
import rospy
import numpy as np
from sensor_msgs.msg import PointCloud2
from std_msgs.msg import Bool
from sensor_msgs import point_cloud2


def callback_cloud(data):
    assert isinstance(data, PointCloud2)
    gen=point_cloud2.read_points(data,field_names=("x","y","z"),skip_nans=True)  
    #print type(gen)
    noTope=True
    voto=0
    #><
    for p in gen:
        if -3<p[0]<3 and -1.5<p[1]<0.5 and -20<p[2]<-2:
	    voto +=1
    noTope=voto<40
    print(("Todo libre" if noTope else "Estorba"))
    """if voto> 40:
            print("Estorba")
            noTope=True
	else:
	   noTope=False
	   print("Todo libre")
            
	#print "x : %.3f y:%.3f z:%.3f" %(p[0],p[1],p[2])
        #print(msg.width)
	#arr = ros_numpy.point_cloud2.pointcloud2_to_array(msg)
    """

def main():
    print("Initializing node.....")
    rospy.init_node ('software_obstacle_detector',anonymous=True)
    rospy.Subscriber("/point_cloud", PointCloud2, callback_cloud)
    print("Nodo exitosoooo!!.....")
    rospy.spin()

main()

