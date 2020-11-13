#-*- coding: utf-8 -*-

import cv2 #módulo para la visión computacional
import numpy as np #módulo para el manejo de arreglos
import time #esto sólo se usa pra guardar fotografías para prueba

def makeCoordinates(image, lineParameters):
    print("lineParameters: ", lineParameters)
    try:
        slope, intercept = lineParameters #intercept es la ordenada al origen de la recta
        y1 = image.shape[0] #obtiene el valor '0' de la imagen
        y2 = int(y1*(3/5)) #esto es pra determinar el largo de la recta que dibuja en la imagen
        x1 = int((y1 - intercept)/slope) #obtiene la ecuación de la recta con el primer punto
        x2 = int((y2 - intercept) / slope) # obtiene la ecuación de la recta con el segundo punto
        return np.array([x1, y1, x2, y2])
    except:
        return np.array([0, 0, 0, 0])

def averagedSlopeIntercept(image, lines):
    leftFit = [] #lista para almacenar los valores de la recta izquierda
    rightFit = [] #lista para almacenar los valores de la recta derecha
    for line in lines: #itera en los valores de la recta
        x1, y1, x2, y2 = line.reshape(4) #obtiene las coordenadas de inicio y final de cada recta
        parameters = np.polyfit((x1, x2), (y1, y2), 1) #optimiza la ecuación de la recta
        print(parameters)
        slope = parameters[0] #separa el primer valor de los parámetros
        intercept = parameters[1] #separa el primer valor de los parámetros
        if slope < 0: #este if es para saber si está a la izquierda o derechga del centro
            leftFit.append((slope, intercept))
        else:
            rightFit.append((slope, intercept))
    leftFitAverage = np.average(leftFit, axis = 0) #unifica los valores de las rectas izquierdas
    rightFitAverage = np.average(rightFit, axis = 0) #unifica los valores de las rectas izquierdas
    leftLine = makeCoordinates(image, leftFitAverage) #obtiene las ecuaciones de cada recta (izquierda)
    rightLine = makeCoordinates(image, rightFitAverage) #obtiene las ecuaciones de cada recta (izquierda)
    return np.array([leftLine, rightLine])

"""def colorSet(image, gray):
    maskWitheMax = np.array([255])
    maskWitheMin = np.array([150])
    maskBlackMax = np.array([10])
    maskBlackMin = np.array([0])
    maskWithe = cv2.inRange(gray, maskWitheMin, maskWitheMax)
    maskBlack = cv2.inRange(gray, maskBlackMin, maskBlackMax)
    mask = cv2.bitwise_or(maskWithe, maskBlack)
    maskColors = cv2.bitwise_and(image, image, maks = mask)
    cv2.imwrite("maskColors.jpg", maskColors)
    #cv2.waitKey(0)
    return maskColors
"""
def canny(image, gray):
    blur = cv2.GaussianBlur(gray, (5, 5), 0) #elimina el ruido en la imagen
    canny = cv2.Canny(blur, 10, 150) #encuentra las rectas mediante los valores de las derivadas de cada pixel
    return canny

def displayLines(image, lines):
    lineImage = np.zeros_like(image) #obtiene un arreglo de ceros de las mismas características de la imagen
    if lines is not None: #verifica que existan líneas
        for x1, y1, x2, y2 in lines: #itera en cada línea
            #x1, y1, x2, y2 = line.shape()
            #print(lines.shape, 'Shapes on the line')
            #print(lines, 'lines')
            #print(x1, 'x1', y1, 'y1', x2, 'x2', y2, 'y2')
            try: #evita que el programa falle si no hay líneas
                cv2.line(lineImage, (x1, y1), (x2, y2), (255, 255, 255), 1) #dibuja una línea azul en las líneas
            except:
                lineImage = lineImage #regresa una matriz de ceros
    return lineImage

def regionOfInterest(image):
    y, x = image.shape #obtiene las medidas de la imagen
    #polygons = np.array([[(0, 0), (144, 320), (288, 640)]])
    #polygons = np.array([[(390, 360), (730, 380), (600, 271)]])
    #polygons = np.array([[(150, 172), (357, 182), (339, 138)]])#para el video, ambos valores se vividen entre 2.02
    #polygons = np.array([[(170, 330), (570, 350), (370, 171)]])
    #polygons = np.array([[(0, 300), (280, 180), (640, 335)]]) #polígono en donde busca los carriles
    #polygons = np.array([[(0, 384), (0, 300), (240, 180), (340, 180), (640, 335), (640, 400)]])
    #polygons = np.array([[(0, 350), (0, 398), (640, 398), (500, 250), (155, 250)]]) #este es el bueno
    #polygons = np.array([[(0, 400), (640, 400), (640, 250), (0, 250)]])
    polygons = np.array([[(0, 400), (640, 400), (640, 240), (0, 240)]])
    #polygons = np.array([[(40, 420), (640, 420), (295, 220)]])
    #polygons = np.array([[(197, 177), (354, 182), (302, 133)]])
    #polygons = np.array([[(670, 0), (y//2, x//2), (670, 270)]])
    mask = np.zeros_like(image) #crea un arreglo de ceros con las mismas características de la imagen
    cv2.fillPoly(mask, polygons, 255) #obtiene todas las áreas dentro del polígono
    maskedImage = cv2.bitwise_and(image, image, mask = mask) #compara mediante operaciones booleanas si coinciden las líneas que encontró con el polígono
    return maskedImage

