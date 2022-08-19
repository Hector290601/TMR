import time
import board
import busio
import digitalio

from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import subprocess

oled_reset = digitalio.DigitalInOut(board.D4)

width = 128
height = 64
border = 1

i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(width, height, i2c, addr=0x3C, reset=oled_reset)

oled.fill(0)
oled.show()

img = Image.new("1", (oled.width, oled.height))

draw = ImageDraw.Draw(img)

draw.rectangle((0, 0, oled.width, oled.width), outline=255, fill=255)

font = ImageFont.load_default()

while True:
    draw.rectangle((0, 0, oled.width, oled.width), outline=0, fill=0)
    ip = "hostname -I"
    IP = subprocess.check_output(ip, shell=True)
    try:
        ssid = "iwgetid"
        SSID = subprocess.check_output(ssid, shell=True)
        SSID = str(SSID, 'utf-8')
        SSID = SSID[SSID.find("ESSID"):]
    except:
        SSID = "N/A"
    cpu = "sensors | head -n 3 | tail -n 1 | cut -d \" \" -f9"
    CPU = subprocess.check_output(cpu, shell=True)
    voltage = "dmesg | tail -n 1 | cut -d \" \" -f3,4"
    VOLTAGE = subprocess.check_output(voltage, shell=True)
    ssh = "ss | grep -i ssh | cut -d \" \" -f33"
    SSH = subprocess.check_output(ssh, shell=True)
    draw.text((0, 0), "GENERAL SYS STATS", font=font, fill=255)
    draw.text((0, 14), str(IP, 'utf-8'), font=font, fill=255)
    draw.text((0, 22), SSID, font=font, fill=255)
    draw.text((0, 30), str(CPU, 'utf-8'), font=font, fill=255)
    draw.text((0, 38), str(VOLTAGE, 'utf-8'), font=font, fill=255)
    draw.text((0, 46), str(SSH, 'utf-8'), font=font, fill=255)
    oled.image(img)
    oled.show()
    time.sleep(0.1)
