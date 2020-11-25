import freenect
import time

dev = freenect.open_device(freenect.init(), 0)
for i in [0, 1, 2, 3, 4, 5, 6]:
    freenect.set_led(dev, i)
    print(i)
    time.sleep(3)
