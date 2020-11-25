import cv2
import numpy as np
import imutils
laptop = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('videoEntrada.mp4')

bgLaptop = None

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
    ret, frame1 = laptop.read()
    ret, frame2 = webCam.read()
    # Redimensionar la imagen para que tenga un ancho de 640
    frame1 = imutils.resize(frame1,width=640)
    #frame = cv2.flip(frame,1)
    frameAux1 = frame1.copy()
    cv2.imshow('kinect', frameAux3)
    k = cv2.waitKey(20)
    if k == ord('i'):
        bgLaptop = cv2.cvtColor(frameAux1, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frameAux1bg', bgLaptop)
    if bgLaptop is not None and bgWebCam is not None and bgKinect is not None:
        roiLaptop = frame1[50:300, 380:600]
        cv2.rectangle(frame1, (380-2, 50-2), (600+2, 300+2), color_fingers)
        grayRoi1 = cv2.cvtColor(roiLaptop, cv2.COLOR_BGR2GRAY)
        bgRoi1 = bgLaptop[50:300, 380:600]
        dif1 = cv2.absdiff(grayRoi1, bgRoi1)
        _, th1 = cv2.threshold(dif1, 30, 255, cv2.THRESH_BINARY)
        th1 = cv2.medianBlur(th1, 7)
        cv2.imshow('th1', th1)
    if k == 27:
        break

laptop.release()
webCam.release()
cv2.destroyAllWindows()

