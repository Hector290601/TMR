import cv2
import numpy as np
import freenect

def cannyImage(cannyGray):
    cannyBlur = cv2.GaussianBlur(cannyGray, (5, 5), 0)
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
    colorRanged = cv2.inRange(colorFrame, colorMin, colorMax)
    return colorRanged

def main():
    while cap.isOpened():
        #ret, origFrame = cap.read()
        kinectFrame, _ = freenect.sync_get_video()
        origFrame = cv2.
        coppiedFrame = np.copy(origFrame)
        gray = cv2.cvtColor(origFrame, cv2.COLOR_BGR2GRAY)
        canny = cannyImage(gray)
        croppedImage = regionOfInterest(canny)
        colorInRange = colorRange(coppiedFrame, gray, croppedImage)
        canny = cannyImage(colorInRange)
        colorColor = cv2.bitwise_and(colorInRange, colorInRange, mask = croppedImage)
        cv2.imshow('Frame', colorInRange)
        cv2.imshow('canny', canny)
        #cv2.imshow('kinectframe', kinectFrame)
        #cv2.imshow('colors', whites)
        k = cv2.waitKey(1)
        if k == 27:
            break

if __name__ == '__main__':
    cap = cv2.VideoCapture(0)
    k = 0
    main()
    cap.release()
    cv2.destroyAllWindows()

