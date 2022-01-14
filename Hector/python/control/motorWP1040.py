#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)

p = GPIO.PWM(16, 60.2)  # channel=7 frequency=50Hz
p.start(9)

while 1:
    i = input("Porcentaje: ")
    if i == 'c':
        break
    i = float(i)
    print(i)
    p.ChangeDutyCycle(i)
p.stop()
GPIO.cleanup()
