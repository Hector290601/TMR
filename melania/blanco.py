import cv2
import numpy as np
nImagen = 255*np.ones((50,50,3), dtype=np.uint8)
hsvBlanco = cv2.cvtColor(nImagen, cv2.COLOR_BGR2HSV)
print('hsvBlanco= ', hsvBlanco)
cv2.imshow('nImagen', nImagen)
cv2.imshow('hsvBlanco', hsvBlanco)
cv2.waitKey(0)