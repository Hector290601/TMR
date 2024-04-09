import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import UInt8MultiArray
from cv_bridge import CvBridge
import cv2
import numpy as np
 
class ImageSubscriber(Node):
  def __init__(self):
    super().__init__('image_subscriber')
    self.subscription = self.create_subscription(
      UInt8MultiArray, 
      '/compressed_rgb', 
      self.listener_callback, 
      1
      )
    self.subscription
    self.br = CvBridge()
   
  def listener_callback(self, data):
    print(type(data.data))
    current_frame = cv2.imdecode(np.array(data.data, type=np.uint8), cv2.IMREAD_COLOR)
    cv2.imshow("compressed_image", current_frame)
    cv2.waitKey(1)
  
def main(args=None):
  rclpy.init(args=args)
  image_subscriber = ImageSubscriber()
  rclpy.spin(image_subscriber)
  image_subscriber.destroy_node()
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()
