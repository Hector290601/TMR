import RPi.GPIO as GPIO
import time

pins = [
        7,
        11, 12,
        13,
        15, 16,
            18,
            22,
        29,
        31, 32,
        33,
        35, 36,
        37, 38,
            40
        ]

enable = [
        7,
        40
        ]

motor = [
        11, 12,
        13,
        15, 16,
            18
        ]

motor = [
        18,
            13,
        12, 11
        ]

servo = [
        22,
        29,
        31, 32,
        33,
        35, 36,
        37, 38,
            40
        ]

"""

Mitades equivalen a cero

primeros seis bits son motor y siguientes diez son dirección, el cero y el último son banderas

"""

def enable_read():
    GPIO.output(7, 1)
    GPIO.output(40, 0)

def diable_read():
    GPIO.output(7, 0)
    GPIO.output(40, 1)

def write_motor_value(value):
    for pin in motor:
        print(pin)
        p = ( value & 1 )
        GPIO.output(pin, p)
        print(p)
        value >>= 1
    """
    GPIO.output(11, 1)
    GPIO.output(12, 1)
    GPIO.output(13, 1)
    """

GPIO.setmode(GPIO.BOARD)

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

#try:
if True:
    while True:
        #values = []
        velocidad = int(input("Velocidad del 0 a 64: "))
        enable_read()
        write_motor_value(velocidad)
        diable_read()
"""
except:
    GPIO.cleanup()
"""

