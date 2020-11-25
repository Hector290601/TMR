import cv2
import time

cap = cv2.VideoCapture(0)
salida = cv2.VideoWriter('test.avi',cv2.VideoWriter_fourcc(*'XVID'),20.0,(int(cap.get(3)),int(cap.get(4))))

while cap.isOpened():
	_, frame = cap.read()
	cv2.imshow('test', frame)
	salida.write(frame)
	if cv2.waitKey(1) & 0xFF == ord('f'):
		nombre = 'captura' + str(time.time()) + '.png'
		cv2.imwrite(nombre, frame)
	if cv2.waitKey(1) & 0xFF == ord('s'):
		break

cap.release()
cv2.destroyAllWindows()
