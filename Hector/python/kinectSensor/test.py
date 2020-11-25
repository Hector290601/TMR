from freenect import sync_get_depth as get_depth, sync_get_video as get_video
import cv2
import numpy as np
  
def doloop():
    global depth, rgb
    while True:
        # Get a fresh frame
        (depth,_), (rgb,_) = get_depth(), get_video()
        
        # Build a two panel color image
        d3 = np.dstack((depth,depth,depth)).astype(np.uint8)
        da = np.hstack((d3,rgb))
        
        # Simple Downsample
        cv2.imshow('both',np.array(da[::2,::2,::-1]))
        k = cv2.waitKey(5)
        if k == 27:
            break
        
doloop()
