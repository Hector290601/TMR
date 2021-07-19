#! /usr/bin/env python3
import rospy
from std_srvs.srv import SetBool
import RPi.GPIO as GPIO

led = 20

def setLedStateCallback(req):
    GPIO.output(led, req.data)
    return {'success':True,
            'message': 'Estado de led cambiado con exito'}

if __name__ == '__main__':
    rospy.init_node('actuator')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led, GPIO.OUT)
    rospy.Service('setLedStateCallback', SetBool, setLedStateCallback)
    rospy.loginfo("Servicio iniciado, listo para las peticiones")
    rospy.spin()
    GPIO.cleanup()
