#!/usr/bin/env python
"""
This node implements a proportional control and is intended to be used
together with the lane_detector node. It is assumed both lane borders 
are given by two straight lines in rho-theta form. Given a desired rho-theta
for each lane border, an error is calculated.
Steering is calculated proportional to this error and linear speed is
set as a constant. 
"""
import cv2
import numpy
import rospy
from std_msgs.msg import Float64MultiArray, Float64, Float32

#
# Steering is calculated proportional to two errors: distance error and angle error.
# These errors correspond to differences between an observed line (in normal form)
# and a desired line.
# Speed is calculated as the max speed minus a speed proportional to the steering.
# In this way, car goes with lower speed in curves and at max speed in straight roads. 
#
def calculate_control(rho_l, theta_l, rho_r, theta_r, goal_rho_l, goal_theta_l, goal_rho_r, goal_theta_r):
    global max_speed, k_rho, k_theta
    error_rho_l   = goal_rho_l   - rho_l
    error_theta_l = goal_theta_l - theta_l
    error_rho_r   = rho_r   - goal_rho_r
    error_theta_r = theta_r - goal_theta_r
    if rho_l != 0 and rho_r != 0:
        error_rho   = (error_rho_l + error_rho_r)/2
        error_theta = (error_theta_l + error_theta_r)/2
    elif rho_l != 0:
        error_rho   = error_rho_l
        error_theta = error_theta_l
    else:
        error_rho   = error_rho_r
        error_theta = error_theta_r
    
    steering = -k_rho*error_rho - k_theta*error_theta
    speed = max_speed#*(1 - 1.5*abs(steering))
    return speed, steering

def callback_left_lane(msg):
    global lane_rho_l, lane_theta_l
    global sum_rho_l, sum_theta_l, counter_l
    lane_rho_l, lane_theta_l = msg.data
    if counter_l > 0:
        sum_rho_l += lane_rho_l
        sum_theta_l += lane_theta_l
        counter_l-=1
        print('tunning l @ ' + str(counter_l))

def callback_right_lane(msg):
    global lane_rho_r, lane_theta_r
    global sum_rho_r, sum_theta_r, counter_r
    lane_rho_r, lane_theta_r = msg.data
    if counter_r > 0:
        sum_rho_r += lane_rho_r
        sum_theta_r += lane_theta_r
        counter_r-=1
        print('tunning r @ ' + str(counter_r))

def main():
    global lane_rho_l, lane_theta_l, lane_rho_r, lane_theta_r
    global max_speed, k_rho, k_theta
    global goal_rho_l, global_theta_l, global_tho_r, global_theta_r
    global sum_rho_l, sum_theta_l, sum_rho_r, sum_theta_r
    global counter_l, counter_r, COUNTER_L, COUNTER_R
    sum_rho_l = sum_theta_l = sum_rho_r = sum_theta_r = 0
    counter_l = counter_r = 10
    max_speed = 0.13
    k_rho   = 0.001
    k_theta = 0.01
    lane_rho_l   = 0
    lane_theta_l = 0
    lane_rho_r   = 0
    lane_theta_r = 0
    goal_rho_l   = 186.0
    goal_theta_l = 2.26
    goal_rho_r   = 200.0
    goal_theta_r = 0.77
    print('INITIALIZING LANE TRACKING NODE...')
    rospy.init_node('lane_tracking')
    rate = rospy.Rate(30)
    if rospy.has_param('~max_speed'):
        max_speed = rospy.get_param('~max_speed')
    if rospy.has_param('~k_rho'):
        k_rho = rospy.get_param('~k_rho')
    if rospy.has_param('~k_theta'):
        k_theta = rospy.get_param('~k_theta')
    if rospy.has_param('~counter_l'):
        counter_l = rospy.get_param('~counter_l')
    if rospy.has_param('~counter_r'):
        counter_l = rospy.get_param('~counter_r')
    COUNTER_L = counter_l
    COUNTER_R = counter_r
    rospy.Subscriber("/demo/left_lane" , Float64MultiArray, callback_left_lane)
    rospy.Subscriber("/demo/right_lane", Float64MultiArray, callback_right_lane)
    pub_speed = rospy.Publisher('/speed', Float32, queue_size=10)
    pub_angle = rospy.Publisher('/steering', Float64, queue_size=10)
    print("Waiting for lane detection...")
    msg_left_lane  = rospy.wait_for_message('/demo/left_lane' , Float64MultiArray, timeout=100)
    msg_right_lane = rospy.wait_for_message('/demo/right_lane', Float64MultiArray, timeout=100)
    print("Using:")
    print("Max speed: " + str(max_speed))
    print("K_rho: " + str(k_rho))
    print("K_theta: " + str(k_theta))
    while not rospy.is_shutdown():
        if counter_l == 0 or counter_r == 0:
            speed, steering = calculate_control(lane_rho_l, lane_theta_l, lane_rho_r, lane_theta_r, goal_rho_l, goal_theta_l, goal_rho_r, goal_theta_r)
            pub_speed.publish(speed)
            pub_angle.publish(steering)
            rate.sleep()
        elif counter_l == 1:
            goal_theta_l = sum_theta_l / COUNTER_L
            goal_rho_l = sum_rho_l / COUNTER_L
            print('Tunned l @ ({},{})'.format(goal_theta_l, goal_rho_l))
        elif counter_r == 1:
            goal_theta_r = sum_theta_r / COUNTER_R
            goal_rho_r = sum_rho_r / COUNTER_R
            print('Tunned r @ ({},{})'.format(goal_theta_r, goal_rho_r))
    

if __name__ == "__main__":
    main()

    

