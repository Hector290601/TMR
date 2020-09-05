import time
import serial


arduinoPort = serial.Serial('/dev/ttyACM0', 9600, timeout=1)

time.sleep(1.8)

while True:
    i = str(input("Ingrese un valor numérico para enviar a arduino: "))
    iString = i
    if iString == 'c':
        break
    arduinoPort.write(iString.encode())
    getSerialValue = arduinoPort.readline()
    print('Valor retornado de Arduino: ', getSerialValue)

arduinoPort.close()

