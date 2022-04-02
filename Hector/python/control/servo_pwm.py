#-*-coding: latin-1-*-
import time
import RPi.GPIO as GPIO
import math

def ang_to_duty(ang):
    pos = ang * (180 * math.pi)
    duty = pos/10.+5.
    return duty

servo_pin = 12
motor_pin = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin, GPIO.OUT)
GPIO.setup(motor_pin, GPIO.OUT)
pwm_servo = GPIO.PWM(servo_pin, 100)
pwm_motor = GPIO.PWM(motor_pin, 50)

pwm_servo.start(0)
pwm_motor.start(0)

# Activar motor: 10 % -> 0 %

try:
    while True:
        pwm_servo.ChangeDutyCycle(ang_to_duty(.08))
        pwm_motor.ChangeDutyCycle(5)
except:
    GPIO.cleanup()
