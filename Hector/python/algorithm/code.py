import cv2
import numpy

cap = cv2.VideoCapture(0)
k = 0

while cap.isOpened():
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Frame', frame)
    cv2.imshow('Gray', gray)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()

