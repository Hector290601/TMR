from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from time import sleep
import socket
import busio
import subprocess
from RPi_GPIO_Rotary import rotary

count = 0
exit = False

def network_info():
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
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((0, 0), "NETWORK INFO", fill=255)
        draw.text((0, 14), str(IP, 'utf-8'), fill=255)
        draw.text((0, 22), SSID, fill=255)

def ssh_info():
    with canvas(device) as draw:
        cmd = "w | head -n 4 | tail -n 3 | tr -s ' ' | cut -d ' ' -f 3"
        try:
            cmd_output = subprocess.check_output(cmd, shell=True)
        except:
            cmd_output = "N/A"
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((0, 0), "SSH INFO", fill=255)
        draw.text((0, 14), str(cmd_output, 'utf-8'), fill=255)

def top():
    with canvas(device) as draw:
        cmd = "ps aux --sort -rss --width 30 | head -n5 | tr -s ' ' | cut -d ' ' -f 3,4,11 | cut -d '/' -f1,4,5,6"
        try:
            cmd_output = subprocess.check_output(cmd, shell=True)
        except:
            cmd_output = "N/A"
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((0, 0), "PROCCESS INFO", fill=255)
        draw.text((0, 8), str(cmd_output, 'utf-8'), fill=255)

def ros_topics_info():
    with canvas(device) as draw:
        cmd = "rostopic list"
        try:
            cmd_output = subprocess.check_output(cmd, shell=True)
        except:
            cmd_output = "N/A"
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((0, 0), "ROS TOPIC INFO", fill=255)
        draw.text((0, 8), str(cmd_output, 'utf-8'), fill=255)

def run_no_obstacles():
    with canvas(device) as draw:
        cmd = "roslaunch pumas_hm no_obstacles.launch"
        try:
            cmd_output = subprocess.check_output(cmd, shell=True)
        except:
            cmd_output = "N/A"
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        draw.text((0, 0), "Run no obstacles", fill=255)
        draw.text((0, 8), str(cmd_output, 'utf-8'), fill=255)
    

functions = [
        network_info,
        ssh_info,
        top,
        ros_topics_info,
        run_no_obstacles
        ]

def buttonPushed():
    global count, execute
    if execute == options:
        execute = functions[count]
    else:
        execute = options
    print("Button")

def valueChanged(cnt):
    global count
    new = cnt
    if -1 < new < 8:
        count = new

rot = rotary.Rotary(23, 24, 25, 1)

rot.register(pressed=buttonPushed, onchange=valueChanged)

rot.start()

serial = i2c(port=1, address=0x3C)
device = sh1106(serial, width=128, height=64, rotate=0)

main_menu = [
        "Network info",
        "Ssh info",
        "TOP",
        "Ros topics",
        "No Obstacles",
        "future2",
        "future3",
        "future4",
        ]

def options():
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        for i in range(len(main_menu)):
            if i == count:
                draw.text((0, 8 * i), " * " + main_menu[i], fill=255)
            else:
                draw.text((0, 8 * i), main_menu[i], fill=255)

execute = options

def home():
    global exit
    while not exit:
        execute()
        sleep(0.1)

"""
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
        draw.text((0, 54), str(count), fill=255)
    sleep(0.1)

"""

if __name__ == "__main__":
    home()
rot.stop()
