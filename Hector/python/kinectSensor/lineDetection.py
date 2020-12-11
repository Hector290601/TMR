import freenect
import cv2
import numpy as np
import matplotlib.pyplot as plt

def getBGR():
    frameUnconverted, _ = freenect.sync_get_video()
    bgrVideo = cv2.cvtColor(frameUnconverted, cv2.COLOR_RGB2BGR)
    bgrVideo = bgrVideo.astype(np.uint8)
    return bgrVideo

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
    improvedHls = cv2.cvtColor(finalHls, cv2.COLOR_HSV2BGR)
    return improvedHls, improvedHsv

def display_lines(img_bgr, average_lines):
    img_lines = np.zeros((img_bgr.shape[0], img_bgr.shape[1],3),dtype=np.uint8)
    if average_lines is None:
        return img_lines
    line_color = [255, 0, 0] #line color wil be blue
    line_thickness = 4
    dot_color = [0, 0, 255] #dot color will be red
    dot_size = 5
    for line in average_lines:
        for x1, y1, x2, y2 in line:
            cv2.line(img_lines, (x1, y1), (x2, y2), line_color, line_thickness)
            cv2.circle(img_lines, (x1, y1), dot_size, dot_color, -1)
            cv2.circle(img_lines, (x2, y2), dot_size, dot_color, -1)
    return img_lines

def main():
    led = 1
    vS = 243
    bS = 245
    while True:
        frame = getBGR()
        improvedHls, improvedHsv = toOthercolorspaces(frame, vS, bS)
        medianBlurHsv = cv2.medianBlur(improvedHsv, 5)
        bordes = cv2.Canny(medianBlurHsv, 400, 800)
        lines = cv2.HoughLinesP(bordes,rho=1.0,theta=np.pi/180,threshold=150,lines=None,minLineLength=175, maxLineGap=150)
        imgLines = display_lines(frame, lines)
        cv2.imshow('frame', frame)
        cv2.imshow('hsv', improvedHsv)
        cv2.imshow('cannyHsv', bordes)
        cv2.imshow('lines', imgLines)
        print(lines)
        k = cv2.waitKey(1)
        if k == 27:
            break

if __name__ == '__main__':
    main()

