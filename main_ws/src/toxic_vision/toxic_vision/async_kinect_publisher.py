#import the necessary modules
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import freenect
import cv2
import numpy as np
import threading

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('kinect_rgb_publisher')
        self.publisher_ = self.create_publisher(Image, "kinect/rgb/raw", 30)
        self.frame = np.zeros((480, 640, 3), dtype = np.uint8)
        timer = 0.03
        self.timer = self.create_timer(timer, self.timer_callback)
        self.bgr_frame = np.zeros((480, 640, 3), dtype = np.uint8)
        self.br = CvBridge()

    def timer_callback(self):
        frame = self.frame
        self.publisher_.publish(self.br.cv2_to_imgmsg(frame))

def video_cback(dev, data, timestamp):
    global image_publisher
    image_publisher.frame = data[:, :, ::-1]

def kinect_async():
    global image_publisher
    freenect.runloop(
            video = video_cback,
            )

def main(args=None):
    global image_publisher
    rclpy.init(args=args)
    image_publisher = ImagePublisher()
    ros_thread = threading.Thread(target=rclpy.spin, args=(image_publisher,))
    kinect_thread = threading.Thread(target=kinect_async)
    ros_thread.start()
    kinect_thread.start()
    ros_thread.join()
    kinect_thread.join()
    #rclpy.spin(image_publisher)
    image_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

