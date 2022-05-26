#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)

p = GPIO.PWM(16, 100) # 60.2
p.start(0)

while 1:
    i = input("Porcentaje: ")
    if i == 'c':
        break
    i = float(i)
    p.ChangeDutyCycle(i)
    print(i)

GPIO.cleanup()
