import cv2
import numpy as np

cap = cv2.imread("captura1605307832.5289142.png")
frame = cap
hls = cv2.cvtColor(frame, cv2.COLOR_RGB2HLS)
h, l, s = cv2.split(hls)

cv2.imshow("original.jpg", frame)
cv2.imshow("hls.jpg", hls)
cv2.imshow("h.jpg", h)
cv2.imshow("l.jpg", l)
cv2.imshow("s.jpg", s)
k = 0
while k != 27:
    k = cv2.waitKey(1)

cv2.destroyAllWindows()
