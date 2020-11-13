import cv2
import numpy as np

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0)

def regionOfInterest(image):
    y, x= image.shape
    #polygons = np.array([[(0, 0), (144, 320), (288, 640)]])
    #polygons = np.array([[(390, 360), (730, 380), (600, 271)]])
    #polygons = np.array([[(150, 172), (357, 182), (339, 138)]])#para el video, ambos valores se vividen entre 2.02
    polygons = np.array([[(170, 330), (570, 350), (370, 171)]])
    #polygons = np.array([[(670, 0), (y//2, x//2), (670, 270)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    maskedImage = cv2.bitwise_and(image, image, mask = mask)
    return maskedImage


def canny(image, gray):
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny


while cap.isOpened():
    _, frame = cap.read()
    image = np.copy(frame)
    whitesMax = np.array([255, 255, 255])
    whitesMin = np.array([150, 150, 150])
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cannyImage = canny(image, gray)
    cropped = regionOfInterest(cannyImage)
    color = cv2.bitwise_or(frame, frame, mask = cropped)
    msk = cv2.inRange(color, whitesMin, whitesMax)
    cv2.imshow('results', msk)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()