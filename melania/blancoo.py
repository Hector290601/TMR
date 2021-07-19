import cv2
import numpy as np

cap = cv2.VideoCapture(0)

<<<<<<< HEAD
blancoAlto=np.array([255,255,255])
blancoBajo=np.array([222,219,219])
=======
blancoBajo=np.array([100,100,100])
blancoAlto=np.array([222,255,255])
>>>>>>> 046dcd121e3e93fdcab680b316052be59d57cb05

while True:
    ret, frame = cap.read()
    if ret ==True:
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frameHSV,blancoAlto,blancoBajo)
        cv2.imshow("Solo blanco", mask)
        cv2.imshow("frame", frame)

    if cv2.waitKey(1) == 27:
       break
cap.release()
cv2.destroyAllWindows()#no recibe parametro
