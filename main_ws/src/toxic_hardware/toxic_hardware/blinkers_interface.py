import rclpy
from rclpy.node import Node
from std_msgs.msg import Int8
import lgpio
import time

gpio_pin = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(gpio_pin, 17)
lgpio.gpio_claim_output(gpio_pin, 27)
class BlinkersInterface(Node):
    def __init__(self):
        super().__init__('blinkers_interface')
        self.subscription = self.create_subscription(
                Int8,
                '/blinkers',
                self.blinkers_callback,
                2
                )
        self.subscription

    def blinkers_callback(self, data):
        global gpio_pin
        recived = data.data
        if recived == 0:
            lgpio.gpio_write(gpio_pin, 17, 0)
            lgpio.gpio_write(gpio_pin, 27, 0)
        elif recived == 1:
            lgpio.gpio_write(gpio_pin, 17, 1)
            time.sleep(0.5)
            lgpio.gpio_write(gpio_pin, 17, 0)
            time.sleep(0.5)
        elif recived == -1:
            lgpio.gpio_write(gpio_pin, 27, 1)
            time.sleep(0.5)
            lgpio.gpio_write(gpio_pin, 27, 0)
            time.sleep(0.5)
        else:
            lgpio.gpio_write(gpio_pin, 17, 1)
            lgpio.gpio_write(gpio_pin, 27, 1)
            time.sleep(0.5)
            lgpio.gpio_write(gpio_pin, 17, 0)
            lgpio.gpio_write(gpio_pin, 27, 0)
            time.sleep(0.5)


def main(args=None):
    rclpy.init(args=args)
    blinkersInterface = BlinkersInterface()
    rclpy.spin(blinkersInterface)
    blinkersInterface.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

