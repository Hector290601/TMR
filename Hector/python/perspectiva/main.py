import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.circle(frame, (0, 400), 7, (0, 0, 0), 2)
        cv2.circle(frame, (640, 400), 7, (255, 0, 0), 2)
        cv2.circle(frame, (420, 240), 7, (0, 255, 0), 2)
        cv2.circle(frame, (100, 240), 7, (0, 0, 255), 2)
        puntos1 = np.float32(
                [
                    [0, 400],
                    [640, 400],
                    [420, 240],
                    [100, 240]
                ]
            )
        puntos2 = np.float32(
                [
                    [0, 0],
                    [0, 480],
                    [640, 480],
                    [640, 0]
                ]
            )
        m = cv2.getPerspectiveTransform(puntos1, puntos2)
        transformada = cv2.warpPerspective(frame, m, (640, 480))
        kernel = np.ones((20, 20), np.uint8)
        eroded = cv2.erode(transformada, kernel, iterations = 1)
        dilated = cv2.dilate(transformada, kernel, iterations = 1)
        superPos = cv2.addWeighted(eroded, 0.5, dilated, 0.5, 0)
        maximo = (230, 230, 240)
        minimo = (150, 160, 170)
        mask = cv2.inRange(superPos, minimo, maximo)
        cv2.imshow("frame", frame)
        cv2.imshow("mask", mask)
        cv2.imshow("final", superPos)
        k = cv2.waitKey(1)
        if k == 27:
            break


if __name__ == '__main__':
    main()
