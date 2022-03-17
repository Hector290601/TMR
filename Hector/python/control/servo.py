#-*-coding: latin-1-*-

import RPi.GPIO as GPIO
import time
import math

def AngleToDuty(ang):
    pos = ang * (180 / math.pi)
    dty = pos/10. + 5.
    print([pos, dty])
    return dty

servoPin=12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPin,GPIO.OUT)
pwm=GPIO.PWM(servoPin,100)

depart =-.44
arrivee=.44
DELAY=5
pos=depart

pwm.start(AngleToDuty(0))

i= 0
v = 0
while v != 'c':
    pos = float(v)
    print("--------------------------run {}".format(i))
    duty=AngleToDuty(pos)
    print([duty, pos])
    pwm.ChangeDutyCycle(duty)
    print("position: {}° -> duty cycle : {}%".format(pos,duty))
    i=i+1
    v = str(input("Ingrese un valor para la direccion: "))

pwm.stop()
GPIO.cleanup()
