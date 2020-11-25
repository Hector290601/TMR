#-*- coding:utf-8 -*-

import cv2
import numpy as np

"""
PASOS:
    img -> HSL
    HSL -> Gray
    mask yellow and blue to gray
    Gausian blur
    Canny edge
    crop image
    hough lines
"""

cap = cv2.imread("cero.jpeg")

frame = cap
hls = cv2.cvtColor(frame, cv2.COLOR_RGB2HLS)
_, _, gray = cv2.split(hls)

maskYellowMax = np.array([233, 139, 98])
maskYellowMin = np.array([193, 115, 98])
maskWitheMax = np.array([255, 239, 106])
maskWitheMin = np.array([62, 173, 99])
maskGrayMax = np.array(255)
maskGrayMin = np.array(250)

yellowMask = cv2.inRange(hls, maskYellowMin, maskYellowMax)
witheMask = cv2.inRange(hls, maskWitheMin, maskWitheMax)
grayMask = cv2.inRange(gray, maskGrayMin, maskGrayMax) #esta es la máscara qe mejor funciona

blur = cv2.GaussianBlur(grayMask, (5, 5), cv2.BORDER_DEFAULT)

edges = cv2.Canny(blur, 100, 200, 3)

h, w = edges.shape
crop = edges[int(h/2) : ]

lines = cv2.HoughLines(edges, 1, np.pi/180, 20)
copy = frame

#for i in range(20):
print(type(lines))
print(lines)
for r, t in lines[0]:
    a = np.cos(t)
    b = np.sin(t)
    x0 = a*r
    y0 = b*r
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))
    cv2.line(copy, (x1, y1), (x2, y2), (0, 0, 0), 1)

cv2.imwrite("original.jpg", frame)
cv2.imwrite("hsl.jpg", hls)
cv2.imwrite("gray.jpg", gray)
#cv2.imwrite("yellowLines.jpg", yellowMask)
#cv2.imwrite("whiteLines.jpg", witheMask)
cv2.imwrite("grays.jpg", grayMask)
cv2.imwrite("gaussianBlur.jpg", blur)
cv2.imwrite("canny.jpg", edges)
#cv2.imwrite("crop.jpg", crop)
cv2.imwrite("lines.jpg", copy)
