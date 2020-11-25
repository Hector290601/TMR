import cv2
import numpy as np

cap = cv2.imread("captura1605307832.5289142.png")

frame = cap

rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)

r, g, b = cv2.split(rgb)

cv2.imshow("rgb", rgb)
cv2.imshow("r", r)
cv2.imshow("g", g)
cv2.imshow("b", b)

k = 0

while k != 27:
    k = cv2.waitKey(1)

cv2.destroyAllWindows()
