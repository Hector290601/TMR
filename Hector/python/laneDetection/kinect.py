import cv2
import freenect
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
    deltaTime = time.time() - startTime
    if isNanLeft:
        print('L')
        #detected.loc[len(detected)]=['L', leftFitAverage, rightFitAverage, leftLine, rightLine, slopeLeft, interceptLeft, slopeRight, interceptRight]
    elif isNanRight:
        print('R')
        #detected.loc[len(detected)]=['R', leftFitAverage, rightFitAverage, leftLine, rightLine, slopeLeft, interceptLeft, slopeRight, interceptRight]
    else:
        detected.loc[len(detected)]=['C', leftFitAverage, rightFitAverage, leftLine, rightLine, slopeLeft, interceptLeft, slopeRight, interceptRight]
    return np.array([leftLine, rightLine]), isNanLeft, isNanRight

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

def displayLines(displayImage, displayLinesVar):
    lineImage = np.zeros_like(displayImage)#obtiene un arreglo de ceros de las mismas características de la imagen
    if displayLinesVar is not None: #verifica que existan líneas
        for x1, y1, x2, y2 in displayLinesVar: #itera en cada línea
            #x1, y1, x2, y2 = line.shape()
            #print(lines.shape, 'Shapes on the line')
            #print(lines, 'lines')
            #print(x1, 'x1', y1, 'y1', x2, 'x2', y2, 'y2')
            try: #evita que el programa falle si no hay líneas
                cv2.line(lineImage, (x1, y1), (x2, y2), (255, 255, 255), 3) #dibuja una línea azul en las líneas
            except:
                lineImage = lineImage #regresa una matriz de ceros
    return lineImage

if __name__ == '__main__':
    try:
        #cap = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        while True:
            #os.system("clear")
            #ret, origFrame = cap.read()
            #origFrame, _ = freenect.sync_get_video(0, freenect.VIDEO_IR_10BIT)
            origFrame, _ = freenect.sync_get_video()
            #np.clip(origFrame, 0, 2**10-1, origFrame)
            #origFrame >>=2
            #origFrame = origFrame.astype(np.uint8)
            origFrame = cv2.cvtColor(origFrame,cv2.COLOR_RGB2BGR)
            coppiedFrame = np.copy(origFrame)
            hsvFrame = cv2.cvtColor(origFrame,cv2.COLOR_BGR2HSV)
            origFrame = hsvFrame
            gray = cv2.cvtColor(origFrame, cv2.COLOR_BGR2GRAY)
            canny = cannyImage(gray)
            croppedImage = regionOfInterest(canny)
            colorInRange = colorRange(coppiedFrame, gray, croppedImage)
            lines = cv2.HoughLinesP(colorInRange, 1, np.pi/180, 50, minLineLength=20, maxLineGap=50)
            #print(lines)
            #left = range(0, 480 // 2)
            #right = range(480 // 2, 480)
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
                    #cv2.rectangle(coppiedFrame, (x1, y1), (x2, y2), (0, 255, 0), 5)
                    cv2.line(coppiedFrame, (x1, y1), (x2, y2), (0, 255, 0), 5)
            if cv2.waitKey(25) & 0xFF == ord('s'):
                break
            #cv2.imshow("origFrame", origFrame)
            #salida.write(coppiedFrame)
            cv2.imshow("coppiedFrameWithLines", coppiedFrame)
            #if lines is not None:
            #    cv2.imshow("lineImage", lineImage)
            
            #cv2.imshow("lines", lines)
        #print(detected)
        timeSaved = time.strftime("%Y%m%d%H%M%S%Z", time.localtime())
        name1 = 'detected' + timeSaved + '.csv'
        name2 = 'detected' + timeSaved + 'HeadAndIndexFalse.csv'
        detected.to_csv(name1)
        detected.to_csv(name2, header=False, index=False)
        cap.release()
        cv2.destroyAllWindows()
    except:
        print("Algo malo ha ocurrido!")
