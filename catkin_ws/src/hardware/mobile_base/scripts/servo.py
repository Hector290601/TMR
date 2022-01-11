#!/usr/bin/env python3
#-*-coding: latin-1-*-

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
    servoPin=12
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPin,GPIO.OUT)
    steering = 0
    pwm=GPIO.PWM(servoPin, 50)
    pwm.start(AngleToDuty())
    speed = 0
    while not rospy.is_shutdown():
        #
        # TODO:
        # Transform steering to pwm values
        #
        duty=AngleToDuty()
        pwm.ChangeDutyCycle(3)
        loop.sleep()
        

    pwm.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    main()
