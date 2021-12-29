#!/usr/bin/env python
#-*-coding: latin-1-*-

import RPi.GPIO as GPIO
import time
import rospy
from std_msgs.msg import Float32

def AngleToDuty(ang):
    return float(pos)/10.+5.

def callback_steering(msg):
    global steering
    steering = msg.data #Steering in radians

def callback_speed(msg):
    global speed
    speed = msg.data

def main():
    print("INITIALIZING SERVO CONTROL NODE...")
    rospy.init_node("mobile_base")
    rospy.Subscribe("/steering", Float32, callback_steering)
    rospy.Subscribe("/speed", Float32, callback_speed)
    loop = rospy.Rate(10)
    servoPin=12
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(servoPin,GPIO.OUT)
    pwm=GPIO.PWM(servoPin,100)
    
    pwm.start(AngleToDuty(pos))

    i=0
    v = 60
    global steering, speed
    steering = 0
    speed = 0
    while not rospy.is_shutdown():
        #
        # TODO:
        # Transform steering to pwm values
        #
        pos = int(v)
        duty=AngleToDuty(pos)
        pwm.ChangeDutyCycle(duty)
        i=i+1
        

    pwm.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    main()
