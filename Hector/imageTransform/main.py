import cv2
assert float(cv2.__version__.rsplit('.', 1)[0]) >= 3, 'OpenCV version 3 or newer required.'
import numpy as np

K = np.array([[  689.21,     0.  ,  1295.56],
              [    0.  ,   690.48,   942.17],
              [    0.  ,     0.  ,     1.  ]])

D = np.array([0., 0., 0., 0.])

Knew = K.copy()

Knew[(0,1), (0,1)] = 0.4 * Knew[(0,1), (0,1)]

def main():
    cap = cv2.imread("fisheye_004.jpg")
    frame = cap
    copiedFrame = frame.copy()
    cv_size = lambda img: tuple(img.shape[1::-1])
    shp = cv_size(frame)
    original = frame[0:-1, 0:(((shp[0])//2)-10)]
    fishEye = frame[0:-1, (((shp[0])//2) + 10):shp[0]]
    img_undistorted = cv2.fisheye.undistortImage(fishEye, K, D=D, Knew=Knew)
    k = 0
    cv2.imshow('original', original)
    cv2.imshow('fishEye', fishEye)
    cv2.imshow('undistorted', img_undistorted)
    while k != 27:
        k = cv2.waitKey(1)

if __name__ == '__main__':
    main()

