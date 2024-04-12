import rclpy
from rclpy.node import Node
import numpy as np
import math
from std_msgs.msg import Float64MultiArray, Float64, Float32MultiArray
import os
from sensor_msgs.msg import Joy

##
# TODO:
# - Add a timer to verify the last line message recived.
# - Add a subscriber to see if the speed and steering's recognized
#

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
        self.joy_subscriber = self.create_subscription(
                Joy,
                '/joy',
                self.control_callback,
                1
                )
        """
        self.speed_subscriber = self.create_subscription(
                Float64,
                '/speed',
                self.control_callback,
                1
                )
        """
        timer_period = 1/30
        #self.timer = self.create_timer(timer_period, self.timer_callback)
        self.steering_publisher = self.create_publisher(Float64, '/steering', 1)
        self.esp32_publisher = self.create_publisher(Float32MultiArray, '/esp32_topic', 1)
        self.speed_publisher = self.create_publisher(Float64, '/speed', 1)
        self.k_rho_publisher = self.create_publisher(Float64, '/k/rho', 1)
        self.k_theta_publisher = self.create_publisher(Float64, '/k/theta', 1)
        self.max_speed_publisher = self.create_publisher(Float64, '/max_speed', 1)
        self.left_subscription
        self.right_subscription
        self.left_rho = 0
        self.left_theta = 0
        self.right_rho = 0
        self.right_theta = 0
        """
        self.goal_rho_left = 85.3915173743109
        self.goal_theta_left = 1.1003831279978304
        self.goal_rho_right = 233.10512423852725
        self.goal_theta_right = -0.9467732738181398
        #"""
        self.goal_rho_left = 0
        self.goal_theta_left = 0
        self.goal_rho_right = 0
        self.goal_theta_right = 0
        self.k_rho = 0.0055
        self.k_theta = 3.54
        self.autocalibrate_left = 0
        self.autocalibrate_right = 0
        self.max_speed = 1.2
        self.publish_flag = False

    def control_callback(self, data):
        self.k_rho += 0.0001 * data.axes[0]
        self.k_theta += 0.01 * data.axes[3]
        self.max_speed += (0.001 * data.axes[7])
        if data.buttons[0]:
            msg = Float64()
            msg.data = self.k_rho
            self.k_rho_publisher.publish(msg)
            msg = Float64()
            msg.data = self.k_theta
            self.k_theta_publisher.publish(msg)
            msg = Float64()
            msg.data = self.max_speed
            self.max_speed_publisher.publish(msg)
            print("self.k_rho = {}\nself.k_theta = {}\nself.max_speex = {}".format(
                self.k_rho,
                self.k_theta,
                self.max_speed
                )
            )
        if data.buttons[1]:
            self.autocalibrate_left = 0
            self.autocalibrate_right = 0
            self.goal_rho_left = 0
            self.goal_theta_left = 0
            self.goal_rho_right = 0
            self.goal_theta_right = 0
        if data.buttons[3]:
            self.publish_flag = False
        elif data.buttons[4]:
            self.publish_flag = True


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
        message_esp32 = Float32MultiArray()
        message.data = -((theta * self.k_theta) + (rho * self.k_rho))
        message_esp32.data = [4,
                (
                    (180/math.pi)
                    * -((theta * self.k_theta) + (rho * self.k_rho))
                    )
                + 85
                ]

        if self.publish_flag:
            self.steering_publisher.publish(message)
            self.esp32_publisher.publish(message_esp32)
        msg = Float64()
        msg.data = self.max_speed
        if self.publish_flag:
            self.speed_publisher.publish(msg)

    def left_listener_callback(self, data):
        if self.autocalibrate_left < 10:
            self.goal_rho_left += data.data[0] * 0.1
            self.goal_theta_left += data.data[1] * 0.1
            self.autocalibrate_left += 1
            print("CALIBRATING LEFT")
        else:
            self.left_rho = data.data[0]
            self.left_theta = data.data[1]
            self.get_errors()
        #print("left: {}@{}".format(self.left_rho, self.left_theta))

    def right_listener_callback(self, data):
        if self.autocalibrate_right < 10:
            self.goal_rho_right += data.data[0] * 0.1
            self.goal_theta_right += data.data[1] * 0.1
            self.autocalibrate_right += 1
            print("CALIBRATING RIGHT")
        else:
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