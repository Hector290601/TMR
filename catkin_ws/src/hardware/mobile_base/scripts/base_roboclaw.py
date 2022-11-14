#!/usr/bin/env python
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import math
import cv2
import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan, Image
from cv_bridge import CvBridge
from roboclaw import Roboclaw

steering = 0
speed = 0
rbc = None

def AngleToDuty(speed, steering):
    return speed, steering

def callback_steering(msg):
    global steering
    steering = msg.data #Steering in radians

def callback_speed(msg):
    global speed
    speed = int(msg.data) #Speed in percentage
    if speed > 127:
        speed = 127
    elif speed < 0:
        speed = 0

def main():
    global steering, speed
    print("INITIALIZING HARDWARE CONTROL NODE...")
    rospy.init_node("mobile_base")
    img_publisher = rospy.Publisher("/raw_image", Image, queue_size=10)
    rospy.Subscriber("/steering", Float32, callback_steering)
    rospy.Subscriber("/speed", Float32, callback_speed)
    loop = rospy.Rate(60)
    steering = 0
    speed = 0
    cap = cv2.VideoCapture(0)
    brdg = CvBridge()
    main_motor = Roboclaw("/dev/ttyACM0", 115200)
    if main_motor.Open() == 0:
        return False
    print("ALL SUCCESFULLY INITIALIZED")
    dutySpeed, dutySteering=AngleToDuty(8.5, 0)
    dutySpeed, dutySteering=AngleToDuty(0, 0)
    while not rospy.is_shutdown():
        dutySpeed, dutySteering=AngleToDuty(speed, steering)
        main_motor.ForwardM1(0x80, speed)
        ret, frame = cap.read()
        if ret == True:
            img_publisher.publish(brdg.cv2_to_imgmsg(frame))
        loop.sleep()
    servo.stop()
    motor.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    main()

