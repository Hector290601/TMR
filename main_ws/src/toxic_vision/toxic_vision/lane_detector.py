import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
import math

upper_color = [120, 235, 107]                                          
lower_color = [0, 0, 9]  

frame = []

def mouse_callback(event, x, y, flags, param):
    global where, upper_color, lower_color
    if event == cv2.EVENT_LBUTTONDOWN:
        hu, su, vu = upper_color
        hl, sl, vl = lower_color
        hc, sc, vc = where[y, x]
        print([lower_color, where[y, x], upper_color])
        if hu < hc:
            hu = int(hc)
        if su < sc:
            su = int(sc)
        if vu < vc:
            vu = int(vc)
        if hc < hl:
            hl = int(hc)
        if sc < sl:
            sl = int(sc)
        if vc < vl:
            vl = int(vc)
        upper_color = [hu, su, vu]
        lower_color = [hl, sl, vl]
        print([lower_color, where[y, x], upper_color])
    elif event == cv2.EVENT_RBUTTONDOWN:
        upper_color = [0, 0, 0]
        lower_color = [255, 255, 255]
    elif event == cv2.EVENT_MOUSEWHEEL:
        print("upper_color = {}\nlower_color = {}".format(
            upper_color, lower_color
            )
            )

class ImageSubscriber(Node):
  def __init__(self):
    super().__init__('image_subscriber')
    self.subscription = self.create_subscription(
      Image, 
      '/raw_rgb', 
      self.listener_callback, 
      1
      )
    self.subscription
    self.br = CvBridge()

  def range_finder(self):
    global lower_color, upper_color, where
    band_filter = cv2.inRange(
                where,
            np.array(lower_color),
            np.array(upper_color)
        )
    return band_filter

  def process_image(self):
      global frame, where
      hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
      where = hsv
      return hsv
  
  def line_finder(self):
      global band_pass, frame
      kernel = np.ones((3, 3), np.uint8) 
      band_pass = cv2.morphologyEx(band_pass, cv2.MORPH_OPEN, kernel, iterations=1) 
      dst = cv2.Canny(band_pass, 100, 100, None, 3)
      lines = cv2.HoughLines(dst, 1, np.pi / 180, 150, None, 50, 10)
      if lines is not None:
          for i in range(0, len(lines)):
              rho = lines[i][0][0]
              theta = lines[i][0][0]
              a = math.cos(theta)
              b = math.sin(theta)
              x0 = a * rho
              y0 = a * rho
              pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
              pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
              cv2.line(frame, pt1, pt2, (0,0,255), 3, cv2.LINE_AA)

  def listener_callback(self, data):
    global frame, band_pass
    current_frame = self.br.imgmsg_to_cv2(data)
    frame = current_frame
    hsv = self.process_image()
    band_pass = self.range_finder()
    self.line_finder()
    cv2.imshow("camera", current_frame)
    cv2.imshow("band_filter", band_pass)
    cv2.setMouseCallback("camera", mouse_callback)
    cv2.setMouseCallback("band_filter", mouse_callback)
    cv2.waitKey(1)
  
def main(args=None):
  rclpy.init(args=args)
  image_subscriber = ImageSubscriber()
  rclpy.spin(image_subscriber)
  image_subscriber.destroy_node()
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()
