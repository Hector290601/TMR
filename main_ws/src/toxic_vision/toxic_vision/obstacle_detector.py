import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import UInt8
from cv_bridge import CvBridge
import cv2
import numpy as np

upper_color = [0, 0, 0]
lower_color = [255, 255, 255]

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
      '/depth/image_rect_raw',
      self.listener_callback, 
      1
      )
    self.publisher = self.create_publisher(Image, '/band_filter', 30)
    self.traffic_light = self.create_publisher(UIn8, '/obstacles/traffic_light', 30)
    self.subscription
    self.br = CvBridge()

  def range_finder(self):
    global lower_color, upper_color, where
    band_filter = cv2.inRange(
                where,
            np.array(lower_color),
            np.array(upper_color)
        )
    delta_x = 0.3
    delta_y = 0.3
    umbral = 125
    limit1 = 20
    limit2 = 100
    height, width, _ = band_filter.shape
    min_x = int((0.5 - delta_x) * width)
    max_x = int((0.5 + delta_x) * width)
    min_y = int((0.5 - delta_y) * height)
    max_y = int((0.5 + delta_y) * height)
    counter = 0
    for point in band_filder[min_y:max_y,min_x:max_y,:]:
        if point => umbral:
            counter += 1
        print(point)
        if counter => limit1:
            self.publisher.publish(self.traffic_light.publish(UInt8(1)))
        elif counter => limit2:
            self.publisher.publish(self.traffic_light.publish(UInt8(2)))
        else:
            self.publisher.publish(self.traffic_light.publish(UInt8(0)))
    return band_filter

  def process_image(self):
      global frame, where
      hsv = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
      where = hsv
      return hsv
   
  def listener_callback(self, data):
    global frame
    current_frame = self.br.imgmsg_to_cv2(data)
    frame = current_frame
    hsv = self.process_image()
    band_pass = self.range_finder()
    cv2.imshow("camera", current_frame)
    cv2.imshow("hsv", hsv)
    cv2.imshow("band_filter", band_pass)
    cv2.setMouseCallback("camera", mouse_callback)
    cv2.setMouseCallback("hsv", mouse_callback)
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
