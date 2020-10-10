#!/bin/bash
echo "Empezando!"
sudo apt-get update
sudo apt autoremove
sudo apt upgrade
##################################################SSH
echo "Instalando y habilitando SSH"
sudo apt install openssh-server
sudo systemctl enable openssh-server
sudo systemctl start openssh-server
sudo apt-get update
sudo apt autoremove
sudo apt upgrade
#################################################GUI
echo "Instalando escritorio Xfce"
sudo apt install tasksel
sudo apt-get install xubuntu-desktop
sudo apt-get update
sudo apt autoremove
sudo apt upgrade
################################################Java
echo "Instalando Java"
sudo apt install default-jre
sudo apt install default-jdk
#################################################OpenCv
########################Cmake
echo "Instalando cmake"
sudo apt-get install cmake
########################gcc y g++
echo "Instalando gcc y g++"
sudo apt-get install gcc g++
########################Dependencias python 2 y 3
echo "Instalando dependencias python"
sudo apt-get install python-dev python-numpy
sudo apt-get install python3-dev python3-numpy
########################Dependencias Opencv
echo "Instalando "
sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev
sudo apt-get install libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev
sudo apt-get install libgtk2.0-dev
sudo apt-get install libgtk-3-dev
sudo apt-get install libpng-dev
sudo apt-get install libjpeg-dev
sudo apt-get install libopenexr-dev
sudo apt-get install libtiff-dev
sudo apt-get install libwebp-dev
sudo apt-get install libavresample-dev
echo "Instalando git"
sudo apt-get install git
echo "Clonando repositorio de Opencv"
git clone https://github.com/opencv/opencv.git
mkdir build
cd build
echo "Creando archivo swap"
sudo dd if=/dev/zero of=/swapfile bs=64M count=16
sudo mkswap /swapfile
sudo swapon /swapfile
echo "Compilando openCv"
cmake ../ -DENABLE_PRECOMMPILED_HEADERS=OFF
make
echo "Instalando compilado de OpenCv"
sudo make install
#################################################ROS
echo "Instalando ROS"
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | sudo apt-key add -
sudo apt update
echo "Instalando ROS Noetic Desktop"
sudo apt install ros-noetic-desktop
source /opt/ros/noetic/setup.bash
source /opt/ros/noetic/setup.bash
source ~/.bashrc
###################################################Verificar ROS
echo "Verificando Instalacion de ROS Neotic"
printenv | grep ROS
source /opt/ros/noetic/setup.bash
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make -DPYTHON_EXECUTABLE=/usr/bin/python3
source devel/setup.bash
echo $ROS_PACKAGE_PATH
##################################################Instalar pip
echo "Instalando pip para python3"
python3 -m pip install -U pip
##################################################Instalar pandas
echo "Instalando Pandas"
sudo apt-get install python3-pandas
sudo pip3 install hypothesis
##################################################Instalar matplotlib
echo "Instalando Matplotlib"
python3 -m pip install -U matplotlib
sudo apt install libfreetype6-dev
sudo apt install pkg-config
##################################################Instalar VIM
echo "Instalando Vim"
sudo apt-get install vim
##################################################Ultimo Paso
sudo apt update
sudo apt upgrade
