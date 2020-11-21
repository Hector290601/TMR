from mpu6050 import mpu6050
import os
import time

sensor = mpu6050(0x68)

def main():
    while True:
        print(sensor.get_gyro_data())
        time.sleep(0.1)
        os.system('clear')

if __name__ == '__main__':
    main()

