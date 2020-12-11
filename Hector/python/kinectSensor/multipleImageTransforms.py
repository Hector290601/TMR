import freenect
import cv2
import numpy as np
import matplotlib.pyplot as plt

def getBGR():
    frameUnconverted, _ = freenect.sync_get_video()
    bgrVideo = cv2.cvtColor(frameUnconverted, cv2.COLOR_RGB2BGR)
    bgrVideo = bgrVideo.astype(np.uint8)
    return bgrVideo

def getDepth():
    irSensor, _ = freenect.sync_get_depth()
    np.clip(irSensor, 0, 2**10-1, irSensor)
    irSensor >>=2
    irSensor = cv2.cvtColor(irSensor, cv2.COLOR_GRAY2BGR)
    irSensor = irSensor.astype(np.uint8)
    return irSensor

def toOthercolorspaces(frame, vS, bS):
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
    improvedHls = cv2.cvtColor(finalHls, cv2.COLOR_HLS2BGR)
    return improvedHls, improvedHsv

def blurs(improvedHsv, improvedHls):
    kernel = np.ones((5,5),np.float32)/25
    medianBlurHsv = cv2.medianBlur(improvedHsv, 5)
    medianBlurHls = cv2.medianBlur(improvedHls, 5)
    filter2DHsv = cv2.filter2D(improvedHsv, -1, kernel)
    filter2DHls = cv2.filter2D(improvedHls, -1, kernel)
    blurHsv = cv2.blur(improvedHsv, (5, 5))
    blurHls = cv2.blur(improvedHls, (5, 5))
    gausianBlurHsv = cv2.medianBlur(improvedHsv, 5)
    gausianBlurHls = cv2.medianBlur(improvedHls, 5)
    bilateralFilterHsv = cv2.bilateralFilter(improvedHsv, 9, 75, 75)
    bilateralFilterHls = cv2.bilateralFilter(improvedHls, 9, 75, 75)
    return medianBlurHls, medianBlurHsv, filter2DHls, filter2DHsv, blurHls, blurHsv, gausianBlurHls, gausianBlurHsv, bilateralFilterHls, bilateralFilterHsv

def main():
    vS = 243
    bS = 245
    while True:
        frame = getBGR()
        depth = getDepth()
        improvedHls, improvedHsv = toOthercolorspaces(frame, vS, bS)
        medianBlurHls, medianBlurHsv, filter2DHls, filter2DHsv, blurHls, blurHsv, gausianBlurHls, gausianBlurHsv, bilateralFilterHls, bilateralFilterHsv = blurs(improvedHsv, improvedHls)
        cv2.imshow('frame', frame)
        cv2.imshow('depth', depth)
        cv2.imshow('hsv', improvedHsv)
        cv2.imshow('hls', improvedHls)
        cv2.imshow("medianBlurHsv", medianBlurHsv)
        cv2.imshow("medianBlurHls", medianBlurHls)
        cv2.imshow("2DFilterHsv", filter2DHsv)
        cv2.imshow("2DfilterHls", filter2DHls)
        cv2.imshow("blurHsv", blurHsv)
        cv2.imshow("blurHls", blurHls)
        cv2.imshow("gaussianBlurHsv", gausianBlurHsv)
        cv2.imshow("gaussianBlurHls", gausianBlurHls)
        cv2.imshow("bilateralFilterHsv", bilateralFilterHsv)
        cv2.imshow("bilateralFilterHls", bilateralFilterHls)
        k = cv2.waitKey(1)
        if k == 27:
            break
        elif k == ord('w') and vS < 255:
            vS += 1
        elif k == ord('s') and vS > 0:
            vS -= 1
        elif k == ord('a') and bS < 255:
            bS += 1
        elif k == ord('d') and bS > 0:
            bS -= 1
        elif k == ord('p'):
            print("Suma a V y L: ", vS)
            print("Suma a S: ", bS)

if __name__ == '__main__':
    main()

