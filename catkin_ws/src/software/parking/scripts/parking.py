#!/usr/bin/env python
import rospy, math 
from std_msgs.msg import Float32, Float64, Float64MultiArray 
from geometry_msgs.msg import PointStamped

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
   
def lane_steering_callback(data):
    global lane_steering
    lane_steering = data.data

def main_callback(data):
    global right_lane, left_lane, parking_lane, lane_speed, lane_steering, speed_pub, steering_pub, state
    centroid_x = data.point.x
    centroid_y = data.point.y
    if state == 'searching_park':
        if 0.0 < centroid_x < 0.25 and centroid_y != 0.0:
            print('Searching space to park')
            state = 'searching_space'
            speed_pub.publish(lane_speed)
            steering_pub.publish(lane_steering)
        else:
            speed_pub.publish(lane_speed)
            steering_pub.publish(lane_steering)
    elif state == 'searching_space':
        if centroid_x == 0 and centroid_y == 0:
            print('Space found')
            state = 'parking'
            start = rospy.get_time()
            rate = rospy.Rate(10)
            while rospy.get_time() - start < 3:
                speed_pub.publish(lane_speed*1.2)
                steering_pub.publish(2.5)
                rate.sleep()
            speed_pub.publish(0.0)
            steering_pub.publish(0.0)
        else:
            speed_pub.publish(lane_speed)
            steering_pub.publish(lane_steering)
    elif state == 'parking':
        start = rospy.get_time()
        rate = rospy.Rate(10)
        while rospy.get_time() - start < 2.9:
            speed_pub.publish(-lane_speed)
            steering_pub.publish(-1.5)
            rate.sleep()
        speed_pub.publish(0.0)        	
        steering_pub.publish(0.0)
        print('Parked')
        state = 'parked'

def main():
    global speed_pub, steering_pub, state, lane_speed, lane_steering

    lane_speed = 0.0
    lane_steering = 0.0

    print("INITIALIZING PARKING NODE...")
    rospy.init_node('parking')
    
    state = 'searching_park'
    
    speed_pub = rospy.Publisher('/speed', Float32, queue_size=10)
    steering_pub = rospy.Publisher('/steering', Float64, queue_size=10)
    
    rospy.wait_for_message('/right_lane', Float64MultiArray)
    rospy.wait_for_message('/left_lane', Float64MultiArray)
    rospy.wait_for_message('/parking_lane', Float64MultiArray)
    rospy.wait_for_message('/lane_speed', Float32)
    rospy.wait_for_message('/lane_steering', Float64)
    rospy.wait_for_message('/obstacles', PointStamped)
    
    rospy.Subscriber('/right_lane', Float64MultiArray, right_lane_callback)    
    rospy.Subscriber('/left_lane', Float64MultiArray, left_lane_callback)    
    rospy.Subscriber('/parking_lane', Float64MultiArray, parking_lane_callback)
    rospy.Subscriber('/lane_speed', Float32, lane_speed_callback)
    rospy.Subscriber('/lane_steering', Float64, lane_steering_callback)   
    rospy.Subscriber('/obstacles', PointStamped, main_callback)
    
    print('Searching for parking place...')
    
    rospy.spin()

if __name__ == "__main__":
    global speed_pub
    try:
        main()
    except rospy.ROSInterruptException:
        speed_pub.publish(0.0)
