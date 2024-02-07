##
# @file webcam_sub.py
#
# @brief Very simple image subscriber to /raw_rgb node.
#
# @section detailed_webcam_pub Detail
# This script create an image subscriber to "/raw_rgb" and draw the recived
# frame, this node's used just as test to verify the image publisher and nodes
# communication performance.
#
# @section parameters_webcam_subscriber Important parameters to change.
# On this code, you don'r need to change anything, except if you've changed the
# name of the image publisher node, or just wanna check another node.
#
# @section dependences_webcam_sub Dependences.
# - rclpy
#   - Used to node manipulation.
# - rclpy.node
#   - Used to node manipulation. (really idk why we don't import only this or
# the above library)
# - sensor_msgs.msg.Image
#   - Used to be able to use the Image message type (very self-explained, I
# think)
# - cvBridge.cvBridge
#   - Used to parse a ROS2's Image type to OpenCv Frame type
# - cv2
#   - In this case it's just used to draw the image in a frame.
#
# @section rights_webcam_Sub Copyright
# This script conforms part from 'El tóxico' and it's licenced unser GPL 3V0.
#
# @section code_webcam_subscriber Code Spinnet.
#
# \include webcam_sub.py
#

# Used by ros2
import rclpy
# Used by ros2
from rclpy.node import Node
# Used by ros2
from sensor_msgs.msg import Image
# Used by ros2
from cv_bridge import CvBridge
# Used to basic image manipulation
import cv2
 
class ImageSubscriber(Node):
    ##
    # @brief ImageSubscriber object to grab the currently published frame in
    # a ROS2 Topic (this time, it's '/raw_rgb', but you can change it) and
    # display in a GUI window.
    #
    # @param Node The ROS2 Node where the image publisher'll be able to
    # read/write (this time, just read)
    #
    # @return None, keeps running and alive until it's user cancelled.
    #

    def __init__(self):
        ##
        # @brief ImageSubscriber obtect init def (or constructor, under a
        # Java´s OOP context)
        #
        # @param self, Self contained object, like a 'this' reference just to
        # read, write and genereally access object's attributes.
        #
        super().__init__('image_subscriber')
        self.subscription = self.create_subscription(
                Image, 
                '/raw_rgb', 
                self.listener_callback, 
                25
                )
        self.subscription
        self.br = CvBridge()
    
    def listener_callback(self, data):
        current_frame = self.br.imgmsg_to_cv2(data)
        cv2.imshow("band_filter_sub", current_frame)
        cv2.waitKey(1)
  
def main(args=None):
    rclpy.init(args=args)
    image_subscriber = ImageSubscriber()
    rclpy.spin(image_subscriber)
    image_subscriber.destroy_node()
    rclpy.shutdown()
  
if __name__ == '__main__':
    main()