def color(frame, gray, cropped):
    #image = np.copy(frame)
    whitesMax = np.array([255, 255, 255]) #rángo máximo de colores blancos
    #whitesMin = np.array([150, 150, 150]) #rángo mínimo de colores blancos
    #yellowMax = np.array([204, 214, 228]) #rángo máximo de colores amarillos
    yellowMin = np.array([79, 73, 57]) #rángo mínimo de colores amarillos
    color = cv2.bitwise_or(frame, frame, mask = cropped) #combina las máscaras usando como argumento la zona de interés (para que sólo busque el color en la zona de interés)
    msk = cv2.inRange(color, yellowMin, whitesMax) #busca el color en la zona de interés
    return msk

cap = cv2.VideoCapture(0) #importa el video o abre la imagen de la cámara
salida = cv2.VideoWriter('videoSalida.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(int(cap.get(3)),int(cap.get(4)))) #guarda el video procesado en un video externo
prueba = cv2.VideoWriter('videoTest.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(int(cap.get(3)),int(cap.get(4)))) #guarda el video sin procesar en un video externo
try:
    while cap.isOpened():
        try:
            _, image = cap.read() #obtiene cada fotograma por separado
            laneIMage = np.copy(image) #crea una copia de la imagen para evitar que se pueda alterar la original
            gray = cv2.cvtColor(laneIMage, cv2.COLOR_BGR2GRAY) #cambia el espacio de color a gama de grises
            cannyImage = canny(laneIMage, gray) #obtiene los contornos
            croppedImage = regionOfInterest(cannyImage) #recorta la imagen en el área de interés
            colorZone = color(laneIMage, gray, croppedImage) #discrimina los pixeles que no entren al rango de color 
            lines = cv2.HoughLinesP(colorZone, 2, np.pi / 180, 100, np.array([]), minLineLength = 1, maxLineGap = 40) #busca las líneas, los últimos dos valores definen el grosor mínimo y la distancia entre pixeles máxima, respectivamente
            if lines is not None: #verifica que existan líneas
                averagedLines =  averagedSlopeIntercept(laneIMage, lines) #optimiza las líneas
                #print(averagedLines)
                mI1, mI2, _ = image.shape #obtiene las medidas de la imagen
                l1y1, l1x1, l1y2, l1x2 = averagedLines[0] #obtiene los puntos de la primera línea
                l2y1, l2x1, l2y2, l2x2 = averagedLines[1] #obtiene los puntos de la segunda línea
                mx1 = (l1x1 + l2x1)//2 #obtiene el centro de los primeros puntos de ambas líneas
                mx2 = (l2x2 + l2x2)//2 #obtiene el centro de los últimps puntos de ambas líneas
                mx3 = (mx1 + mx2) // 2 #obtiene el promedio de los puntos antes obtenidos
                my1 = (l1y1 + l2y1)//2 #obtiene el centro de los primeros puntos de ambas líneas
                my2 = (l2y2 + l2y2)//2 #obtiene el centro de los segundos puntos de ambas líneas
                my3 = (my1 + my2) // 2 #obtiene el promedio de los puntos antes obtenidos
                #print(mx2, my1)
                if (l1x2 - l1x1) != 0: #evita divisiones entre 0
                    mI = (l1y2 - l1y1) / (l1x2 - l1x1) #obtiene la pendiente de la primera recta
                    #print('mI: ', mI)
                if (l2x2 - l2x1) != 0: #evita divisiones entre 0
                    mD = (l2y2 - l2y1) / (l2x2 - l2x1) #obtiene la pendiente de la segunda recta
                    #print('mD: ', mD)
                cv2.line(laneIMage, (my1, 0), (my1, 300), (0, 0, 0), 1) #dibuja una línea
                #cv2.line(laneIMage, (mx2, 0), (mx2, 300), (255, 0, 0), 1) #dibuja una línea
                delta = 288 - my1 #obtiene la desviación del centro de la imagen al centro de los carriles
                if delta <= 30 and delta >= -30: #establece los rangos de cada lado
                    print('recta')
                elif delta < -30:
                    print('izquierda')
                else:
                    print('derecha')
                #cv2.line(laneIMage, (mx3, 0), (mx3, 300), (0, 255, 0), 1) #dibuja una línea
                cv2.line(laneIMage, ((620//2), 0), ((620//2), 300), (0, 0, 255), 1) #dibuja una línea
                #cv2.line(laneIMage, (my2, 0), (my2, 300), (255, 255, 0), 1) #dibuja una línea
                #cv2.line(laneIMage, (my3, 0), (my3, 300), (255, 255, 255), 1) #dibuja una línea
                #cv2.line(laneIMage, (mI2//2, 0), (mI2//2, 300), (255, 255, 255), 10) #dibuja una línea
                #cv2.line(laneIMage, (mI2//2, 0), (mI2//2, 300), (255, 255, 255), 10) #dibuja una línea
                #cv2.line(laneIMage, (288, 0), (288, 300), (0, 255, 0), 10) #dibuja una línea
                lineImage = displayLines(laneIMage, averagedLines) #muestra las líneas que se obtuvieron anteriormente
                comboImage = cv2.addWeighted(laneIMage, 0.8, lineImage, 1, 1) #combina ambas imágenes (la de las líneas y la original)
                cv2.imshow("resultado", comboImage) #muestra la imagen
                #print(lines)
            if cv2.waitKey(1) & 0xFF == ord('s'): #esto es para salir
                break
            salida.write(comboImage) #esribe el vídeo procesado
        except:
            cv2.imshow("resultado", colorZone) #muestra la imagen aunque no temga líneas
            salida.write(image) #escribe el vídeo aunque no tenga líneas
            if cv2.waitKey(1) & 0xFF == ord('s'): #esto es para salir
                break
            #print(ValueError)
            #break
            salida.write(colorZone) #esribe el vídeo procesado
        prueba.write(image) #esribe el vídeo procesado
        if cv2.waitKey(1) & 0xFF == ord('f'): # esto sirve para captrar imágenes para muestra
            name = 'capture' + str(time.time()) + '.png' #crea un nombre de imagen único para cada una
            cv2.imwrite(name, image) #escribe la imagen en disco
except:
    print("bueno bai")
"""
image = cv2.imread("test.png")
#_, image = cap.read()
laneIMage = np.copy(image)
gray = cv2.cvtColor(laneIMage, cv2.COLOR_BGR2GRAY)
cannyImage = canny(laneIMage, gray)
croppedImage = regionOfInterest(cannyImage)
colorZone = color(laneIMage, gray, croppedImage)
lines = cv2.HoughLinesP(colorZone, 2, np.pi / 180, 10, np.array([]), minLineLength = 10, maxLineGap = 5)
if lines is not None:
    averagedLines =  averagedSlopeIntercept(laneIMage, lines)
    l1y1, l1x1, l1y2, l1x2 = averagedLines[0]
    l2y1, l2x1, l2y2, l2x2 = averagedLines[1]
    print('Linea 1: ', l1x1, ',', l1y1, ';', l1x2, ',', l1y2)
    print('Linea 2: ', l2x1, ',', l2y1, ';', l2x2, ',', l2y2)
    mI1, mI2, _ = image.shape
    mx1 = (l1x1 + l2x1)//2
    mx2 = (l2x2 + l2x2)//2
    mx3 = (mx1 + mx2) // 2
    print(mx1, mx2, mx3)
    #cv2.line(laneIMage, (mx1, 0), (mx1, 300), (0, 255, 0), 10)
    cv2.line(laneIMage, (mx2, 0), (mx2, 300), (0, 0, 0), 10)
    #cv2.line(laneIMage, (mx3, 0), (mx3, 300), (255, 255, 255), 10)
    #cv2.line(laneIMage, (mI1//2, 0), (mI1//2, 300), (255, 0, 0), 10)
    #cv2.line(laneIMage, (mx1, my1), (mx2, my2), (0, 255, 0), 10)
    lineImage = displayLines(laneIMage, averagedLines)
    comboImage = cv2.addWeighted(laneIMage, 0.8, lineImage, 1, 1)
    #salida.write(comboImage)
    cv2.imshow("resultado", comboImage)
else:
    print('algo ha ocurrido!')
    print(lines)
cv2.imshow('laneImage:', laneIMage)
cv2.imshow('gray:', gray)
cv2.imshow('cannyImage:', cannyImage)
cv2.imshow('croppedImage:', croppedImage)
cv2.imshow('color:', colorZone)
cv2.waitKey(0)
"""
cap.release()
salida.release()
cv2.destroyAllWindows()
#todos los prints son para uso de debug
