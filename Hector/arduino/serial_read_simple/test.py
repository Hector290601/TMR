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
        35, 36
        ]

GPIO.setmode(GPIO.BOARD)

for pin in pins:
    GPIO.setup(pin, GPIO.OUT)

for pin in pins:
    GPIO.output(pin, GPIO.HIGH)
try:
    time.sleep(100)
except:
    GPIO.cleanup()

