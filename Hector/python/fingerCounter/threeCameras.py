import cv2
import freenect
import numpy as np
import imutils
laptop = cv2.VideoCapture(0)
webCam = cv2.VideoCapture(2)
#cap = cv2.VideoCapture('videoEntrada.mp4')

bgLaptop = None
bgWebCam = None
bgKinect = None

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
    frameKinect, _ = freenect.sync_get_video()
    frameKinect = cv2.cvtColor(frameKinect, cv2.COLOR_RGB2BGR)
    #if ret == False: break
    # Redimensionar la imagen para que tenga un ancho de 640
    frame1 = imutils.resize(frame1,width=640)
    frame2 = imutils.resize(frame2,width=640)
    frame3 = imutils.resize(frameKinect, width=640)
    #frame = cv2.flip(frame,1)
    frameAux1 = frame1.copy()
    frameAux2 = frame2.copy()
    frameAux3 = frame3.copy()
    cv2.imshow('kinect', frameAux3)
    cv2.imshow('frameAux1', frameAux1)
    cv2.imshow('frameAux2', frameAux2)
    k = cv2.waitKey(20)
    if k == ord('i'):
        bgLaptop = cv2.cvtColor(frameAux1, cv2.COLOR_BGR2GRAY)
        bgWebCam = cv2.cvtColor(frameAux2, cv2.COLOR_BGR2GRAY)
        bgKinect = cv2.cvtColor(frameAux3, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frameAux1bg', bgLaptop)
        cv2.imshow('frameAux2bg', bgWebCam)
        cv2.imshow('frameAux3bg', bgKinect)
    if bgLaptop is not None and bgWebCam is not None and bgKinect is not None:
        roiLaptop = frame1[50:300, 380:600]
        roiWebCam = frame2[50:300, 380:600]
        roiKinect = frame3[50:300, 380:600]
        cv2.rectangle(frame1, (380-2, 50-2), (600+2, 300+2), color_fingers)
        cv2.rectangle(frame2, (380-2, 50-2), (600+2, 300+2), color_fingers)
        cv2.rectangle(frame3, (380-2, 50-2), (600+2, 300+2), color_fingers)
        grayRoi1 = cv2.cvtColor(roiLaptop, cv2.COLOR_BGR2GRAY)
        grayRoi2 = cv2.cvtColor(roiWebCam, cv2.COLOR_BGR2GRAY)
        grayRoi3 = cv2.cvtColor(roiKinect, cv2.COLOR_BGR2GRAY)
        bgRoi1 = bgLaptop[50:300, 380:600]
        bgRoi2 = bgWebCam[50:300, 380:600]
        bgRoi3 = bgKinect[50:300, 380:600]
        dif1 = cv2.absdiff(grayRoi1, bgRoi1)
        dif2 = cv2.absdiff(grayRoi2, bgRoi2)
        dif3 = cv2.absdiff(grayRoi3, bgRoi3)
        _, th1 = cv2.threshold(dif1, 30, 255, cv2.THRESH_BINARY)
        _, th2 = cv2.threshold(dif2, 30, 255, cv2.THRESH_BINARY)
        _, th3 = cv2.threshold(dif3, 30, 255, cv2.THRESH_BINARY)
        th1 = cv2.medianBlur(th1, 7)
        th2 = cv2.medianBlur(th2, 7)
        th3 = cv2.medianBlur(th3, 7)
        cnts1, _ = cv2.findContours(th1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts2, _ = cv2.findContours(th2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts3, _ = cv2.findContours(th3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        cnts1 = sorted(cnts1, key = cv2.contourArea, reverse = True)[:1]
        cnts2 = sorted(cnts2, key = cv2.contourArea, reverse = True)[:1]
        cnts3 = sorted(cnts3, key = cv2.contourArea, reverse = True)[:1]
        for cnt in cnts1:
            M = cv2.moments(cnt)
            if M["m00"] == 0:M["m001"]=1
            x = int(M["m10"]/M["m00"])
            y = int(M["m01"]/M["m00"])
            cv2.circle(roiLaptop, tuple([x, y]), 5, (0, 255, 0), -1)
            ymin = cnt.min(axis = 1)
            cv2.circle(roiLaptop, tuple(ymin[0]), 5, color_ymin, -1)
            hull11 = cv2.convexHull(cnt)
            cv2.drawContours(roiLaptop, [hull11], 0, color_contorno, 2)
            hull12 = cv2.convexHull(cnt, returnPoints = False)
            defects = cv2.convexityDefects(cnt, hull12)
            if defects is not None:
                inicio = []
                fingers = []
                for i in range(defects.shape[0])
        cv2.imshow('roiLaptop', roiLaptop)
        cv2.imshow('roiWebCam', roiWebCam)
        cv2.imshow('roiKinect', roiKinect)
    if k == 27:
        break

laptop.release()
webCam.release()
cv2.destroyAllWindows()

