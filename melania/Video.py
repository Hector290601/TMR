import cv2
import numpy

cap=cv2.VideoCapture(0)#id de mi camara es 0\\
k=0#tecla de key
while cap.isOpened():#mientras este abierto
    #_desperdiciar, frame= cap.read()#cap es un objeto, sus valores son un boolenao y una matriz, el read es para desempaquetarlo, me va a devolver el booleano y la matriz
    ret, frame= cap.read()#frame la imagen, en ret el boolenado, cap es el video
    
    rgb= cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)#hace cambio de espacios de colores, bgr blue green red

    r,g,b=cv2.split(rgb)#voy a dividir la imagen en tres, divide en vectores

    cv2.imshow("rgb", rgb)#nombre de la ventana, la imagene que se guardo rgb

    #v2.imshow("r", r)#imagen en rojo

    #cv2.imshow("g", g)#imagen en verde

    #cv2.imshow("b", b)#imagen en azul
    
    k=cv2.waitKey(0)#0 porque es en vivo
    if k==27:
        break
cap.release()#va a liberar la camara
cv2.destroyAllWindows()#no recibe parametr
