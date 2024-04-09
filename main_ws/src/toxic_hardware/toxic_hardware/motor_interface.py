import sys
import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
import os
import time
sys.path.append('/home/ubuntu/roboclaw_python')
from roboclaw_3 import Roboclaw
roboclaw = Roboclaw("/dev/ttyACM0", 115200)

class MotorInterface(Node):
    def __init__(self):
        super().__init__('motor_interface')
        timer_period = 0.01
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.subscription = self.create_subscription(
                Float64,
                '/speed',
                self.motor_callback,
                1
                )
        self.subscription
        self.last = 0
        self.current_speed = 0.0

    def motor_callback(self, data):
        global roboclaw
        self.current_speed = data.data
        self.last = time.time()

    def timer_callback(self):
        delta = time.time() - self.last
        if delta > 0.05:
            self.current_speed = 0
        if self.current_speed > 1.0:
            self.current_speed = 1.0
        elif self.current_speed < -1.0:
            self.current_speed = -1.0
        if self.current_speed >= 0:
            roboclaw.ForwardM2(0x80, int(20*self.current_speed))
        elif self.current_speed < 0:
            roboclaw.BackwardM2(0x80, int(20*-self.current_speed))

def main(args=None):
    print(roboclaw.Open())
    rclpy.init(args=args)
    motorInterface = MotorInterface()
    rclpy.spin(motorInterface)
    motorInterface.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
