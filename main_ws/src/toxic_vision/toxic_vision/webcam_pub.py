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
# @section parameters_webcam_publisher Important parameters to change.
# On this code, you'll change the camera int ID to select the camera you'll want
# opencv to open, read ad publish on the line:
# ```
# self.cap = cv2.VideoCapture(0)
# ```
#
# @section dependences_webcam_pub Dependences.
# - rclpy
#   - Used to node manipulation.
# - rclpy.node
#   - Used to node manipulation. (really idk why we don't import only this or
# the above library)
# - sensor_msgs.msg.Image
#   - Used to be able to use the Image message type (very self-explained, I
# think)
# - cvBridge.cvBridge
#   - Used to parse cv2 frame (like a numpy's multidimensional array) to ROS2's
# Image type
# - cv2
#   - In this case it's just used to open the camera, grab the image and read
# it from the buffer
#
# @section rights_webcam_pub Copyright
# This script conforms part from 'El tóxico' and it's licenced unser GPL 3V0.
#
# @section code_webcam_publisher Code Spinnet.
#
# \include webcam_pub.py
#

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
 

class ImagePublisher(Node):
    ##
    # @brief ImagePublisher object to grab the live camera image and publish to 
    # a ROS2 Node as CvBridge message type.
    #
    # @param Node The ROS2 Node where the image publisher'll be able to
    # read/write (this time, just write)
    #
    # @return None, keeps running and alive while the camera's oppened.
    #

    def __init__(self):
        ##
        # @brief ImagePublisher object init def (or constructor function, under
        # a Java's OOP context).
        #
        # @param self Self contained object like a 'this' reference, just to
        # read, write, and generally access object's attributes.
        #
        # @return ImagePublisherNewObject returns a new image publisher object.
        #
        # @detail Creates the publisher node, set the timer, open the camera,
        # set some needed params like image shape and framerate, open the
        # bridge between OpenCv and ROS2.
        #

        super().__init__('image_publisher')
        self.publisher_ = self.create_publisher(Image, '/raw_rgb', 1)
        timer_period = 0.033
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.cap.set(cv2.CAP_PROP_FPS, 30)
        self.br = CvBridge()

    def timer_callback(self):
        ##
        # @brief Timer callback to publish the image, everytime the timer
        # achieve the desired time, this callback'll run.
        #
        # @param self Self contained object like a 'this' reference, jus to
        # read, write, and generally access object's attributes.
        #
        # @return None, just publish the current frame.
        #
        # @detail Not much, just validate if there's a new image and publish it
        #

        ret, frame = self.cap.read()
        if ret:
            self.publisher_.publish(self.br.cv2_to_imgmsg(frame))

def main(args=None):
    ##
    # @brief This function create the publisher node, the image publisher object
    # and starts to run the publisher.
    #
    rclpy.init(args=args)
    image_publisher = ImagePublisher()
    rclpy.spin(image_publisher)
    image_publisher.destroy_node()
    rclpy.shutdown()
  
if __name__ == '__main__':
    main()
