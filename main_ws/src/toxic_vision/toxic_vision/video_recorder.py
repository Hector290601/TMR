import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os
 
class ImageSubscriber(Node):
  def __init__(self):
    super().__init__('image_subscriber')
    self.subscription = self.create_subscription(
      Image, 
      '/raw_rgb', 
      self.listener_callback, 
      25
      )
    self.subscription
    self.br = CvBridge()
    self.output = cv2.VideoWriter('/home/ubuntu/output.avi', -1, 20, 0, (640, 480))
    print(os.getcwd())
   
  def listener_callback(self, data):
    current_frame = self.br.imgmsg_to_cv2(data)
    print("writing")
    self.output.write(current_frame)
    print(dir(self.output))
    print(self.output.getBackendName())
  
def main(args=None):
  rclpy.init(args=args)
  image_subscriber = ImageSubscriber()
  rclpy.spin(image_subscriber)
  image_subscriber.destroy_node()
  rclpy.shutdown()
  image_subscriber.release()
  
if __name__ == '__main__':
  main()
