from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from time import sleep
import socket
import busio
import subprocess

#decodigo.com

serial = i2c(port=1, address=0x3C)
#device = ssd1306(serial, rotate=0)
device = sh1106(serial, width=128, height=64, rotate=0)

#device.capabilities(width=128, height=64, rotate=0)
print("size: " , device.bounding_box)

while True:
    #device.clear()
    with canvas(device) as draw:
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
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((0, 0), "GENERAL SYS STATS", fill=255)
        draw.text((0, 14), str(IP, 'utf-8'), fill=255)
        draw.text((0, 22), SSID, fill=255)
        draw.text((0, 30), str(CPU, 'utf-8'), fill=255)
        draw.text((0, 38), str(VOLTAGE, 'utf-8'), fill=255)
        draw.text((0, 46), str(SSH, 'utf-8'), fill=255)
    sleep(0.1)
