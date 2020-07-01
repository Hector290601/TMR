#-*- coding: utf-8 -*-

import cv2
import numpy as np
import matplotlib.pyplot as plt

def makeCoordinates(image, lineParameters):
    slope, intercept = lineParameters
    y1 = image.shape[0]
    y2 = int(y1*(3/5))
    x1 = int((y1 - intercept)/slope)
    x2 = int((y2 - intercept) / slope)
    return np.array([x1, y1, x2, y2])


def averagedSlopeIntercept(image, lines):
    leftFit = []
    rightFit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0:
            leftFit.append((slope, intercept))
        else:
            rightFit.append((slope, intercept))
    leftFitAverage = np.average(leftFit, axis = 0)
    rightFitAverage = np.average(rightFit, axis = 0)
    leftLine = makeCoordinates(image, leftFitAverage)
    rightLine = makeCoordinates(image, rightFitAverage)
    return np.array([leftLine, rightLine])


def canny(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny


def displayLines(image, lines):
    lineImage = np.zeros_like(image)
    if lines is not None:
        for x1, y1, x2, y2 in lines:
            cv2.line(lineImage, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return lineImage


def regionOfInterest(image):
    y, x = image.shape
    #polygons = np.array([[(0, 0), (144, 320), (288, 640)]])
    #polygons = np.array([[(390, 360), (730, 380), (600, 271)]])
    polygons = np.array([[(193, 177), (361, 187), (297, 133)]])#para el vide, ambos valores se vividen entre 2.02
    #polygons = np.array([[(670, 0), (y//2, x//2), (670, 270)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    maskedImage = cv2.bitwise_and(image, mask)
    return maskedImage


"""
image = cv2.imread('equis.png')
print(image.shape)
laneIMage = np.copy(image)
cannyImage = canny(laneIMage)
croppedImage = regionOfInterest(cannyImage)
lines = cv2.HoughLinesP(croppedImage, 2, np.pi / 180, 10, np.array([]), minLineLength = 10, maxLineGap = 5)
averagedLines =  averagedSlopeIntercept(laneIMage, lines)
lineImage = displayLines(laneIMage, averagedLines)
comboImage = cv2.addWeighted(laneIMage, 0.8, lineImage, 1, 1)
plt.imshow(comboImage)
plt.show()
"""
cap = cv2.VideoCapture("video.mp4")

while(cap.isOpened()):
    ret, frame = cap.read()
    print(frame.shape)
    cannyImage = canny(frame)
    croppedImage = regionOfInterest(cannyImage)
    lines = cv2.HoughLinesP(croppedImage, 2, np.pi / 180, 50, np.array([]), minLineLength = 40, maxLineGap = 5)
    averagedLines =  averagedSlopeIntercept(frame, lines)
    lineImage = displayLines(frame, averagedLines)
    comboImage = cv2.addWeighted(frame, 0.8, lineImage, 1, 1)
    cv2.imshow("results", comboImage)
    cv2.waitKey(1)
