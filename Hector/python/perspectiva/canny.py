import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
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
        izquierda = transformada[:150, :300, :]
        derecha = transformada[300:480, :300, :]
        kernel = np.ones((20, 20), np.uint8)
        gradientI = cv2.morphologyEx(izquierda, cv2.MORPH_GRADIENT, kernel)
        topI = cv2.morphologyEx(izquierda, cv2.MORPH_TOPHAT, kernel)
        blackI = cv2.morphologyEx(izquierda, cv2.MORPH_BLACKHAT, kernel)
        superPosI = cv2.addWeighted(gradientI, 0.5, topI, 0.5, 0)
        superPosI = cv2.addWeighted(superPosI, 0.6, blackI, 0.4, 0)
        gradientD = cv2.morphologyEx(derecha, cv2.MORPH_GRADIENT, kernel)
        topD = cv2.morphologyEx(derecha, cv2.MORPH_TOPHAT, kernel)
        blackD = cv2.morphologyEx(derecha, cv2.MORPH_BLACKHAT, kernel)
        superPosD = cv2.addWeighted(gradientD, 0.5, topD, 0.5, 10)
        superPosD = cv2.addWeighted(superPosD, 0.9, blackD, 0.1, 0)
        supers = np.concatenate((superPosI, superPosD), axis = 0)
        canny = cv2.Canny(supers, 60, 60)
        kernel = np.ones((7, 7), np.uint8)
        openc = cv2.morphologyEx(canny, cv2.MORPH_CLOSE, kernel)
        cnts = cv2.findContours(openc, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = cnts[0] if len(cnts) == 2 else cnts[1]
        for c in cnts:
            cv2.drawContours(openc,[c], 0, (255, 0, 0), 3)
        cv2.imshow("frame", frame)
        cv2.imshow("superPosicionamientos concatenados", supers)
        cv2.imshow("cannyOpenc", openc)
        k = cv2.waitKey(1)
        if k == 27:
            break


if __name__ == '__main__':
    main()
