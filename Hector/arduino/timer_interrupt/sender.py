import serial

arduino = serial.Serial("COM3", 115200)

while True:
    value = int(input("Valor: "))
    arduino.write(chr(value).encode())
