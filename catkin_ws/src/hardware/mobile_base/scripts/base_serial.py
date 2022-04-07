#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import time
import serial
import math
import cv2
import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan, Image
from cv_bridge import CvBridge

steering = 0
speed = 0
last_speed = 0
last_steering = 0
flag_speed = False
flag_steering = False

def AngleToDuty(speed = last_speed, steering = last_steering): 
    dutySteering = int(steering)
    dutySpeed = int(speed)
    return dutySpeed, dutySteering

def callback_steering(msg):
    global steering, flag_steering
    steering = msg.data #Steering in radians
    flag_steering = True

def callback_speed(msg):
    global speed, flag_speed
    speed = msg.data #Speed in PWM
    flag_speed = True

def main():
    global steering, speed, flag_speed, flag_steering
    print("INITIALIZING HARDWARE CONTROL NODE...")
    arduino = serial.Serial("/dev/ttyACM0", 115200)
    time.sleep(1)
    rospy.init_node("mobile_base")
    img_publisher = rospy.Publisher("/raw_image", Image, queue_size=10)
    rospy.Subscriber("/steering", Float32, callback_steering)
    rospy.Subscriber("/speed", Float32, callback_speed)
    loop = rospy.Rate(60)
    steering = 0
    speed = 0
    cap = cv2.VideoCapture(0)
    brdg = CvBridge()
    print("ALL SUCCESFULLY INITIALIZED")
    while not rospy.is_shutdown():
        if flag_speed or flag_steering:
            dutySpeed, dutySteering=AngleToDuty(speed, steering)
            arduino.write(bytes([dutySpeed, dutySteering]))
            flag_speed = False
            flag_steering = False
        ret, frame = cap.read()
        if ret == True:
            img_publisher.publish(brdg.cv2_to_imgmsg(frame))
        loop.sleep()

if __name__ == '__main__':
    main()

