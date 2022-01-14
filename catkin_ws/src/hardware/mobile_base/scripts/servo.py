#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import rospy
from std_msgs.msg import Float32

steering = 0
speed = 0

def AngleToDuty():
    global steering
    return float(steering)/10.+5.

def callback_steering(msg):
    global steering
    steering = msg.data #Steering in radians

def callback_speed(msg):
    global speed
    speed = msg.data

def main():
    global steering, speed
    print("INITIALIZING SERVO CONTROL NODE...")
    rospy.init_node("mobile_base")
    rospy.Subscriber("/steering", Float32, callback_steering)
    rospy.Subscriber("/speed", Float32, callback_speed)
    loop = rospy.Rate(10)
    servoPin = 12
    motorPin = 16
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPin,GPIO.OUT)
    GPIO.setup(motorPin,GPIO.OUT)
    steering = 0
    speed = 0
    servo = GPIO.PWM(servoPin, 50)
    servo.start(AngleToDuty())
    motor = GPIO.PWM(motorPin, 60.2)
    motor.start(9)
    while not rospy.is_shutdown():
        duty=AngleToDuty()
        servo.ChangeDutyCycle(steering)
        motor.ChangeDutyCycle(9)
        loop.sleep() 
    servo.stop()
    motor.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    main()

