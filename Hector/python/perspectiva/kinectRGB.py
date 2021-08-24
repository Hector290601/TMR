import freenect
import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)
    while True:
        rgbVideo, _ = freenect.sync_get_video()
        bgrVideo = cv2.cvtColor(rgbVideo, cv2.COLOR_RGB2BGR)
        frame = bgrVideo.astype(np.uint8)
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
        #superPos = cv2.addWeighted(eroded, 0.5, dilated, 0.5, 0)
        dilated = cv2.dilate(transformada, kernel, iterations = 1)
        eroded = cv2.erode(transformada, kernel, iterations = 1)
        opening = cv2.morphologyEx(transformada, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(transformada, cv2.MORPH_CLOSE, kernel)
        gradient = cv2.morphologyEx(transformada, cv2.MORPH_GRADIENT, kernel)
        top = cv2.morphologyEx(transformada, cv2.MORPH_TOPHAT, kernel)
        black = cv2.morphologyEx(transformada, cv2.MORPH_BLACKHAT, kernel)
        """
        maximo = (230, 230, 240)
        minimo = (150, 160, 170)
        mask = cv2.inRange(superPos, minimo, maximo)
        """
        cv2.imshow("frame", frame)
        cv2.imshow("transformada", transformada)
        cv2.imshow("dilatacion", dilated)
        cv2.imshow("erosion", erode)
        cv2.imshow("apertura", opening)
        cv2.imshow("cerradura", closing)
        cv2.imshow("gradiente", gradient)
        cv2.imshow("sombre superior", top)
        cv2.imshow("sombre negro", black)
        k = cv2.waitKey(1)
        if k == 27:
            break


if __name__ == '__main__':
    main()
