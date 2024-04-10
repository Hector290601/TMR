import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32MultiArray
import time

class BlinkersInterface(Node):
    def __init__(self):
        super().__init__('barrido')
        self.publisher = self.create_publisher(Float32MultiArray,
                'esp32_node',
                1)
        self.timer_period = 1
        self.timer = self.create_timer(self.timer_period, self.pass_callback)

    def pass_callback(self):
        msg = Float32MultiArray()
        for i in range(50, 500, 1):
            msg.data = [5, (i*0.1)]
            self.publisher.publish(msg)
            time.sleep(1/30)
            if i == 50:
                msg.data = [2, 3]
                self.publisher.publish(msg)
                msg.data = [3, 0]
                self.publisher.publish(msg)
                time.sleep(1/30)
            elif i == 200:
                msg.data = [2, 0]
                self.publisher.publish(msg)
                msg.data = [3, 0]
                self.publisher.publish(msg)
                time.sleep(1/30)
            elif i == 300:
                msg.data = [2, 0]
                self.publisher.publish(msg)
                msg.data = [3, 3]
                self.publisher.publish(msg)
                time.sleep(1/30)
        for i in range(500, 50, -1):
            msg.data = [5, (i*0.1)]
            self.publisher.publish(msg)
            time.sleep(1/30)
            if i == 200:
                msg.data = [2, 3]
                self.publisher.publish(msg)
                msg.data = [3, 0]
                self.publisher.publish(msg)
                time.sleep(1/30)
            elif i == 300:
                msg.data = [2, 0]
                self.publisher.publish(msg)
                msg.data = [3, 0]
                self.publisher.publish(msg)
                time.sleep(1/30)
            elif i == 500:
                msg.data = [2, 0]
                self.publisher.publish(msg)
                msg.data = [3, 3]
                self.publisher.publish(msg)
                time.sleep(1/30)
        """
        for i in range(50, 200, 1):
            msg.data = [5, (i*0.1)]
            #self.publisher.publish(msg)
            time.sleep(0.1)
        msg.data = [2, 0]
        self.publisher.publish(msg)
        for i in range(200, 300, 1):
            msg.data = [5, (i*0.1)]
            #self.publisher.publish(msg)
            time.sleep(0.1)
        msg.data = [3, 3]
        self.publisher.publish(msg)
        for i in range(300, 500, 1):
            msg.data = [5, (i*0.1)]
            #self.publisher.publish(msg)
            time.sleep(0.1)
        """


def main(args=None):
    rclpy.init(args=args)
    blinkersInterface = BlinkersInterface()
    rclpy.spin(blinkersInterface)
    blinkersInterface.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

