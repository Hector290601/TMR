#-*-coding: latin-1-*-

import RPi.GPIO as GPIO
import time

def AngleToDuty(ang):
    return float(pos)/10.+5.

servoPin=12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPin,GPIO.OUT)
pwm=GPIO.PWM(servoPin,100)

depart =50
arrivee=130
DELAY=5
incStep=10
pos=depart

pwm.start(AngleToDuty(pos))

i=0
v = 60
while v != 'c':
    pos = int(v)
    print("--------------------------run {}".format(i))
    duty=AngleToDuty(pos)
    pwm.ChangeDutyCycle(duty)
    print("position: {}° -> duty cycle : {}%".format(pos,duty))
    i=i+1
    v = str(input("Ingrese un valor para la direccion: "))

pwm.stop()
GPIO.cleanup()
