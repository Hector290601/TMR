import cv2
import numpy as np
import math

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
    leftFit = [] #lista para almacenar los valores de la recta izquierda
    rightFit = [] #lista para almacenar los valores de la recta derecha
    for line in interceptLines: #itera en los valores de la recta
        x1, y1, x2, y2 = line.reshape(4) #obtiene las coordenadas de inicio y final de cada recta
        parameters = np.polyfit((x1, x2), (y1, y2), 1) #optimiza la ecuación de la recta
        slope = parameters[0] #separa el primer valor de los parámetros
        intercept = parameters[1] #separa el primer valor de los parámetros
        if slope < 0: #este if es para saber si está a la izquierda o derechga del centro
            leftFit.append((slope, intercept))
        else:
            rightFit.append((slope, intercept))
    leftFitAverage = np.average(leftFit, axis = 0) #unifica los valores de las rectas izquierdas
    rightFitAverage = np.average(rightFit, axis = 0) #unifica los valores de las rectas izquierdas
    leftLine = makeCoordinates(interceptImage, leftFitAverage) #obtiene las ecuaciones de cada recta (izquierda)
    rightLine = makeCoordinates(interceptImage, rightFitAverage) #obtiene las ecuaciones de cada recta (izquierda)
    return np.array([leftLine, rightLine])

def makeCoordinates(coordinatesImage, lineParameters):
    print("lineParameters: ", lineParameters)
    isNan = math.isnan(lineParameters[0])
    print(isNan)
    isNan = math.isnan(lineParameters[1])
    print(isNan)
    try:
        slope, intercept = lineParameters #intercept es la ordenada al origen de la recta
        y1 = coordinatesImage.shape[0] #obtiene el valor '0' de la imagen
        y2 = int(y1*(3/5)) #esto es pra determinar el largo de la recta que dibuja en la imagen
        x1 = int((y1 - intercept)/slope) #obtiene la ecuación de la recta con el primer punto
        x2 = int((y2 - intercept) / slope) # obtiene la ecuación de la recta con el segundo punto
        print(type(lineParameters))
        return np.array([x1, y1, x2, y2])
    except:
        return np.array([0, 0, 0, 0])

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
        cap = cv2.VideoCapture(0)
        while cap.isOpened():
            ret, origFrame = cap.read()
            
            coppiedFrame = np.copy(origFrame)
            
            gray = cv2.cvtColor(origFrame, cv2.COLOR_BGR2GRAY)
            canny = cannyImage(gray)
            croppedImage = regionOfInterest(canny)
            colorInRange = colorRange(coppiedFrame, gray, croppedImage)
            lines = cv2.HoughLinesP(colorInRange, 1, np.pi/180, 50, minLineLength=20, maxLineGap=50)
            #print(lines)
            #left = range(0, 480 // 2)
            #right = range(480 // 2, 480)
            if lines is not None:
                averagedLines =  averagedSlopeIntercept(coppiedFrame, lines)
                lineImage = displayLines(coppiedFrame, averagedLines)
                for line in lines:
                    x1, y1, x2, y2 = line[0]
                    #cv2.rectangle(coppiedFrame, (x1, y1), (x2, y2), (0, 255, 0), 5)
                    cv2.line(coppiedFrame, (x1, y1), (x2, y2), (0, 255, 0), 5)
            if cv2.waitKey(25) & 0xFF == ord('s'):
                break
            
            cv2.imshow("origFrame", origFrame)
            cv2.imshow("coppiedFrameWithLines", coppiedFrame)
            if lines is not None:
                cv2.imshow("lineImage", lineImage)
            
            #cv2.imshow("lines", lines)
        cap.release()
        cv2.destroyAllWindows()
    except:
        print("Algo malo ha ocurrido!")
