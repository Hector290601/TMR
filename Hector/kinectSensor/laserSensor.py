from freenect import sync_get_depth as get_depth
import numpy as np
import cv2

depth = get_depth()[0]

output = depth.astype(np.uint8)
cv2.imshow('Depth', output)
cv2.waitKey(0) # se espera a que se presione cualquier tecla
cv2.destroyAllWindows() # un clean up no está de más
