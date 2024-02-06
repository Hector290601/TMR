import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

import subprocess

RST = None    
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = -2
top = padding
bottom = height-padding
x = 0

font = ImageFont.load_default()

class OledInterface(Node):
    def __init__(self):
        super().__init__('oled_interface')
        self.subscription = self.create_subscription(
                String,
                '/message',
                self.oled_callback,
                60
        )

    def oled_callback(self, data):
        global draw, image
        draw.rectangle((0,0,width,height), outline=0, fill=0)
        msg_content = data.data
        draw.text((x, top), msg_content,  font=font, fill=255)
        disp.image(image)
        disp.display()

def main(args=None):
    rclpy.init(args=args)
    oledInterface = OledInterface()
    rclpy.spin(oledInterface)
    oledInterface.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
