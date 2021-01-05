#!/bin/bash

######################################Aditional repositories

sudo add-apt-repository "deb http://security.ubuntu.com/ubuntu xenial-security main"
sudo add-apt-repository ppa:rock-core/qt4
sudo apt update

#####################################To support python2

sudo apt-get install python-dev python-numpy python-pip -y

######################################To support python3:

sudo apt-get install python3-dev python3-numpy python3-pip -y

###################################### Optional dependencies

sudo apt-get install libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqtgui4 libqt4-test

######################################Installing OpenCv


sudo pip3 install opencv-contrib-python==4.1.0.25
sudo pip install opencv-contrib-python==4.1.0.25

