import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64, Float64MultiArray, Int8
import lgpio
import time
import threading

board_interface = lgpio.gpiochip_open(0)
print(board_interface)
outputs = [
        25, 2, 3, 1
        ]

inputs = [
        10, 9, 11, 23, 24
        ]

for pin in outputs:
    lgpio.gpio_claim_output(board_interface, pin)

for pin in inputs:
    lgpio.gpio_claim_input(board_interface, pin)


def threaded_function(pin, id_pin):
    global distances, board_interface
    max_distance = 200
    max_time = max_distance / 1750
    start = time.time()
    end = time.time()
    while lgpio.gpio_read(board_interface, pin) == 0 or time.time() - start < max_time:
        start = time.time()
    while lgpio.gpio_read(board_interface, pin) == 0 or time.time() - start < max_time:
        end = time.time()
    delta = end - start
    distance = delta * 1750
    if distance > 200:
        distance = 200
    distances[id_pin] = distance

class USonicsInterface(Node):
    def __init__(self):
        global board_interface
        super().__init__('steering_interface')
        self.subscription = self.create_subscription(
                Int8,
                '/lookingat',
                self.look_callback,
                1
                )
        self.publisher = self.create_publisher(
                Float64MultiArray,
                '/obstacles/sensors',
                1
                )
        self.subscription

    def look_callback(self, data):
        global board_interface, distances
        recived = data.data
        if recived == 1:
            distances = [0, 0, 0]
            us1 = threading.Thread(target=threaded_function, args=(10, 0))
            us2 = threading.Thread(target=threaded_function, args=(9, 1))
            us3 = threading.Thread(target=threaded_function, args=(11, 2))
            lgpio.gpio_write(board_interface, 25, 0)
            start = time.time()
            while time.time() - start <= 0.00001:
                pass
            lgpio.gpio_write(board_interface, 25, 1)
            us1.start()
            us2.start()
            us3.start()
            start = time.time()
            while time.time() - start <= 0.00001:
                pass
            lgpio.gpio_write(board_interface, 25, 0)
            us1.join()
            us2.join()
            us3.join()
            print(distances)
        print(recived)

def main(args=None):
    rclpy.init(args=args)
    uSonicsInterface = USonicsInterface()
    rclpy.spin(uSonicsInterface)
    uSonicsInterface.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

