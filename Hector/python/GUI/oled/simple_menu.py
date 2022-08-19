#! /usr/bin/python3
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306, ssd1325, ssd1331, sh1106
from time import sleep
import socket
import busio
import subprocess
from RPi_GPIO_Rotary import rotary
import roslaunch
import rospy
import os

count = 0
exit = False
rcore = False
launched = None

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
    global rcore
    if rcore:
        with canvas(device) as draw:
            cmd = "rostopic list"
            try:
                cmd_output = subprocess.check_output(cmd, shell=True)
            except:
                cmd_output = "N/A"
            draw.rectangle(device.bounding_box, outline="white", fill="black")
            draw.text((0, 0), "ROS TOPIC INFO", fill=255)
            draw.text((0, 8), str(cmd_output, 'utf-8'), fill=255)
    else:
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="white", fill="black")
            draw.text((0, 0), "ROS TOPIC INFO", fill=255)
            draw.text((0, 8), "No roslaunch running", fill=255)

def run_no_obstacles():
    global rcore, launched
    if not rcore:
        with canvas(device) as draw:
            """
            cmd = "roslaunch pumas_hm no_obstacles.launch"
            try:
                cmd_output = subprocess.check_output(cmd, shell=True)
                rcore = True
            except:
                cmd_output = "Something failed"
                rcore = False
            """
            rospy.init_node("no_obstacles_main", anonymous=True)
            uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
            roslaunch.configure_logging(uuid)
            launch = roslaunch.parent.ROSLaunchParent(uuid, ["/home/ubuntu/TMR/catkin_ws/src/pumas_hm_2022/launch/no_obstacles.launch"])
            launch.start()
            rospy.loginfo("started")
            launched = launch
            rcore = True
            draw.rectangle(device.bounding_box, outline="white", fill="black")
            draw.text((0, 0), "Run no obstacles", fill=255)
            draw.text((0, 8), "launched", fill=255)
    else:
        cmd = "if rostopic list | grep -q '/raw_lanes_left'; then   echo \"matched\"; fi"
        try:
            cmd_output = subprocess.check_output(cmd, shell=True)
        except:
            cmd_output = "Still no response"
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="white", fill="black")
            draw.text((0, 0), "Run no obstacles", fill=255)
            draw.text((0, 8), str(cmd_output, 'utf-8'), fill=255)

def kill():
    global launched
    if launched is not None:
        launched.shutdown()
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="white", fill="black")
            draw.text((0, 0), "Kill launched node", fill=255)
            draw.text((0, 8), "killing", fill=255)
    else:
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="white", fill="black")
            draw.text((0, 0), "Kill launched node", fill=255)
            draw.text((0, 8), "killed or nothing to kill", fill=255)
    launched = None

def selfkill():
    os.kill(os.getpid(), 9)

def sdown():
    os.system("sudo shutdown now | Ha05rm06")

def future1():
    print("future1")

def future2():
    print("future2")

def future3():
    print("future3")

def future4():
    print("future4")

def future5():
    print("future5")

def future6():
    print("future6")

def future7():
    print("future7")

def future8():
    print("future8")

def future9():
    print("future9")

def future10():
    print("future10")

"""
functions = [
        network_info,
        ssh_info,
        top,
        ros_topics_info,
        run_no_obstacles,
        kill,
        selfkill,
        sdown
        ]
"""

def buttonPushed():
    global count, execute, start, end
    fun = list(functions.values())[start:end]
    if execute == options:
        execute = fun[count-start]
    else:
        execute = options

def cwTurn():
    global count, ln
    new = count + 1
    if -1 < new < ln:
        count = new

def ccwTurn():
    global count, ln
    new = count - 1
    if -1 < new < ln:
        count = new

rot = rotary.Rotary(23, 24, 25, 1)


rot.register(increment=cwTurn, decrement=ccwTurn)
rot.register(pressed=buttonPushed)
rot.start()

serial = i2c(port=1, address=0x3C)
device = sh1106(serial, width=128, height=64, rotate=0)

"""
main_menu = [
        "Network info",
        "Ssh info",
        "TOP",
        "Ros topics",
        "No Obstacles",
        "kill " + str(launched),
        "self kill",
        "shutdown",
        ]
"""

functions = {
        "Network info" : network_info,
        "Ssh info" : ssh_info,
        "TOP" : top,
        "Ros topics" : ros_topics_info,
        "No Obstacles" : run_no_obstacles,
        "kill " + str(launched) : kill,
        "self kill" : selfkill,
        "shutdown" : sdown,
        "future1" :future1,
        "future2" :future2,
        "future3" :future3,
        "future4" :future4,
        "future5" :future5,
        "future6" :future6,
        "future7" :future7,
        "future8" :future8,
        "future9" :future9,
        "future10" :future10,
        }

def options():
    global start, end, functions, ln
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
        ln = len(functions)
        start = 0 if count < 7 else count -4
        end = 8 if count < 7 else count + 4 if count + 4 < ln else ln
        main_menu = list(functions.keys())[start:end]
        for i in range(len(main_menu)):
            if i == count - start:
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
