#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import math
import cv2
import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import LaserScan, Image
from cv_bridge import CvBridge

steering = 0
speed = 0

def AngleToDuty(speed, steering):
    dutySteering = 6.0 * steering / math.pi + 2.5
    dutySpeed = speed + 9
    return dutySpeed, dutySteering

def callback_steering(msg):
    global steering
    steering = msg.data #Steering in radians

def callback_speed(msg):
    global speed
    speed = msg.data

def callback_lidar(msg):
    print("ranges: " + str(msg.ranges))
    print("intensities: " + str(msg.intensities))

def main():
    global steering, speed
    print("INITIALIZING HARDWARE CONTROL NODE...")
    rospy.init_node("mobile_base")
    img_publisher = rospy.Publisher("/raw_image", Image, queue_size=10)
    rospy.Subscriber("/steering", Float32, callback_steering)
    rospy.Subscriber("/speed", Float32, callback_speed)
    rospy.Subscriber("/scan", LaserScan, callback_lidar)
    loop = rospy.Rate(10)
    servoPin = 12
    motorPin = 16
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPin,GPIO.OUT)
    GPIO.setup(motorPin,GPIO.OUT)
    steering = 0
    speed = 0
    servo = GPIO.PWM(servoPin, 50)
    servo.start(2.5)
    motor = GPIO.PWM(motorPin, 60.2)
    motor.start(9)
    cap = cv2.VideoCapture(0)
    brdg = CvBridge()
    print("ALL SUCCESFULLY INITIALIZED")
    while not rospy.is_shutdown():
        dutySpeed, dutySteering=AngleToDuty(speed, steering)
        servo.ChangeDutyCycle(dutySteering)
        motor.ChangeDutyCycle(dutySpeed)
        ret, frame = cap.read()
        if ret == True:
            img_publisher.publish(brdg.cv2_to_imgmsg(frame))
        loop.sleep() 
    servo.stop()
    motor.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    main()

