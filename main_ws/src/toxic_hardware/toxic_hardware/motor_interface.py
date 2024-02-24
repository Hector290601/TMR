##
# @file motor_interface.py
#
# @brief This script creates a  susbcriber node to  parse a 
# std_msgs.msg.Float64 ROS's message type to a Roboclaw's serial 
# output.
#
# 
#
#

import sys
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
sys.path.append('/home/ubuntu/roboclaw_python')
from roboclaw_3 import Roboclaw
roboclaw = Roboclaw("/dev/ttyACM0", 115200)

class MotorInterface(Node):
    def __init__(self):
        super().__init__('motor_interface')
        self.subscription = self.create_subscription(
                Float64,
                '/speed',
                self.motor_callback,
                60
                )
        self.subscription

    def motor_callback(self, data):
        global roboclaw
        recived = data.data
        if recived > 1.0:
            recived = 1.0
        elif recived < -1.0:
            recived = -1.0
        if recived >= 0:
            print("Forward@M1")
            roboclaw.ForwardM1(0x80, int(32*recived))
            print(recived)
        elif recived < 0:
            print("Backward@M1")
            roboclaw.BackwardM1(0x80, int(32*-recived))
            print(recived)

def main(args=None):
    print(roboclaw.Open())
    rclpy.init(args=args)
    motorInterface = MotorInterface()
    rclpy.spin(motorInterface)
    motorInterface.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
