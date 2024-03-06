import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import UInt8MultiArray
from cv_bridge import CvBridge
import cv2
 
class ImagePublisher(Node):
  def __init__(self):
    super().__init__('image_publisher')
    self.publisher_ = self.create_publisher(Image, '/raw_rgb', 1)
    self.publisher_uint8 = self.create_publisher(UInt8MultiArray, '/compressed_rgb', 1)
    timer_period = 0.033
    self.timer = self.create_timer(timer_period, self.timer_callback)
    #self.cap = cv2.VideoCapture(4)
    self.cap = cv2.VideoCapture(0)
    """
    self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
    """
    self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    self.cap.set(cv2.CAP_PROP_FPS, 30)
    self.br = CvBridge()
   
  def timer_callback(self):
    ret, frame = self.cap.read()
    if ret:
      #img_encode = cv2.imencode('.jpg', frame)[1] 
      #message = UInt8MultiArray()
      #message.data = img_encode
      self.publisher_.publish(self.br.cv2_to_imgmsg(frame))
      #self.publisher_uint8.publish(message)
  
def main(args=None):
  rclpy.init(args=args)
  image_publisher = ImagePublisher()
  rclpy.spin(image_publisher)
  image_publisher.destroy_node()
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()
