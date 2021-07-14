import freenect
import numpy as np
import cv2
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

def cannyImage(frame):
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(frame, 50, 150, apertureSize = 3)
    return edges

def makeLines(frame):
    lines = cv2.HoughLinesP(frame, 1, np.pi/180, 100, 100, 10)
    for x1, y1, x2, y2 in lines[0]:
        cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    return frame

if __name__ == '__main__':
    while True:
        freenect_change_ir_brightness(0, 50)
        frame, _ = freenect.sync_get_video(0, freenect.VIDEO_IR_10BIT)
        np.clip(frame, 0, 2**10-1, frame)
        frame >>= 3
        frame = frame.astype(np.uint8)
        frameRBG = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        cany = cannyImage(frame)
        #lineas = makeLines(cany)
        cv2.imshow("IR", frame)
        cv2.imshow("RGB", frameRBG)
        cv2.imshow("Canny", cany)
        #cv2.imshow("Lines", lineas)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()
"""
