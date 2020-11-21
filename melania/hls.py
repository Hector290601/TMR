import cv2
import numpy

cap=cv2.imread("robot.jpeg")#por convenio las imagenes se les iba a asignar a cap,
frame = cap #el fotogramavideo se llama frame
hls= cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)#hace cambio de espacios de colores, bgr blue green red

h,l,s=cv2.split(hls)#voy a dividir la imagen en tres, divide en vectores

cv2.imshow("hls", hls)#nombre de la ventana, la imagene que se guardo rgb

cv2.imshow("h", h)#imagen en rojo

cv2.imshow("l", l)#imagen en verde

cv2.imshow("s", s)#imagen en azul
k=0#tecla de key
while k!=27:#27 es el valor de la tecla esc en ascii, con esc se cierra
    k=cv2.waitKey(1)#es para que espere la tecla en un tiempo en milisegundos

cv2.destroyAllWindows()#no recibe parametro
