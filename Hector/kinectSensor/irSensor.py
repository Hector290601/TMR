import freenect
import numpy as np
import cv2
"""
def get_video():
    array,_ = freenect.sync_get_video(0,freenect.VIDEO_IR_10BIT)
    return array
def pretty_depth(depth):
    np.clip(depth, 0, 2**10-1, depth)
    depth >>=2
    depth=depth.astype(np.uint8)
    return depth
if __name__ == "__main__":
    while 1:
        #get a frame from RGB camera
        frame = get_video()
        #display IR image
        frame = pretty_depth(frame)
        cv2.imshow('IR image',frame)

        # quit program when 'esc' key is pressed
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
"""

if __name__ == '__main__':
    while True:
        frame, _ = freenect.sync_get_video(0, freenect.VIDEO_IR_10BIT)
        np.clip(frame, 0, 2**10-1, frame)
        frame >>=2
        frame = frame.astype(np.uint8)
        cv2.imshow("IR", frame)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
