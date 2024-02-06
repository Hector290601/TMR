##
# @file webcam_pub.py
#
# @brief Main image publisher as /raw_rgb node.
#
# @section detailed_webcam_pub Detail
# This script create the image publisher as "/raw_rgb", open the
# camera, read the camera and publish frames as Ros2 OpenCv messages, to be able
# to all nodes to subscribe to te current frames to process it.
#

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
 
class ImagePublisher(Node):
  def __init__(self):
    super().__init__('image_publisher')
    self.publisher_ = self.create_publisher(Image, '/raw_rgb', 1)
    timer_period = 0.033
    self.timer = self.create_timer(timer_period, self.timer_callback)
    self.cap = cv2.VideoCapture(2)
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
      self.publisher_.publish(self.br.cv2_to_imgmsg(frame))
  
def main(args=None):
  rclpy.init(args=args)
  image_publisher = ImagePublisher()
  rclpy.spin(image_publisher)
  image_publisher.destroy_node()
  rclpy.shutdown()
  
if __name__ == '__main__':
  main()
