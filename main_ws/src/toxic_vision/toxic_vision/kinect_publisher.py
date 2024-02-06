#import the necessary modules
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import freenect
import cv2
import numpy as np

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('kinect_rgb_publisher')
        self.publisher_ = self.create_publisher(Image, "kinect/rgb/raw", 30)
        timer = 0.03
        self.timer = self.create_timer(timer, self.timer_callback)
        self.bgr_frame = np.zeros((480, 640, 3), dtype = np.uint8)
        self.br = CvBridge()

    def timer_callback(self):
        frame, _ = freenect.sync_get_video()
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        self.publisher_.publish(self.br.cv2_to_imgmsg(frame))

def main(args=None):
    rclpy.init(args=args)
    image_publisher = ImagePublisher()
    rclpy.spin(image_publisher)
    image_publisher.destroy_node()
    rclp.shutdown()

if __name__ == '__main__':
    main()

