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
import time
from std_msgs.msg import Float64MultiArray, Float64, Float32, Bool

stops = 0

#
# Steering is calculated proportional to two errors: distance error and angle error.
# These errors correspond to differences between an observed line (in normal form)
# and a desired line.
# Speed is calculated as the max speed minus a speed proportional to the steering.
# In this way, car goes with lower speed in curves and at max speed in straight roads. 
#
# calculate_control {{{
def calculate_control(rho_l, theta_l, rho_r, theta_r, goal_rho_l, goal_theta_l, goal_rho_r, goal_theta_r):
    global max_speed, k_rho, k_theta
    error_rho_l = 0
    error_theta_l = 0
    error_rho_r = 0
    error_theta_r = 0
    if rho_l == 0 or theta_l == 0:
        pass
    else:
        error_rho_l   = goal_rho_l   - rho_l
        error_theta_l = goal_theta_l - theta_l
    if rho_r == 0 or theta_r == 0:
        pass
    else:
        error_rho_r   = rho_r   - goal_rho_r
        error_theta_r = theta_r - goal_theta_r
    if True: #rho_l != 0 and theta_l != 0 and rho_r != 0 and theta_r != 0
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
        """
    elif rho_r == 0 or theta_r == 0 and rho_l != 0 and theta_l != 0:
        #steering = -0.6
        #speed = max_speed / 2
    elif rho_l == 0 or theta_l == 0 and rho_r != 0 and theta_r != 0:
        #steering = 0.6
        #speed = max_speed / 2
        """
    else:
        steering = 0
        speed = -max_speed / 2
    return speed, steering
# }}}

# callback left lane {{{
def callback_left_lane(msg):
    global lane_rho_l, lane_theta_l
    global sum_rho_l, sum_theta_l, counter_l, auto_calibrate
    lane_rho_l, lane_theta_l = msg.data
    if counter_l > 0 and auto_calibrate:
        sum_rho_l += lane_rho_l
        sum_theta_l += lane_theta_l
        counter_l-=1
# }}}

# callback right lane {{{
def callback_right_lane(msg):
    global lane_rho_r, lane_theta_r
    global sum_rho_r, sum_theta_r, counter_r, auto_calibrate
    lane_rho_r, lane_theta_r = msg.data
    if counter_r > 0 and auto_calibrate:
        sum_rho_r += lane_rho_r
        sum_theta_r += lane_theta_r
        counter_r-=1
# }}}

#
#
# obstacle callback{{{
def callback_obstacle(msg):
    global obstacle
    if msg.data:
        obstacle += 1
#}}}

#
#
# stop callback{{{
def callback_stop(msg):
    global stops
    if msg.data:
        stops += 1
#}}}

