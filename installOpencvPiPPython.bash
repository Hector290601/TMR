#!/bin/bash

######################################Aditional repositories

sudo add-apt-repository "deb http://security.ubuntu.com/ubuntu xenial-security main"
sudo add-apt-repository ppa:rock-core/qt4
sudo apt update

######################################Required build dependencies

sudo apt-get install cmake -y
sudo apt-get install gcc g++ -y

#####################################To support python2

sudo apt-get install python-dev python-numpy -y

######################################To support python3:

sudo apt-get install python3-dev python3-numpy -y

######################################GTK SUPPORT
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev -y
sudo apt-get install libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev -y

######################################To support GTK2

sudo apt-get install libgtk2.0-dev

######################################To support GTK3

sudo apt-get install libgtk-3-dev

###################################### Optional dependencies

sudo apt-get install libpng-dev -y
sudo apt-get install libjpeg-dev -y
sudo apt-get install libopenexr-dev -y
sudo apt-get install libtiff-dev -y
sudo apt-get install libwebp-dev -y
sudo apt-get install libhdf5-dev libhdf5-serial-dev libatlas-base-dev libjasper-dev libqtgui4 libqt4-test

######################################Downloading OpenCv

sudo apt-get install git -y
git clone https://github.com/opencv/opencv.git
cd opencv
mkdir build
cd build

###################################### Configuring and installing

cmake ../
make
sudo make install

