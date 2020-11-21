import cv2
import numpy as np

def cannyImage(imagen):
    nueva=cv2.GaussianBlur(imagen, (5,5),0)
    nn=cv2.Canny(nueva, 10, 250)
    return nn
def regionOfInterest(regionImage):#regioninteres
   regionPolygons = np.array([[(0, 400), (640, 400), (640, 180), (0, 180)]])
   zeros = np.zeros_like(regionImage)
   cv2.fillPoly(zeros, regionPolygons, 255)
   regionedImage = cv2.bitwise_and(regionImage, regionImage, mask=zeros)
   return regionedImage

def color(rgb, gray,cortado):#imagen a color en gris y cortada
    colormax= np.array([255,255,255])
    colormin = np.array([79,73,57])
    colorEncon=cv2.bitwise_and(rgb, rgb, mask=cortado)
    colorEmcon=cv2.inRange(colorEncon, colormin, colormax)
    return colorEncon

def main():
    while cap.isOpened():
        ret, frame= cap.read()#descomprimir imagen
        gray= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        imbin=cannyImage(gray)#guardar la imagen en binario
        cv2.imshow("Carril", gray)
        gray1 = regionOfInterest(imbin)#guardar en una variable
        cv2.imshow("Region", gray1)#mostrar
        gray2=color(gray1,gray, imbin)
        cv2.imshow("Color", gray2)
        k=cv2.waitKey(1)#0 porque es en vivo
        if k==27:#esc
            break
        
if __name__=='__main__':
    cap= cv2.VideoCapture(0)
    k=0
    main()

    cap.release()#va a liberar la camara
    cv2.destroyAllWindows()#no recibe parametr
    

    
 