import sys
import rclpy
from rclpy.node import Node
import lgpio
from sensor_msgs.msg import Joy
from std_msgs.msg import Float64
import os
import time
import subprocess

"""
axes:
    0 - Left stick X  std: 0
    1 - Left stick Y  std: 0
    2 - Right stick X std: 0 
    3 - Right stick Y std: 0 
    4 - Right trigger std: 1
    5 - Left trigger  std: 1
    6 - Pad X         std: 0
    7 - Pad Y         std: 0
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
        super().__init__('automate')
        os.system("ros2 run joy_linux joy_linux_node &")
        print("JOY STARTED")
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
        os.system("ros2 run toxic_hardware motor_interface &")
        print("MOTOR STARTED")
        self.aviable_nodes = [
                "controller",
                "lane_detector",
                "lane_tracker",
                ]

    def kill_all(self):
            print("KILLING ALL NOT ESSENCIAL NODES")
            for node in self.aviable_nodes:
                os.system("pkill -f " + node)

    def launch_node(self, pkg, desired):
        os.system(
                "if ! pgrep -x "
                + desired
                + " > /dev/null; then ros2 run "
                + pkg
                + " "
                + desired
                + "; fi &"
            )

    def control_callback(self, data):
        if data.buttons[0]:
            print("NO OBSTACLES")
            self.kill_all()
            time.sleep(1)
            print("STARTING FUNCTION NODES")
            self.launch_node("toxic_vision", "lane_detector")
            self.launch_node("toxic_vision", "lane_tracker")
        elif data.buttons[1]:
            print("STATIC OBSTACLES")
        elif data.buttons[3]:
            print("DYNAMIC OBSTACLES")
        elif data.buttons[4]:
            print("PARKING")
        elif data.buttons[6]:
            print("MANUAL SPEED")
        elif data.buttons[7]:
            print("ALL AUTOMATIC")
        elif data.buttons[13]:
            print("ALL MANUAL")
            self.kill_all()
            time.sleep(1)
            self.launch_node("toxic_hardware", "controller")
            time.sleep(1)
        elif data.buttons[14]:
            print("EMERGENCY STOP")
            os.system("pkill -f controller")
            os.system("ros2 topic pub --once /speed std_msgs/msg/Float64 \"{data: 0.0}\"")
            self.kill_all()
            time.sleep(1)

def main(args=None):
    rclpy.init(args=args)
    control_subscriber = ControlSubscriber()
    rclpy.spin(control_subscriber)
    control_subscriber.destroy_node()
    rclpy.shutdown()
    os.system("ps ax | grep ros2")

if __name__ == '__main__':
    main()
