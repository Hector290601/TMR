import sys
import rclpy
from rclpy.node import Node
import lgpio
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64
import os

"""
axes:
    - Left stick X  std: 0
    - Left stick Y  std: 0
    - Right stick X std: 0 
    - Right stick Y std: 0 
    - Right trigger std: -1
    - Left trigger  std: -1
    - Pad X         std: 0
    - Pad Y         std: 0
    buttons:
        0  - A : NO OBSTACLE
        1  - B : STATIC OBSTACLES
        2  - 0
        3  - X : DYNAMIC OBSTACLES
        4  - Y : PARKINT
        5  - 0
        6  - Left back : MANUAL SPEED
        7  - Right back : ALL AUTOMATIC
        8  - 0
        9  - 0
        10 - 0
        11 - 0
        12 - 0
        13 -Left stick Z : ALL MANUAL
        14 - Right stick Z : EMERGENCY STOP
        ---

"""

class ControlSubscriber(Node):
    def __init__(self):
        print("INITIALIZING...")
        super().__init__('control_toxic_subscriber')
        self.subscription = self.create_subscription(
                Joy,
                '/joy',
                self.control_callback,
                60
                )
        self.subscription
        os.system("ros2 run toxic_vision webcam_publisher &")
        print("WEBCAM STARTED")
        os.system("ros2 run toxic_hardware servo_interface &")
        print("STEERING STARTED")
        os.system("ros2 run toxic_hardware servo_interface &")
        print("MOTOR STARTED")

    def control_callback(self, data):
        print(data.buttons)
        if data[0]:
            print("NO OBSTACLES")
        elif data[1]:
            print("STATIC OBSTACLES")
        elif data[3]:
            print("DYNAMIC OBSTACLES")
        elif data[4]:
            print("PARKING")
        elif data[6]:
            print("MANUAL SPEED")
        elif data[7]:
            print("ALL AUTOMATIC")
        elif data[13]:
            print("ALL MANUAL")
        elif data[14]:
            print("EMERGENCY STOP")

def main(args=None):
    rclpy.init(args=args)
    control_subscriber = ControlSubscriber()
    rclpy.spin(control_subscriber)
    control_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
