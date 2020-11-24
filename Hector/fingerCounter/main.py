import cv2
import freenect
import numpy as np
import imutils
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('videoEntrada.mp4')

bg = None

# COLORES PARA VISUALIZACIÓN
color_start = (204,204,0)
color_end = (204,0,204)
color_far = (255,0,0)
color_start_far = (204,204,0)
color_far_end = (204,0,204)
color_start_end = (0,255,255)
color_contorno = (0,255,0)
color_ymin = (0,130,255) # Punto más alto del contorno

#color_angulo = (0,255,255)
#color_d = (0,255,255)

color_fingers = (0,255,255)

while True:
    ret, frame = cap.read()
    frameKinect, _ = freenect.sync_get_video()
    frameKinect = cv2.cvtColor(frameKinect, cv2.COLOR_RGB2BGR)
    #if ret == False: break
    # Redimensionar la imagen para que tenga un ancho de 640
    frame = imutils.resize(frame,width=640)
    kinect = imutils.resize(frameKinect, width=640)
    #frame = cv2.flip(frame,1)
    frameAux = frame.copy()
    cv2.imshow('kinect', kinect)
    cv2.imshow('frameAux', frameAux)
    k = cv2.waitKey(20)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

