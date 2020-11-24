import freenect
import cv2
import numpy as np

def depthMap():
    depthMap, _ = freenect.sync_get_depth()
    depthMap = depthMap.astype(np.uint8)
    return depthMap

def depthLetters(dpth):
    for i in range(50, dpth.shape[0], 20):
        for j in range(50, dpth.shape[1], 20):
            color = (255, 255, 255)
            if dpth[i][j] == 0:
                cv2.putText(dpth, 'A', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 10:
                cv2.putText(dpth, 'B', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 20:
                cv2.putText(dpth, 'B', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 30:
                cv2.putText(dpth, 'C', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 40:
                cv2.putText(dpth, 'D', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 50:
                cv2.putText(dpth, 'E', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 60:
                cv2.putText(dpth, 'F', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 70:
                cv2.putText(dpth, 'G', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 80:
                cv2.putText(dpth, 'H', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 90:
                cv2.putText(dpth, 'I', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 100:
                cv2.putText(dpth, 'J', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 110:
                cv2.putText(dpth, 'K', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 120:
                cv2.putText(dpth, 'L', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 130:
                cv2.putText(dpth, 'M', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 140:
                cv2.putText(dpth, 'N', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 150:
                cv2.putText(dpth, 'O', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 140:
                cv2.putText(dpth, 'P', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 150:
                cv2.putText(dpth, 'Q', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 160:
                cv2.putText(dpth, 'R', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 170:
                cv2.putText(dpth, 'S', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 180:
                cv2.putText(dpth, 'T', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 190:
                cv2.putText(dpth, 'U', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 200:
                cv2.putText(dpth, 'V', (i, j), font, fontScale, color, thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 210:
                cv2.putText(dpth, 'W', (i, j), font, fontScale, (255, 0, 0), thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 220:
                cv2.putText(dpth, 'X', (i, j), font, fontScale, (255, 0, 0), thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 230:
                cv2.putText(dpth, 'Y', (i, j), font, fontScale, (255, 0, 0), thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 240:
                cv2.putText(dpth, 'Z', (i, j), font, fontScale, (255, 0, 0), thickness, cv2.LINE_AA)
            elif dpth[i][j] <= 250:
                cv2.putText(dpth, '0', (i, j), font, fontScale, (255, 0, 0), thickness, cv2.LINE_AA)
            else:
                cv2.putText(dpth, '!', (i, j), font, fontScale, (255, 0, 0), thickness, cv2.LINE_AA)
    return dpth

if __name__ == '__main__':
    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 0.5
    thickness = 2
    while True:
        dpth = depthMap()
        dpth = depthLetters(dpth)
        cv2.imshow('depth', dpth)
        k = cv2.waitKey(20)
        if k == 27:
            break
    cv2.destroyAllWindows()

