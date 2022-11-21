import serial

arduino = serial.Serial("COM5", 115200)

while True:
    for i in range(32, 126):
        print(i, end=":")
        print(chr(i))
        arduino.write(chr(i).encode())
        input()
