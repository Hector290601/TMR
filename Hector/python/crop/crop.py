import cv2
import numpy as np

def crop(image):
    h, w, l = image.shape
    print('h: ', h, 'w: ', w)
    a = int( h / 2.1 )
    cropped = image[a : ]
    cv2.imwrite('cropped.jpeg', cropped)


image = cv2.imread('uno.jpeg')
crop(image)