# main{{{
def main():
    global lane_rho_l, lane_theta_l, lane_rho_r, lane_theta_r
    global max_speed, k_rho, k_theta
    global goal_rho_l, global_theta_l, global_tho_r, global_theta_r
    global sum_rho_l, sum_theta_l, sum_rho_r, sum_theta_r
    global counter_l, counter_r, COUNTER_L, COUNTER_R, auto_calibrate
    global obstacle, stops, obstacle_number
    print('INITIALIZING LANE TRACKING NODE...')
    rospy.init_node("lane_tracking")
    obstacle_number = 0
    obstacle = False
    sum_rho_l = sum_theta_l = sum_rho_r = sum_theta_r = 0
    auto_calibrate = False
    counter_l = counter_r = 10
    max_speed = 0.25
    k_rho   = 0.0055
    k_theta = 0.04
    lane_rho_l   = 0
    lane_theta_l = 0
    lane_rho_r   = 0
    lane_theta_r = 0
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
    if rospy.has_param('~auto_calibrate'):
        auto_calibrate = rospy.get_param('~auto_calibrate')
        if auto_calibrate == 1:
            auto_calibrate = True
        else:
            auto_calibrate = False
    COUNTER_L = counter_l
    COUNTER_R = counter_r
    print(max_speed)
    goal_rho_l   = 326.8
    goal_theta_l = 2.14
    goal_rho_r   = 241.97
    goal_theta_r = 0.75
    """
    goal_rho_l   = 295.42
    goal_theta_l = 2.08
    goal_rho_r   = 221.98
    goal_theta_r = 0.7
    """
    rospy.init_node('lane_tracking')
    rate = rospy.Rate(30)
    rospy.Subscriber("/demo/left_lane" , Float64MultiArray, callback_left_lane)
    rospy.Subscriber("/demo/right_lane", Float64MultiArray, callback_right_lane)
    rospy.Subscriber("/stop", Bool, callback_stop)
    rospy.Subscriber("/obstacle", Bool, callback_obstacle)
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
        if False:#auto_calibrate:
            #{{{
            if counter_l == 0 or counter_r == 0:
                speed, steering = calculate_control(lane_rho_l, lane_theta_l, lane_rho_r, lane_theta_r, goal_rho_l, goal_theta_l, goal_rho_r, goal_theta_r)
                if stops < 2:
                    pub_speed.publish(speed)
                else:
                    pub_speed.publish(0.0)
                pub_angle.publish(steering)
                rate.sleep()
            elif counter_l == 1:
                goal_theta_l = sum_theta_l / COUNTER_L
                goal_rho_l = sum_rho_l / COUNTER_L
            elif counter_r == 1:
                goal_theta_r = sum_theta_r / COUNTER_R
                goal_rho_r = sum_rho_r / COUNTER_R
            #}}}
        else:
            speed, steering = calculate_control(lane_rho_l, lane_theta_l, lane_rho_r, lane_theta_r, goal_rho_l, goal_theta_l, goal_rho_r, goal_theta_r)
            if obstacle < 2 and stops < 2:
                pub_speed.publish(speed)
                pub_angle.publish(steering)
            elif stops > 2:
                time.sleep(0.5)
                pub_speed.publish(0.0)
                pub_angle.publish(steering)
                time.sleep(2)
                stops = -20
            elif obstacle > 2:
                print(obstacle_number)
                if obstacle_number >= 2:
                    # Salida a la izquierda{{{
                    tiempo = 0.7
                    print("a")
                    for i in range(0, int(tiempo * 10)):
                        pub_angle.publish(2.5)
                        pub_speed.publish(max_speed*0.8)
                        time.sleep(0.1)
                    # }}}
                    # Recompone a la deracha {{{
                    print("b")
                    for i in range(0, int(tiempo * 10)):
                        pub_angle.publish(-2.5)
                        pub_speed.publish(max_speed*0.8)
                        time.sleep(0.1)
                    # }}}
                    obstacle_number = 0
                else:
                    obstacle_number += 1
                    # Salida a la izquierda{{{
                    tiempo = 0.6
                    print("a")
                    for i in range(0, int(tiempo * 10)):
                        pub_angle.publish(2)
                        pub_speed.publish(max_speed)
                        time.sleep(0.1)
                    # }}}
                    # Recompone a la deracha {{{
                    print("b")
                    for i in range(0, int(tiempo * 10)):
                        pub_angle.publish(-2.5)
                        pub_speed.publish(max_speed)
                        time.sleep(0.1)
                    # }}}
                    # Adelanta {{{
                    """
                    print("c")
                    tiempo = 2
                    for i in range(0, int(tiempo * 10)):
                        print(i)
                        speed, steering = calculate_control(lane_rho_l, lane_theta_l, lane_rho_r, lane_theta_r, goal_rho_l, goal_theta_l, goal_rho_r, goal_theta_r)
                        pub_angle.publish(steering)
                        pub_speed.publish(max_speed * 1.2)
                        time.sleep(0.1)
                    """
                    # }}}
                    # Regreso a la derecha{{{
                    tiempo = 1.1
                    print("d")
                    for i in range(0, int(tiempo * 10)):
                        pub_angle.publish(-2)
                        pub_speed.publish(max_speed)
                        time.sleep(0.1)
                    # }}}
                    # Recompone a la izquierda{{{
                    tiempo = 0.7
                    print("e")
                    for i in range(0, int(tiempo * 10)):
                        pub_angle.publish(2.5)
                        pub_speed.publish(max_speed)
                        time.sleep(0.1)
                 # }}}
                    print("regresando el control")
                obstacle = 0
            """
            lane_rho_l = 0
            lane_theta_l = 0
            lane_rho_r = 0
            lane_theta_r = 0
            """
            rate.sleep()
# }}}

if __name__ == "__main__":
    main()

