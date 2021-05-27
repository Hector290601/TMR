#-*- coding: utf-8 -*-

import cv2  #importar openCV
import numpy as np  #importar numpy
import os   #import al sistema
from datetime import datetime   #importar la fecha

name = "tercero"    #cambiar al nombre del archivo de video
ext = "mp4" #cambiar a la extención del video
vdo = cv2.VideoCapture(name + '.' + ext)    #lee el video

try:    #evitar que falle si ya existe un folder con ese nombre
    os.makedirs("G:\\Mi unidad\\TMR\\DataSets\\" + name)    #crear un folder con el nombre
    print("Directory ", name, " Created ")  #avisar al usuario que se creó el folder
except FileExistsError: #aquí ya existía el folder
    print("Directory ", name, " already exists")    #notifica que ya existe

while vdo.isOpened():   #valida que el video siga activo
    ret, frame = vdo.read() #lee un fotograma del video
    if ret == True: #leyó el video correctamente
        """
        #   puntos auxiliares
        """
        # image = cv2.circle(frame, (600, 330), 10, color=(0, 0, 255))  #arriba izquierda
        # image = cv2.circle(frame, (600, 600), 10, color=(0, 0, 255))   #abajo izquierda
        # image = cv2.circle(frame, (1420, 600), 10, color=(0, 0, 255))   #abajo derecha
        # image = cv2.circle(frame, (1420, 330), 10, color=(0, 0, 255))   #arriba derecha
        #   crea la zona de interés
        poly = np.array([
            [600, 330],
            [600, 600],
            [1450, 600],
            [1450, 330],
        ])
        image = cv2.polylines(frame, [poly], True, (255, 255, 255), 1)  #dibuja la zona de interés en el video principal
        # interes = frame[330:600, 600:1420]
        interes = frame[poly[0][1]:poly[0][0], poly[0][0]:poly[3][0]]   #recrota la imagen
        now = datetime.now()    #obtiene la fecha
        cv2.imwrite('G:\\Mi unidad\\TMR\\DataSets\\' + name + '\\lanes' + str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '-' + str(now.hour) + '-' + str(now.minute) + '-' + str(now.second) + '-'  + str(now.microsecond) + '.png',interes)   #guarda la imagen
        cv2.imshow("video", image)  #muestra la imagen original
        cv2.imshow("interes", interes)  #muestra la imagen que se guardará o de interés
        #cierra el programa
        k = 0
        k = cv2.waitKey(1)
        if k == 27:
            break

vdo.release()
cv2.destroyAllWindows()