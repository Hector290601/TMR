import freenect
import cv2
import numpy as np

def getRGB():
    frameUnconverted, _ = freenect.sync_get_video()
    bgrVideo = cv2.cvtColor(frameUnconverted, cv2.COLOR_RGB2BGR)
    hsvVideo = cv2.cvtColor(bgrVideo, cv2.COLOR_BGR2HSV)
    bgrVideo = bgrVideo.astype(np.uint8)
    hsvVideo = hsvVideo.astype(np.uint8)
    h, s, v = cv2.split(hsvVideo)
    v0 = v
    v50 = v + 50
    v100 = v + 100
    v150 = v + 150
    v200 = v + 200
    v250 = v + 250
    v255 = v + 255
    final0 = cv2.merge((h, s, v0))
    final50 = cv2.merge((h, s, v50))
    final100 = cv2.merge((h, s, v100))
    final150 = cv2.merge((h, s, v150))
    final200 = cv2.merge((h, s, v200))
    final250 = cv2.merge((h, s, v250))
    final255 = cv2.merge((h, s, v255))
    improved0 = cv2.cvtColor(final0, cv2.COLOR_HSV2BGR)
    improved50 = cv2.cvtColor(final50, cv2.COLOR_HSV2BGR)
    improved100 = cv2.cvtColor(final100, cv2.COLOR_HSV2BGR)
    improved150 = cv2.cvtColor(final150, cv2.COLOR_HSV2BGR)
    improved200 = cv2.cvtColor(final200, cv2.COLOR_HSV2BGR)
    improved250 = cv2.cvtColor(final250, cv2.COLOR_HSV2BGR)
    improved255 = cv2.cvtColor(final255, cv2.COLOR_HSV2BGR)
    return bgrVideo, improved0, improved50, improved100, improved150, improved200, improved250, improved255

def getDepth():
    irSensor, _ = freenect.sync_get_depth()
    np.clip(irSensor, 0, 2**10-1, irSensor)
    irSensor >>=2
    irSensor = irSensor.astype(np.uint8)
    return irSensor

def setTilt(dev, i):
    freenect.set_tilt_degs(dev, i)

def getAccel(dev):
    return freenect.get_accel(dev)

def setLed(dev, i):
    freenect.set_led(dev, i)

def main():
    tilt = 0
    led = 1
    while True:
        frame, a, b, c, d, e, f, g = getRGB()
        depth = getDepth()
        cv2.imshow('frame', frame)
        cv2.imshow('depth', depth)
        cv2.imshow('0', a)
        cv2.imshow('50', b)
        cv2.imshow('100', c)
        cv2.imshow('150', d)
        cv2.imshow('200', e)
        cv2.imshow('250', f)
        cv2.imshow('255', g)
        #dev = freenect.open_device(freenect.init(), 0)
        #setTilt(dev, tilt)
        #setLed(dev, led)
        k = cv2.waitKey(1)
        if k == 27:
            break
        """
        elif k == ord('w'):
            tilt += 1
            setTilt(dev, tilt)
        elif k == ord('s'):
            tilt -= 1
            setTilt(dev, tilt)
        elif k == ord('a'):
            led -= 1
            setLed(dev, led)
        elif k == ord('d'):
            led += 1
            setLed(dev, led)
        """

if __name__ == '__main__':
    main()
