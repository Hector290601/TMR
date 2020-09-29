import cv2
import numpy as np
import imutils
import os
import time

Datos = 'n'
if not os.path.exists(Datos):
    print('Carpeta creada: ',Datos)
    os.makedirs(Datos)
cap = cv2.VideoCapture(0)
x1, y1 = 0, 80
x2, y2 = 620, 400
while cap.isOpened():
    count = time.strftime("%Y%m%d%H%M%S%Z", time.localtime())
    ret, frame = cap.read()
    if ret == False:
        break
    imAux = frame.copy()
    cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)
    objeto = imAux[y1:y2,x1:x2]
    objeto = imutils.resize(objeto,width=38)
    #print(objeto.shape)
    k = cv2.waitKey(1)
    if k == ord('s'):
        svd = cv2.imwrite(Datos+'/objeto_{}.jpg'.format(count),objeto)
        if svd:
            print('Imagen guardada:' + Datos +'/objeto_{}.jpg'.format(count))
        else:
            print("Un error ha ocurrido")
    if k == 27:
        break
    cv2.imshow('frame',frame)
    cv2.imshow('objeto',objeto)
cap.release()
cv2.destroyAllWindows()
