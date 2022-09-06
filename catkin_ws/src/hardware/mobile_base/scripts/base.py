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
from roboclaw_3 import Roboclaw

steering = 0
speed = 0
rbc = None

def AngleToDuty(speed, steering):
    return dutySpeed, dutySteering

def callback_steering(msg):
    global steering
    steering = msg.data #Steering in radians

def callback_speed(msg):
    global speed
    speed = msg.data #Speed in PWM

def main():
    global steering, speed
    print("INITIALIZING HARDWARE CONTROL NODE...")
    rospy.init_node("mobile_base")
    img_publisher = rospy.Publisher("/raw_image", Image, queue_size=10)
    rospy.Subscriber("/steering", Float32, callback_steering)
    rospy.Subscriber("/speed", Float32, callback_speed)
    loop = rospy.Rate(60)
    servoPin = 12
    motorPin = 16
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPin,GPIO.OUT)
    GPIO.setup(motorPin,GPIO.OUT)
    steering = 0
    speed = 0
    servo = GPIO.PWM(servoPin, 100)
    servo.start(5.0)
    motor = GPIO.PWM(motorPin, 60.2)
    motor.start(0)
    cap = cv2.VideoCapture(0)
    brdg = CvBridge()
    print("ALL SUCCESFULLY INITIALIZED")
    dutySpeed, dutySteering=AngleToDuty(8.5, 0)
    servo.ChangeDutyCycle(dutySteering)
    motor.ChangeDutyCycle(dutySpeed)
    dutySpeed, dutySteering=AngleToDuty(0, 0)
    servo.ChangeDutyCycle(dutySteering)
    motor.ChangeDutyCycle(dutySpeed)
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

