import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import lgpio

servo_pin = lgpio.gpiochip_open(0)

class SteeringInterface(Node):
    def __init__(self):
        super().__init__('steering_interface')
        self.subscription = self.create_subscription(
                Float64,
                '/steering',
                self.steering_callback,
                60
                )
        self.subscription

    def steering_callback(self, data):
        global servo_pin
        recived = data.data
        if recived > 1:
            recived = 1
        elif recived < -1:
            recived = -1
        lgpio.tx_pwm(
                servo_pin,
                18,
                50,
                (7.2 + (recived*((10-5)/2)))
                )

def main(args=None):
    rclpy.init(args=args)
    steeringInterface = SteeringInterface()
    rclpy.spin(steeringInterface)
    steeringInterface.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

