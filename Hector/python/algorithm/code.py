import cv2

cap = cv2.VideoCapture(0)
k = 0

while cap.isOpened():
    ret, frame = cap.read() #obtener imagen
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #pasamos a grises
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    anchura, altura, ch = hsv.shape
    mitad = altura // 2
    cortado = hsv[:mitad, :]
    cv2.imshow('Frame', frame)  #mostrar
    cv2.imshow('Gray', gray)
    cv2.imshow('cortado', cortado)
    cv2.imshow('hsv', hsv)
    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
