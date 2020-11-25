import cv2
import numpy

cap = cv2.VideoCapture(0)
k = 0

while cap.isOppened():
    ret, frame = cap.read()
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    r, g, b = cv2.split(rgb)
    cv2.imshow("rgb", rgb)
    cv2.imshow("r", r)
    cv2.imshow("g", g)
    cv2.imshow("b", b)
    k = cv2.waitKey(0)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()