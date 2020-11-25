import freenect
import time

mdev = freenect.open_device(freenect.init(), 0)
for i in [0, 1, 2, 3, 4, 5, 6]:
    freenect.set_led(mdev, i)
    print(i)
    time.sleep(3)
