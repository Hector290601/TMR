import rclpy
from rclpy.node import Node
import numpy as np
import math
from std_msgs.msg import Float64MultiArray, Float64
import os

def to_normal_form(x1, y1, x2, y2):
    A = y2 - y1
    B = x1 - x2
    C = A*x1 + B*y1
    theta = math.atan2(B,A)
    rho   = C/math.sqrt(A*A + B*B)
    if rho < 0:
        theta += math.pi
        rho = -rho
    return np.asarray([rho, theta])

class LaneTracker(Node):
    def __init__(self):
        super().__init__('image_subscriber')
        self.left_subscription = self.create_subscription(
                Float64MultiArray,
                '/lines/left',
                self.left_listener_callback,
                1
        )
        self.right_subscription = self.create_subscription(
                Float64MultiArray,
                '/lines/right', 
                self.right_listener_callback, 
                1
        )
        self.steering_publisher = self.create_publisher(Float64, '/steering', 1)
        self.speed_publisher = self.create_publisher(Float64, '/speed', 1)
        self.left_subscription
        self.right_subscription
        self.left_rho = 0
        self.left_theta = 0
        self.right_rho = 0
        self.right_theta = 0
        self.goal_rho_left = 176.49656082775857
        self.goal_theta_left = 0.9652746567890302
        self.goal_rho_right = 105.81332073669007
        self.goal_theta_right = -1.1552044701520168


    def two_dots_line(self, rho, theta, frame):
        if rho == 0 or theta == 0:
            return
        a = math.cos(theta)
        b = math.sin(theta)
        x0 = a * rho
        y0 = b * rho
        pt1 = (int(x0 + 1000*(-b)), int(y0 + 1000*(a)))
        pt2 = (int(x0 - 1000*(-b)), int(y0 - 1000*(a)))
        return pt1[0], pt1[1], pt2[0], pt2[1]

    def get_error(self, current, goal):
        if current != 0:
            return (abs(goal) - abs(current))
        else:
            return 0

    def get_errors(self):
        self.error_rho_left = self.get_error(self.left_rho, self.goal_rho_left)
        self.left_rho = 0
        self.error_theta_left = self.get_error(self.left_theta, self.goal_theta_left)
        self.left_theta = 0
        self.error_rho_right = self.get_error(self.right_rho, self.goal_rho_right)
        self.right_rho = 0
        self.error_theta_right = self.get_error(self.right_theta, self.goal_theta_right)
        self.right_theta = 0
        """
        print("left: [{}, {}]\nright: [{}, {}]".format(
            self.error_rho_left,
            self.error_theta_left,
            self.error_rho_right,
            self.error_theta_right
            )
        )
        """
        self.calculate_steering()

    def calculate_steering(self):
        theta = -(self.error_theta_left + self.error_theta_right)
        rho = -(self.error_rho_left + self.error_rho_right)
        message = Float64()
        message.data = -((theta * 0.055) + (rho * 0.04))
        self.steering_publisher.publish(message)
        msg = Float64()
        msg.data = 0.75
        self.speed_publisher.publish(msg)

    def left_listener_callback(self, data):
        self.left_rho = data.data[0]
        self.left_theta = data.data[1]
        self.get_errors()
        #print("left: {}@{}".format(self.left_rho, self.left_theta))

    def right_listener_callback(self, data):
        self.right_rho = data.data[0]
        self.right_theta = data.data[1]
        self.get_errors()
        #pr9int("right: {}@{}".format(self.right_rho, self.right_theta))
  
def main(args=None):
    rclpy.init(args=args)
    lane_tracker = LaneTracker()
    rclpy.spin(lane_tracker)
    image_subscriber.destroy_node()
    rclpy.shutdown()
  
if __name__ == '__main__':
    main()
