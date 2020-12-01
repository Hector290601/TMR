import freenect
import os
import time

dev = freenect.open_device(freenect.init(), 0)
while True:
    os.system('clear')
    print(freenect.get_accel(dev))
    time.sleep(0.1)
