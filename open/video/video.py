import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("Camara", frame)
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break;

cv2.destroyAllWindows()
