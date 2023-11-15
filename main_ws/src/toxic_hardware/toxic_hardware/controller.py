import sys
import rclpy
from rclpy.node import Node
import lgpio
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64
sys.path.append('/home/ubuntu/roboclaw_python/')
print(sys.path)
from roboclaw_3 import Roboclaw

interface = lgpio.gpiochip_open(0)
roboclaw = Roboclaw("/dev/ttyACM0", 115200)

roboclaw.Open()

class ControlSubscriber(Node):
    def __init__(self):
        super().__init__('control_toxic_subscriber')
        self.subscription = self.create_subscription(
                Joy,
                '/joy',
                self.control_callback,
                60
                )
        self.speed_publisher = self.create_publisher(Float64, '/speed', 60)
        self.steering_publisher = self.create_publisher(Float64, '/steering', 60)
        self.subscription
        self.steering_publisher
        self.speed_publisher

    def control_callback(self, data):
        normalized_steering = data.axes[0]
        normalized_fw_speed = data.axes[5]
        normalized_bw_speed = data.axes[2]
        print(normalized_steering)
        print(normalized_fw_speed)
        self.steering_publisher.publish(Float64(normalized_steering))
        self.speed_publisher.publish(Float64(normalized_fw_speed + normalized_bw_speed))

def main(args=None):
    rclpy.init(args=args)
    control_subscriber = ControlSubscriber()
    rclpy.spin(control_subscriber)
    control_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
