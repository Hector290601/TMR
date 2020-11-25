import freenect
import time

dev = freenect.open_device(freenect.init(), 0)
for i in range(0, 31):
    print(i)
    freenect.set_tilt_degs(dev, i)
    time.sleep(0.5)
