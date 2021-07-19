#! /usr/bin/env python
import rospy
from std_srvs.srv import SetBool
import RPi.GPIO as GPIO

boton = 16

def buttonCallback(channel):
    poweOnLed = not GPIO.input(boton)
    rospy.wait_for_service(powerOnLed)
    try:
        setLedState = rospy.ServiceProxy('setLedState', SetBool)
        resp = setLedState(powerOnLed)
    except rospy.ServiceException, e:
        rosyp.logwarn(e)

if __name__ == '__main__':
    rospy.init_node('boton')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(boton, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.add_event_detect(
            boton, GPIO.BOTH,
            callback = buttonCallback, bouncetime=50
            )
    rospy.spin()
    GPIO.cleanup()

