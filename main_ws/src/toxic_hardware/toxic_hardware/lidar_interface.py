import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan

class ScanInterface(Node):
    def __init__(self):
        super().__init__('scan_interface')
        self.subscription = self.create_subscription(
                LaserScan,
                '/scan',
                self.scan_callback,
                1
                )
        self.subscription

    def scan_callback(self, data):
        print(data)

def main(args=None):
    rclpy.init(args=args)
    scanInterface = ScanInterface()
    rclpy.spin(scanInterface)
    scanInterface.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

