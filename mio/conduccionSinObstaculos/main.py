import threading
import logging
import datetime
import cv2
import numpy as np
import math
import pandas as pd
import time
import RPi.GPIO as GPIO

#directionPort = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
#time.sleep(1.8)

xL = [0]
xR = [0]
directionPin = 12
leftEnable = 13
rightEnable = 15
lPwm = 16
rPwm = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(directionPin,GPIO.OUT)
GPIO.setup(leftEnable,GPIO.OUT)
GPIO.setup(rightEnable,GPIO.OUT)
GPIO.setup(lPwm,GPIO.OUT)
GPIO.setup(rPwm,GPIO.OUT)

forward = GPIO.PWM(lPwm, 100)
backward = GPIO.PWM(rPwm, 100)
servo = GPIO.PWM(directionPin, 100)

forward.start(0)
backward.start(0)

detected = pd.DataFrame(columns=('direction', 'leftFitAverage', 'rightFitAverage', 'leftLine', 'rigthLine', 'slopeLeft', 'interceptLeft', 'slopeRight', 'interceptRight' ))

startTime = time.time()


def angleToDuty(pos):
    return float(pos)/10.+5.

servo.start(angleToDuty(90))

def linesOnImage(lines):
    for line in lines:
        x1, y1, x2, y2 = line[0]
        cv2.line(coppiedFrame, (x1, y1), (x2, y2), (0, 255, 0), 5)

def directionLeft(left):
    if left:
        GPIO.output(lPwm, GPIO.HIGH)
        GPIO.output(rPwm, GPIO.LOW)
        servo.ChangeDutyCycle(angleToDuty(60))
        forward.ChangeDutyCycle(30)
        print("left")

def directionRight(right):
    if right:
        GPIO.output(lPwm, GPIO.HIGH)
        GPIO.output(rPwm, GPIO.LOW)
        servo.ChangeDutyCycle(angleToDuty(120))
        forward.ChangeDutyCycle(30)
        print("right")

def directionCenter(lft, right):
    if not right and not left:
        GPIO.output(lPwm, GPIO.HIGH)
        GPIO.output(rPwm, GPIO.LOW)
        servo.ChangeDutyCycle(angleToDuty(90))
        forward.ChangeDutyCycle(45)
        print("center")

def directionUnknow(left, right):
    if left and right:
        GPIO.output(lPwm, GPIO.HIGH)
        GPIO.output(rPwm, GPIO.LOW)
        servo.ChangeDutyCycle(angleToDuty(90))
        backward.ChangeDutyCycle(60)
        print("U N K N O W")

