import freenect
import numpy as np
import cv2
import time

if __name__ == '__main__':
    while True:
        irSensor, _ = freenect.sync_get_depth()
        rgbVideo, _ = freenect.sync_get_video()
        np.clip(irSensor, 0, 2**10-1, irSensor)
        irSensor >>=2
        irSensor = cv2.cvtColor(irSensor, cv2.COLOR_GRAY2BGR)
        bgrVideo = cv2.cvtColor(rgbVideo, cv2.COLOR_RGB2BGR)
        irSensor = irSensor.astype(np.uint8)
        bgrVideo = bgrVideo.astype(np.uint8)
        superPos = cv2.addWeighted(irSensor, 0.5, bgrVideo, 0.5, 0)
        #superPos = cv2.cvtColor(superPos, cv2.COLOR_GRAY2RGB)
        cv2.imshow("irSensor", irSensor)
        cv2.imshow("bgrVideo", bgrVideo)
        cv2.imshow("addedCams", superPos)
        k = cv2.waitKey(20) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()

