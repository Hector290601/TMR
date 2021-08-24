import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        """
        cv2.circle(frame, (0, 400), 7, (0, 0, 0), 2)
        cv2.circle(frame, (640, 400), 7, (255, 0, 0), 2)
        cv2.circle(frame, (420, 240), 7, (0, 255, 0), 2)
        cv2.circle(frame, (100, 240), 7, (0, 0, 255), 2)
        """
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
        """
        cv2.rectangle(transformada, (0, 0), (300, 150), (255, 0, 0))
        cv2.rectangle(transformada, (0, 300), (300, 480), (0, 255, 0))
        """
        izquierda = transformada[:150, :300, :]
        derecha = transformada[300:480, :300, :]
        kernel = np.ones((20, 20), np.uint8)
        #superPos = cv2.addWeighted(eroded, 0.5, dilated, 0.5, 0)
        #dilated = cv2.dilate(transformada, kernel, iterations = 1)
        #eroded = cv2.erode(transformada, kernel, iterations = 1)
        #opening = cv2.morphologyEx(transformada, cv2.MORPH_OPEN, kernel)
        #closing = cv2.morphologyEx(transformada, cv2.MORPH_CLOSE, kernel)
        gradientI = cv2.morphologyEx(izquierda, cv2.MORPH_GRADIENT, kernel)
        topI = cv2.morphologyEx(izquierda, cv2.MORPH_TOPHAT, kernel)
        blackI = cv2.morphologyEx(izquierda, cv2.MORPH_BLACKHAT, kernel)
        superPosI = cv2.addWeighted(gradientI, 0.5, topI, 0.5, 0)
        superPosI = cv2.addWeighted(superPosI, 0.5, blackI, 0.5, 0)
        gradientD = cv2.morphologyEx(derecha, cv2.MORPH_GRADIENT, kernel)
        topD = cv2.morphologyEx(derecha, cv2.MORPH_TOPHAT, kernel)
        blackD = cv2.morphologyEx(derecha, cv2.MORPH_BLACKHAT, kernel)
        superPosD = cv2.addWeighted(gradientD, 0.5, topD, 0.5, 0)
        superPosD = cv2.addWeighted(superPosD, 0.6, blackD, 0.4, 0)
        """
        maximo = (230, 230, 240)
        minimo = (150, 160, 170)
        mask = cv2.inRange(superPos, minimo, maximo)
        """
        cv2.imshow("frame", frame)
        cv2.imshow("izquierda", izquierda)
        cv2.imshow("derecha", derecha)
        """
        cv2.imshow("dilatacion", dilated)
        cv2.imshow("erosion", eroded)
        cv2.imshow("apertura", opening)
        cv2.imshow("cerradura", closing)
        cv2.imshow("gradiente", gradient)
        cv2.imshow("sombrero superior", top)
        cv2.imshow("sombrero negro", black)
        """
        cv2.imshow("final drecha", superPosD)
        cv2.imshow("final izquierda", superPosI)
        k = cv2.waitKey(1)
        if k == 27:
            break


if __name__ == '__main__':
    main()