#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)

p = GPIO.PWM(16, 50) # 60.2
p.start(7)
time.sleep(1)
p.ChangeDutyCycle(0)

while 1:
    i = input("Porcentaje: ")
    if i == 'c':
        break
    i = float(i)
    print(i)
    p.ChangeDutyCycle(i)
    """
    for i in range(0, 100, 1):
        p.ChangeDutyCycle(i)
        print(i)
        time.sleep(1)
    for i in range(100, 0, -1):
        p.ChangeDutyCycle(i)
        print(i)
        time.sleep(1)
    p.stop()
    time.sleep(5)
    """
GPIO.cleanup()
