import cv2
import imutils

cap = cv2.VideoCapture(0)
k = cv2.waitKey(1)

def getRedCenter(image):
    limits = ((162, 153, 61), (192, 255, 178))
    maskRojo = cv2.inRange(image, limits[0], limits[1])
    cnts, 

while not k == ord('q'):
    ret, frame = cap.read()
    if frame is None:
        break
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()

