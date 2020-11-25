import numpy as np
import cv2

src = cv2.imread('uno.jpeg')

gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 3)

t, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_TRIANGLE)

contours, _ = cv2.findContours(dst, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for c in contours:
    area = cv2.contourArea(c)
    if area > 1000 and area < 10000:
        cv2.drawContours(src, [c], 0, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow('contornos', src)
cv2.imshow('umbral', dst)

cv2.waitKey(0)