def graphicInterface(left, right, coppiedFrame, anterior):
    if left:
        cv2.putText(coppiedFrame, '<---', (0, 30), font, 0.8, (255, 0, 0), 2, cv2.LINE_AA)
        if anterior != -1:
            anterior = -1
    if right:
        cv2.putText(coppiedFrame, '--->', (0, 30), font, 0.8, (0, 255, 0), 2, cv2.LINE_AA)
        if anterior != 1:
            anterior = 1
    if not right and not left:
        cv2.putText(coppiedFrame, '^', (0, 30), font, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
        if anterior != 0:
            anterior = 0
    if left and right:
        cv2.putText(coppiedFrame, 'UNKNOW', (0, 30), font, 0.8, (0, 0, 255), 2, cv2.LINE_AA)
        anterior = 255
    timeText = time.strftime("%Y/%m/%d %H:%M:%S %Z", time.localtime())
    cv2.putText(coppiedFrame, timeText, (250, 20), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)


def putTimeData(coppiedFrame, font):
    timeText = time.strftime("%Y/%m/%d %H:%M:%S %Z", time.localtime())
    cv2.putText(coppiedFrame, timeText, (250, 20), font, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

def saveVideo(salida, coppiedFrame):
    salida.write(coppiedFrame)


def cannyImage(cannyGray):
    cannyBlur = cv2.GaussianBlur(gray, (5, 5), 0)
    cannyCanny = cv2.Canny(cannyBlur, 10, 250)
    return cannyCanny

def regionOfInterest(regionImage):
    #regionPolygons = np.array([[(0, 448), (639, 425), (434, 276), (256, 159)]])
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
            #leftX.append(slope)
            #leftY.append(intercept)
        else:
            rightFit.append((slope, intercept))
            #rightX.append(slope)
            #rightY.append(intercept)
    leftFitAverage = np.average(leftFit, axis = 0)
    rightFitAverage = np.average(rightFit, axis = 0)
    try:
        isNanLeft = math.isnan(leftFitAverage[0])
    except:
        isNanLeft = math.isnan(leftFitAverage)
    #print("Left ", isNanLeft)
    try:
        isNanRight = math.isnan(rightFitAverage[0])
    except:
        isNanRight = math.isnan(rightFitAverage)
    #print("Right ", isNanRight)
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
    #print("lineParameters: ", lineParameters)
    try:
        slope, intercept = lineParameters #intercept es la ordenada al origen de la recta
        #print("slope: ", slope, "intercept ", intercept)
        y1 = coordinatesImage.shape[0] #obtiene el valor '0' de la imagen
        y2 = int(y1*(3/5)) #esto es pra determinar el largo de la recta que dibuja en la imagen
        x1 = int((y1 - intercept)/slope) #obtiene la ecuación de la recta con el primer punto
        x2 = int((y2 - intercept) / slope) # obtiene la ecuación de la recta con el segundo punto
        #print(type(lineParameters))
        return np.array([x1, y1, x2, y2]), slope, intercept
    except:
        return np.array([0, 0, 0, 0]), np.nan, np.nan

def makeDegrees(leftSide, rightSide):
    summed = rightSide - leftSide
    if summed >= 1.7 or summed <=1.5:
        print(summed)
        if rightSide <= -0.11:
            degrees = 90 + (9 - rightSide)
            degreesStr = str(degrees)
        elif rightSide >= -0.8 :
            degrees = 90 + (9 - rightSide)
            degreesStr = str(degrees)
        elif leftSide <= 0.6:
            degrees = 90 + (9 - leftSide)
            degreesStr = str(degrees)
        elif leftSide >= 0.8:
            degrees = 90 + (90 - leftSide)
            degreesStr = str(degrees)
        return degreesStr
    else:
        return str(90)
try:
    if __name__ == '__main__':
        cap = cv2.VideoCapture(0)
        salida = cv2.VideoWriter('videoSalida.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(int(cap.get(3)),int(cap.get(4))))
        font = cv2.FONT_HERSHEY_SIMPLEX
        leftDirection = str(115)
        rightDirection = str(65)
        rectDirection = str(90)
        unknowDirection = str(255)
        anterior = 0
        while cap.isOpened():
            timeIni = time.time()
            ret, origFrame = cap.read()
            coppiedFrame = np.copy(origFrame)
            gray = cv2.cvtColor(origFrame, cv2.COLOR_BGR2GRAY)
            canny = cannyImage(gray)
            croppedImage = regionOfInterest(canny)
            colorInRange = colorRange(coppiedFrame, gray, croppedImage)
            lines = cv2.HoughLinesP(colorInRange, 1, np.pi/180, 50, minLineLength=20, maxLineGap=50)
            if lines is not None:
                averagedLines, left, right, lSlope, rSlope =  averagedSlopeIntercept(coppiedFrame, lines)
                GPIO.output(lPwm, GPIO.HIGH)
                GPIO.output(rPwm, GPIO.LOW)
                t1 = threading.Thread(target = graphicInterface, args=(left, right, coppiedFrame, anterior))
                t2 = threading.Thread(target=saveVideo, args=(salida, coppiedFrame))
                t3 = threading.Thread(target=linesOnImage, args=(lines, ))
                t4 = threading.Thread(target=directionLeft, args=(left, ))
                t5 = threading.Thread(target=directionRight, args=(right, ))
                t6 = threading.Thread(target=directionCenter, args=(left, right))
                t7 = threading.Thread(target=directionUnknow, args=(left, right))
                t8 = threading.Thread(target=putTimeData, args=(coppiedFrame, font))
                t1.start()
                t8.start()
                t3.start()
                t2.start()
                t4.start()
                t5.start()
                t6.start()
                t7.start()
                t2.join()
            timeEnd = time.time()
            print("Tiempo por este fotograma: " + str(timeEnd - timeIni))
        timeSaved = time.strftime("%Y%m%d%H%M%S%Z", time.localtime())
        name1 = 'detected' + timeSaved + '.csv'
        name2 = 'detected' + timeSaved + 'HeadAndIndexFalse.csv'
        detected.to_csv(name1)
        detected.to_csv(name2, header=False, index=False)
except KeyboardInterrupt:
    cap.release()
    cv2.destroyAllWindows()
cap.release()
cv2.destroyAllWindows()
