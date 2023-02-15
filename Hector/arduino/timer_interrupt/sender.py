import serial
import time

arduino = serial.Serial("/dev/ttyUSB0", 115200)

while True:
    """
    i = float(input("Steering: "))
    arduino.write(('d' + str(i) + '\n').encode())
    """
    delay = 0.1
    for i in range(5, 14, 1):
        print(i*0.1)
        time.sleep(delay)
        arduino.write(bytes([i*10]))
    """
    for i in range(14, 5, -1):
        print(i*0.1)
        time.sleep(delay)
        arduino.write((str(i*100) + '\n').encode())
        print(type((str(i*100) + '\n').encode()))
    """
