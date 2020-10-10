import cv2
import numpy as np
import math
import pandas as pd
import time
import serial

directionPort = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
time.sleep(1.8)

xL = [0]
xR = [0]

detected = pd.DataFrame(columns=('direction', 'leftFitAverage', 'rightFitAverage', 'leftLine', 'rigthLine', 'slopeLeft', 'interceptLeft', 'slopeRight', 'interceptRight' ))

startTime = time.time()

def cannyImage(cannyGray):
    cannyBlur = cv2.GaussianBlur(gray, (5, 5), 0)
    cannyCanny = cv2.Canny(cannyBlur, 10, 250)
    return cannyCanny

def regionOfInterest(regionImage):
    regionPolygons = np.array([[(0, 400), (640, 400), (640, 180), (0, 180)]])
    zeros = np.zeros_like(regionImage)
    cv2.fillPoly(zeros, regionPolygons, 255)
    regionedImage = cv2.bitwise_and(regionImage, regionImage, mask=zeros)
    return regionedImage

def colorRange(colorFrame, colorGray, colorCropped):
    colorMax = np.array([255, 255, 255])
    colorMin = np.array([79, 73, 57])
    colorColor = cv2.bitwise_and(colorFrame, colorFrame, mask = colorCropped)
    colorRanged = cv2.inRange(colorColor, colorMin, colorMax)
    return colorRanged

def averagedSlopeIntercept(interceptImage, interceptLines):
    #global leftX, leftY, rightX, rightY
    global xL, yL, xR, yR
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
    xL.append(interceptLeft)
    xR.append(interceptRight)
    deltaTime = time.time() - startTime
    if isNanLeft:
        detected.loc[len(detected)]=['L', leftFitAverage, rightFitAverage, leftLine, rightLine, slopeLeft, interceptLeft, slopeRight, interceptRight]
    elif isNanRight:
        detected.loc[len(detected)]=['R', leftFitAverage, rightFitAverage, leftLine, rightLine, slopeLeft, interceptLeft, slopeRight, interceptRight]
    else:
        detected.loc[len(detected)]=['C', leftFitAverage, rightFitAverage, leftLine, rightLine, slopeLeft, interceptLeft, slopeRight, interceptRight]
    return np.array([leftLine, rightLine]), isNanLeft, isNanRight, slopeLeft, slopeRight

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

def makeDegrees(leftSide, rightSide, anterior):
    summed = rightSide - leftSide
    if summed >= 1.7 or summed <=1.5:
        print(summed)
        if rightSide <= -0.11:
            degrees = 90 + (rightSide * 10)
            if anterior != degrees:
                anterior = degrees
                degreesStr = str(degrees)
        elif rightSide >= -0.8 :
            degrees = 90 + (rightSide * 10)
            if anterior != degrees:
                anterior = degrees
                degreesStr = str(degrees)
        elif leftSide <= 0.6:
            degrees = 90 + (leftSide * 10)
            if anterior != degrees:
                anterior = degrees
                degreesStr = str(degrees)
        elif leftSide >= 0.8:
            degrees = 90 + (leftSide * 10)
            if anterior != degrees:
                anterior = degrees
                degreesStr = str(degrees)
        return degreesStr, anterior
    else:
        return str(90), 90

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    salida = cv2.VideoWriter('videoSalida.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(int(cap.get(3)),int(cap.get(4))))
    font = cv2.FONT_HERSHEY_SIMPLEX
    leftDirection = str(120)
    rightDirection = str(60)
    rectDirection = str(90)
    directionPort.write(rectDirection.encode())
    anterior = 0
    print("Starting")
    while cap.isOpened():
        try:
            print("Running")
            print("Actual: ", anterior)
            ret, origFrame = cap.read()        
            coppiedFrame = np.copy(origFrame)    
            gray = cv2.cvtColor(origFrame, cv2.COLOR_BGR2GRAY)
            canny = cannyImage(gray)
            croppedImage = regionOfInterest(canny)
            colorInRange = colorRange(coppiedFrame, gray, croppedImage)
            lines = cv2.HoughLinesP(colorInRange, 1, np.pi/180, 50, minLineLength=20, maxLineGap=50)
            if lines is not None:
                averagedLines, left, right, lSlope, rSlope =  averagedSlopeIntercept(coppiedFrame, lines)
                if left:
                    cv2.putText(coppiedFrame, 'L', (0, 30), font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
                    directionPort.write(leftDirection.encode())
                    if anterior != -1:
                        directionPort.write(leftDirection.encode())
                        anterior = -1
                        time.sleep(1)
                elif right:
                    cv2.putText(coppiedFrame, 'R', (0, 30), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
                    directionPort.write(rightDirection.encode())
                    if anterior != 1:
                        directionPort.write(rightDirection.encode())
                        anterior = 1
                        time.sleep(1)
                elif not right and not left:
                    cv2.putText(coppiedFrame, 'C', (0, 30), font, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
                    directionPort.write(rectDirection.encode())
                    if anterior != 0:
                        directionPort.write(rectDirection.encode())
                        anterior = 0
                        time.sleep(1)
                else:
                    cv2.putText(coppiedFrame, 'V', (0, 30), font, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
                if anterior != 0:
                        directionPort.write(rectDirection.encode())
                        anterior = 0
                timeText = time.strftime("%Y/%m/%d %H:%M:%S %Z", time.localtime())
                cv2.putText(coppiedFrame, timeText, (250, 20), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
                for line in lines:
                    x1, y1, x2, y2 = line[0]
                    cv2.line(coppiedFrame, (x1, y1), (x2, y2), (0, 255, 0), 5)
                if cv2.waitKey(25) & 0xFF == ord('s'):
                    break
                if lines is None:
                    break
                salida.write(coppiedFrame)
            timeSaved = time.strftime("%Y%m%d", time.localtime())
            name1 = 'detected' + timeSaved + '.csv'
            name2 = 'detected' + timeSaved + 'HeadAndIndexFalse.csv'
            detected.to_csv(name1)
            detected.to_csv(name2, header=False, index=False)
        except:
            print("Algo ha ocurrido")
    cap.release()
    cv2.destroyAllWindows()
    directionPort.write(rectDirection.encode())
    directionPort.close()