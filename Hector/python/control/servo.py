import RPi.GPIO as GPIO
import time
import math

def AngleToDuty(ang):
    dty = float(ang)/10. + 5.
    return dty

servoPin=12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servoPin,GPIO.OUT)
pwm=GPIO.PWM(servoPin, 100)

depart =-.44
arrivee=.44

pwm.start(AngleToDuty(0))

v = 0

while v != 'c':
    pos = float(v)
    duty=AngleToDuty(pos)
    print([duty, pos])
    pwm.ChangeDutyCycle(duty)
    print("position: {}° -> duty cycle : {}%".format(pos,duty))
    v = str(input("Ingrese un valor para la direccion: "))

pwm.stop()
GPIO.cleanup()
