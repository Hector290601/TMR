import cv2
import numpy

cap = cv2.VideoCapture(0)
k = 0

while True:
    ret, frame = cap.read()
    abc = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    a, b, c = cv2.split(abc)
    cv2.imshow("abc", abc)
    cv2.imshow("a", a)
    cv2.imshow("b", b)
    cv2.imshow("c", c)
    k = cv2.waitKey(0)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
