#-*- coding:utf-8 -*-

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

kernel = np.ones((5, 5), np.uint8)

while cap.isOpened():
    ret, frame = cap.read()
    greenMax = np.array([50, 255, 50]) #BGR
    greenMin = np.array([0, 51, 0])
    mask = cv2.inRange(frame, greenMin, greenMax)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    x, y, w, h = cv2.boundingRect(opening)
    cv2.rectangle(frame, (x, y), (x + w, y + y), (0, 255, 0), 3)
    print(x+w/2, y+h/2)
    cv2.imshow('results', frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()