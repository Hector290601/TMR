import serial
import time

arduino = serial.Serial("COM5", 115200)

while True:
    """
    i = int(input("32~127: "))
    arduino.write(chr(i).encode())
    """
    delay = 0.1
    for i in range(95, 125):
        print(i, end=":")
        print(chr(i))
        time.sleep(delay)
        arduino.write(chr(i).encode())
    for i in range(125, 75, -1):
        print(i, end=":")
        print(chr(i))
        time.sleep(delay)
        arduino.write(chr(i).encode())
    for i in range(75, 95):
        print(i, end=":")
        print(chr(i))
        time.sleep(delay)
        arduino.write(chr(i).encode())
