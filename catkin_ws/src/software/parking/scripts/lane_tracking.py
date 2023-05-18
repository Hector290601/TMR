#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32, Float64, Float64MultiArray

def calculate_control():
    global max_speed, k_rho, k_theta, target_rho_l, target_theta_l, target_rho_r, target_theta_r, left_lane, right_lane

    if left_lane[0] == 0 or left_lane[1] == 0:
        return [max_speed, 0.0]

    if right_lane[0] == 0 or right_lane[1] == 0:
        return [max_speed, 0.0]

    error_rho_l   = target_rho_l   - left_lane[0]
    error_theta_l = target_theta_l - left_lane[1]
    error_rho_r   = right_lane[0]   - target_rho_r
    error_theta_r = right_lane[1] - target_theta_r

    error_rho   = (error_rho_l + error_rho_r) / 2
    error_theta = (error_theta_l + error_theta_r) / 2

    steering = -k_rho*error_rho - k_theta*error_theta
    speed = max_speed

    return speed, steering

def callback_left_lane(msg):
    global left_lane
    left_lane = list(msg.data)

def callback_right_lane(msg):
    global right_lane
    right_lane = list(msg.data)
    speed, steering = calculate_control()
    pub_steering.publish(steering)
    pub_speed.publish(speed)

if __name__ == '__main__':
    global max_speed, k_rho, k_theta, target_rho_l, target_rho_r, target_theta_l, target_theta_r

    left_lane = [0, 0]
    right_lane = [0, 0]    
    max_speed = 0.2
    k_rho = 0.005
    k_theta = 0.04
    target_rho_l   = 312.67
    target_theta_l = 2.12
    target_rho_r   = 175.22
    target_theta_r = 0.64
    
    rospy.init_node("lane_tracking")
    pub_speed = rospy.Publisher('/lane_speed', Float32, queue_size=10)
    pub_steering = rospy.Publisher('/lane_steering', Float64, queue_size=10)
    rospy.wait_for_message('/right_lane', Float64MultiArray)
    rospy.wait_for_message('/left_lane', Float64MultiArray)
    rospy.Subscriber("/left_lane", Float64MultiArray, callback_left_lane)
    rospy.Subscriber("/right_lane", Float64MultiArray, callback_right_lane)
    rospy.spin()
