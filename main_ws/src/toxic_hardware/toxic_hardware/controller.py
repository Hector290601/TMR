import sys
import rclpy
from rclpy.node import Node
import lgpio
from sensor_msgs.msg import Joy
sys.path.insert(1, '/home/pumas/roboclaw_python/roboclaw_python/')
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
        self.subscription

    def steering(self, normalized_value):
        global interface
        lgpio.tx_pwm(
                interface,
                18,
                50,
                (7.2 + (normalized_value*((10-5)/2)))
                )

    def speed(self, normalized_speed):
        print(1-normalized_speed)
        current_speed = 1 - normalized_speed
        global roboclaw
        roboclaw.ForwardM1(0x80, int(32 * current_speed))

    def control_callback(self, data):
        #msg_speed = data.axes[]
        normalized_steering = data.axes[0]
        normalized_speed = data.axes[5]
        self.steering(normalized_steering)
        self.speed(normalized_speed)

def main(args=None):
    rclpy.init(args=args)
    control_subscriber = ControlSubscriber()
    rclpy.spin(control_subscriber)
    control_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
