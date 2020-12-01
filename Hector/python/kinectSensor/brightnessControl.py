import freenect
import cv2
import numpy as np

def getBGR():
    frameUnconverted, _ = freenect.sync_get_video()
    bgrVideo = cv2.cvtColor(frameUnconverted, cv2.COLOR_RGB2BGR)
    bgrVideo = bgrVideo.astype(np.uint8)
    return bgrVideo

def getDepth():
    irSensor, _ = freenect.sync_get_depth()
    np.clip(irSensor, 0, 2**10-1, irSensor)
    irSensor >>=2
    irSensor = irSensor.astype(np.uint8)
    return irSensor

def main():
    tilt = 0
    led = 1
    vS = 100
    bS = 100
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        frame = getBGR()
        depth = getDepth()
        hsvVideo = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hlsVideo = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
        hsvVideo = hsvVideo.astype(np.uint8)
        hlsVideo = hlsVideo.astype(np.uint8)
        h0, s0, v = cv2.split(hsvVideo)
        h1, l, s1  = cv2.split(hsvVideo)
        vSum = v + vS
        lSum = l + vS
        s0S = s0 + bS
        s1S = s1 + bS
        finalHsv = cv2.merge((h0, s0S, vSum))
        finalHls = cv2.merge((h1, lSum, s1S))
        improvedHsv = cv2.cvtColor(finalHsv, cv2.COLOR_HSV2BGR)
        improvedHls = cv2.cvtColor(finalHls, cv2.COLOR_HSV2BGR)
        cv2.imshow('frame', frame)
        cv2.imshow('depth', depth)
        cv2.imshow('hsv', improvedHsv)
        cv2.imshow('hls', improvedHls)
        k = cv2.waitKey(1)
        if k == 27:
            break
        elif k == ord('w'):
            vS += 1
        elif k == ord('s'):
            vS -= 1
        elif k == ord('a'):
            bS += 1
        elif k == ord('d'):
            bS -= 1
        elif k == ord('p'):
            print("Suma a V y L: ", vS)
            print("Suma a S: ", bS)

if __name__ == '__main__':
    main()
