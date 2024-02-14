import sys
import rclpy
from rclpy.node import Node
import lgpio
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64

class ControlSubscriber(Node):
    def __init__(self):
        super().__init__('controller')
        self.subscription = self.create_subscription(
                Joy,
                '/joy',
                self.control_callback,
                60
                )
        self.speed_publisher = self.create_publisher(Float64, '/speed', 1)
        self.steering_publisher = self.create_publisher(Float64, '/steering', 1)
        self.subscription
        self.steering_publisher
        self.speed_publisher

    def control_callback(self, data):
        normalized_steering = data.axes[0]
        steering_msg = Float64()
        steering_msg.data = normalized_steering
        self.steering_publisher.publish(steering_msg)
        speed_msg = Float64()
        if data.axes[4] != 1:
            speed_msg.data = -(data.axes[4] - 1)
        elif data.axes[5] != 1:
            speed_msg.data = (data.axes[5] - 1)
        self.speed_publisher.publish(speed_msg)

def main(args=None):
    rclpy.init(args=args)
    control_subscriber = ControlSubscriber()
    rclpy.spin(control_subscriber)
    control_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
