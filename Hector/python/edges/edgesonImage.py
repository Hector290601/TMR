# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 23:51:22 2020

@author: hrmha
"""

import cv2
import numpy as np

cap = cv2.imread('degradadoMax.png')
h, _, _ = cap.shape
maxb = np.array([175, 8, 165])
minb = np.array([96, 3, 20])
frame = cap[int(h / 2.1) :]
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, minb, maxb)
gray = cv2.GaussianBlur(frame, (7, 7), 3)
blur = cv2.cvtColor(gray, cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(blur, 25, 75)
edgesOnMask = cv2.Canny(mask, 50, 150, apertureSize = 7)
a, g= edgesOnMask.shape
maskpfrm = cv2.bitwise_and(frame, frame, mask = mask)
maskpedgs = cv2.bitwise_and(edge, edge, mask = mask)
t, dst = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)
edges, _ = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.imwrite('orginal.jpeg', frame)
for c in edges:
    area = cv2.contourArea(c)
    if area > 100 and area < 10000 and area in mask:
        cv2.drawContours(frame, [c], 0, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imwrite('areas.jpeg', frame)
cv2.imwrite('cannyEdge.jpeg', edge)
cv2.imwrite('hsv.jpeg', hsv)
cv2.imwrite('whites.jpeg', mask)
cv2.imwrite('whitesAndFrame.jpeg', maskpfrm)
cv2.imwrite('whitesAndEdges.jpeg', maskpedgs)
cv2.imwrite('edgesOnMask.jpeg', edgesOnMask)
