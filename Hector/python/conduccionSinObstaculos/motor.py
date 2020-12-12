import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
leftEnable = 13
rightEnable = 15
lPwm = 16
rPwm = 18

GPIO.setup(leftEnable, GPIO.OUT)
GPIO.setup(rightEnable, GPIO.OUT)
GPIO.setup(lPwm, GPIO.OUT)
GPIO.setup(rPwm, GPIO.OUT)

forward = GPIO.PWM(lPwm, 100)
backward = GPIO.PWM(rPwm, 100)

forward.start(0)
backward.start(0)

print("Go backward")
GPIO.output(lPwm, GPIO.HIGH)
GPIO.output(rPwm, GPIO.LOW)
forward.ChangeDutyCycle(0)
backward.ChangeDutyCycle(100)
sleep(3)

print("NOW S T O P MOTOR")
GPIO.output(lPwm, GPIO.LOW)
GPIO.output(rPwm, GPIO.LOW)
forward.ChangeDutyCycle(0)
backward.ChangeDutyCycle(0)
sleep(2)

print("Go forward")
GPIO.output(lPwm, GPIO.LOW)
GPIO.output(rPwm, GPIO.HIGH)
forward.ChangeDutyCycle(100)
backward.ChangeDutyCycle(0)
sleep(3)

print("NOW S T O P MOTOR")
GPIO.output(lPwm, GPIO.LOW)
GPIO.output(rPwm, GPIO.LOW)
GPIO.output(leftEnable, GPIO.LOW)
GPIO.output(rightEnable, GPIO.LOW)
forward.stop()
backward.stop()
sleep(2)

GPIO.cleanup()
