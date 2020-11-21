import cv2
import numpy
cap= cv2.VideoCapture(0)
k=0
while cap.isOpened():
    ret, frame= cap.read()#descomprimir imagen
    gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Carril", gray)
    
    k=cv2.waitKey(0)#0 porque es en vivo
    if k==27:#esc
        break
cap.release()#va a liberar la camara
cv2.destroyAllWindows()#no recibe parametr
    

    
 