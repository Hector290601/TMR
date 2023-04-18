#!/usr/bin/env python
import rospy, math
from std_msgs.msg import Float32, Float64, Float64MultiArray
from sensor_msgs.msg import PointCloud2
from sensor_msgs import point_cloud2
from geometry_msgs.msg import Point, Pose

def right_lane_callback(data):
    global right_lane
    right_lane = list(data.data)

def left_lane_callback(data):
    global left_lane
    left_lane = list(data.data)

def parking_lane_callback(data):
    global parking_lane
    parking_lane = list(data.data)
    
def lane_speed_callback(data):
    global lane_speed
    lane_speed = data.data
   
def lane_sterring_callback(data):
    global lane_steering
    lane_steering = data.data

def process_points(points):
    obst_cart = []
    obst_sph  = []
    for point in points:
        x = point[0]
        y = point[1]
        r = math.sqrt(x**2 + y**2)
        theta = math.atan2(y, x)    
        if theta < 0:   
            obst_cart.append([x, y])
            obst_sph.append([r, theta])
    return obst_cart, obst_sph

def main_callback(data):
    global right_lane, left_lane, parking_lane, lane_speed, lane_steering, speed_pub, steering_pub, state
    
    points = list(point_cloud2.read_points(data))
    obst_cart, obst_sph = process_points(points)
    
    if(obst_sph):
        print(parking_lane, right_lane, left_lane, min(obst_sph, key=lambda x: x[0]))

"""    if state == 'searching':
        if obst_sph:
            obst_r_min = min(obst_sph, key=lambda x: x[0])
            if -1.6 < obst_r_min[1] < -1.25:
                obst_sph.remove(obst_r_min) 
                obst_r_min = min(obst_sph, key=lambda x: x[0])
                if obst_r_min[1] < -1.4:
                    state = 'turning'
                    print('Turning car to park...')
            else:
                speed_pub.publish(lane_speed)
                steering_pub.publish(lane_steering)
        else:
            speed_pub.publish(lane_speed)
            steering_pub.publish(lane_steering)
    elif state == 'turning':
        obst_r_min = min(obst_sph, key=lambda x: abs(x[1] - (-1.95)))
        if -2.05 > obst_r_min[1]:
            state = 'parking'
            print('Parking...')
        else:
            steering_pub.publish(0.25)
        speed_pub.publish(0.2)
    elif state == 'parking':
        speed_pub.publish(0.2)
        steering_pub.publish(-0.7)
        obst_r_min = min(obst_sph, key=lambda x: x[0])
        if 1.425 < parking_lane[1] < 1.575 and -1.145 < obst_r_min[1] < -1.125 \
          and right_lane == [0.0, 0.0] and left_lane == [0.0, 0.0]:
            state = 'stopping'
            print('Stopping...')
            print('Succesfully parked')
    elif state == 'stopping':
        speed_pub.publish(0.0)
        steering_pub.publish(0.0)"""

def main():
    global speed_pub, steering_pub, state
    
    print("INITIALIZING PARKING NODE...")
    rospy.init_node('parking')
    
    state = 'searching'
    
    speed_pub = rospy.Publisher('/speed', Float32, queue_size=10)
    steering_pub = rospy.Publisher('/steering', Float64, queue_size=10)
    
    rospy.wait_for_message('/right_lane', Float64MultiArray)
    rospy.wait_for_message('/left_lane', Float64MultiArray)
    rospy.wait_for_message('/parking_lane', Float64MultiArray)
    rospy.wait_for_message('/lane_speed', Float32)
    rospy.wait_for_message('/lane_steering', Float64)
    rospy.wait_for_message('/obstacle_centroids', PointCloud2)
    
    rospy.Subscriber('/right_lane', Float64MultiArray, right_lane_callback)    
    rospy.Subscriber('/left_lane', Float64MultiArray, left_lane_callback)    
    rospy.Subscriber('/parking_lane', Float64MultiArray, parking_lane_callback)
    rospy.Subscriber('/lane_speed', Float32, lane_speed_callback)
    rospy.Subscriber('/lane_steering', Float64, lane_steering_callback)   
    rospy.Subscriber('/obstacle_centroids', PointCloud2, main_callback)
    
    print('Searching for parking place...')
    
    rospy.spin()

if __name__ == "__main__":
    try:
        main()
    except:
        rospy.ROSInterruptException
        pass
