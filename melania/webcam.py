import cv2
#import freenect
import numpy as np
import math
import pandas as pd
import time
import matplotlib.pyplot as plt 
import os

leftX = []
leftY = []
rightX = []
rightY = []

detected = pd.DataFrame(columns=('direction', 'leftFitAverage', 'rightFitAverage', 'leftLine', 'rigthLine', 'slopeLeft', 'interceptLeft', 'slopeRight', 'interceptRight' ))

startTime = time.time()
def imageRec(imageRec2):
    gray = cv2.cvtColor(imageRec2, cv2.COLOR_BGR2GRAY)
    canny = cannyImage(gray)
    croppedImage, imageRec2 = regionOfInterest(canny, imageRec2)
    colorMax=np.array([255, 255, 255])
    colorMin=np.array([79,73,57])
    colorInRange = colorRange(coppiedFrame, gray, croppedImage,colorMin,colorMax)
    lines = cv2.HoughLinesP(colorInRange, 1, np.pi/180, 50, minLineLength=20, maxLineGap=50)
    if lines is not None:
        averagedLines, left, right =  averagedSlopeIntercept(coppiedFrame, lines)
        if left:
            cv2.putText(coppiedFrame, '<---', (0, 30), font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
        elif right:
            cv2.putText(coppiedFrame, '--->', (0, 30), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(coppiedFrame, '^', (0, 30), font, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
            timeText = time.strftime("%Y/%m/%d %H:%M:%S %Z", time.localtime())
            cv2.putText(coppiedFrame, timeText, (250, 20), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
            lineImage = displayLines(coppiedFrame, averagedLines)
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(coppiedFrame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    return imageRec2
def imageReci(imageReci2):
    gray = cv2.cvtColor(imageReci2, cv2.COLOR_BGR2GRAY)
    canny = cannyImage(gray)
    croppedImage, imageReci2 = regionOfInterest(canny, imageReci2)
    colorMax=np.array([255, 255, 255])
    colorMin=np.array([79,73,57])
    colorInRange = colorRange(coppiedFrame, gray, croppedImage,colorMin,colorMax)
    lines = cv2.HoughLinesP(colorInRange, 1, np.pi/180, 50, minLineLength=20, maxLineGap=50)
    if lines is not None:
        averagedLines, left, right =  averagedSlopeIntercept(coppiedFrame, lines)
        if left:
            cv2.putText(coppiedFrame, '<---', (0, 30), font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
        elif right:
            cv2.putText(coppiedFrame, '--->', (0, 30), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
        else:
            cv2.putText(coppiedFrame, '^', (0, 30), font, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
            timeText = time.strftime("%Y/%m/%d %H:%M:%S %Z", time.localtime())
            cv2.putText(coppiedFrame, timeText, (250, 20), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
            lineImage = displayLines(coppiedFrame, averagedLines)
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(coppiedFrame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    return imageReci2
def cannyImage(cannyGray):
    cannyBlur = cv2.GaussianBlur(cannyGray, (5, 5), 0)
    cannyCanny = cv2.Canny(cannyBlur, 10, 250)
    return cannyCanny

def regionOfInterest(regionImage, toPol):
    regionPolygons = np.array([[(0, 470), (640, 470), (640, 420), (400, 250), (220, 250), (0, 420)]])
    cv2.polylines(toPol,[regionPolygons],True,(0,255,255))
    zeros = np.zeros_like(regionImage)
    cv2.fillPoly(zeros, regionPolygons, 255)
    regionedImage = cv2.bitwise_and(regionImage, regionImage, mask=zeros)
    return regionedImage, toPol

def colorRange(colorFrame, colorGray, colorCropped, colorMax,colorMin):
    colorColor = cv2.bitwise_and(colorFrame, colorFrame, mask = colorCropped)
    colorRanged = cv2.inRange(colorColor, colorMin, colorMax)
    return colorRanged

def averagedSlopeIntercept(interceptImage, interceptLines):
    global leftX, leftY, rightX, rightY
    leftFit = []
    rightFit = []
    for line in interceptLines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0:
            leftFit.append((slope, intercept))
        else:
            rightFit.append((slope, intercept))
    leftFitAverage = np.average(leftFit, axis = 0)
    rightFitAverage = np.average(rightFit, axis = 0)
    try:
        isNanLeft = math.isnan(leftFitAverage[0])
    except:
        isNanLeft = math.isnan(leftFitAverage)
    try:
        isNanRight = math.isnan(rightFitAverage[0])
    except:
        isNanRight = math.isnan(rightFitAverage)
    leftLine, slopeLeft, interceptLeft =  makeCoordinates(interceptImage, leftFitAverage)
    rightLine, slopeRight, interceptRight = makeCoordinates(interceptImage, rightFitAverage)
    deltaTime = time.time() - startTime
    if isNanLeft:
        print('L')
    elif isNanRight:
        print('R')
    else:
        detected.loc[len(detected)]=['C', leftFitAverage, rightFitAverage, leftLine, rightLine, slopeLeft, interceptLeft, slopeRight, interceptRight]
    return np.array([leftLine, rightLine]), isNanLeft, isNanRight

def makeCoordinates(coordinatesImage, lineParameters):
    try:
        slope, intercept = lineParameters
        y1 = coordinatesImage.shape[0]
        y2 = int(y1*(3/5))
        x1 = int((y1 - intercept)/slope)
        x2 = int((y2 - intercept) / slope)
        return np.array([x1, y1, x2, y2]), slope, intercept
    except:
        return np.array([0, 0, 0, 0]), np.nan, np.nan

def displayLines(displayImage, displayLinesVar):
    lineImage = np.zeros_like(displayImage)
    if displayLinesVar is not None:
        for x1, y1, x2, y2 in displayLinesVar:
            try:
                cv2.line(lineImage, (x1, y1), (x2, y2), (255, 255, 255), 3)
            except:
                lineImage = lineImage
    return lineImage

def improveImage(frame, a):
    hsvVideo = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsvVideo = hsvVideo.astype(np.uint8)
    h, s, v = cv2.split(hsvVideo)
    v += a
    hsvVideo = cv2.merge((h, s, v))
    return hsvVideo

if __name__ == '__main__':
    font = cv2.FONT_HERSHEY_SIMPLEX
    camara = cv2.VideoCapture(0)
    vChange = 87
    
    while True:
        ret, origFrame= camara.read()
        coppiedFrame = np.copy(origFrame)
        hsvVideo = improveImage(origFrame, vChange)
        origFrame = cv2.cvtColor(hsvVideo, cv2.COLOR_HSV2BGR)
        origFrames = imageRec(coppiedFrame)
        origFrame= imageReci(origFrame)
        k = cv2.waitKey(250)
        if k == ord('s'):
            break
        elif k == ord('a') and vChange > 0:
            vChange -= 1
            print(vChange)
        elif k == ord('d') and vChange < 255:
            vChange += 1
            print(vChange)
        cv2.imshow("origFrame", origFrame)
        cv2.imshow("origFrames", origFrames)
        cv2.imshow("hsvVideo", hsvVideo)
        cv2.imshow("coppiedFrameWithLines", coppiedFrame)
    timeSaved = time.strftime("%Y%m%d%H%M%S%Z", time.localtime())
    name1 = 'detected' + timeSaved + '.csv'
    name2 = 'detected' + timeSaved + 'HeadAndIndexFalse.csv'
    detected.to_csv(name1)
    detected.to_csv(name2, header=False, index=False)
    cv2.destroyAllWindows()
