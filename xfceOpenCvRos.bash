#!/bin/bash
echo "Empezando!"
apt-get update
apt autoremove
apt upgrade
##################################################SSH
echo "Instalando y habilitando SSH"
apt install openssh-server
systemctl enable openssh-server
systemctl start openssh-server
apt-get update
apt autoremove
apt upgrade
#################################################GUI
echo "Instalando escritorio Xfce"
apt install tasksel
apt-get install xubuntu-desktop
apt-get update
apt autoremove
apt upgrade
################################################Java
echo "Instalando Java"
apt install default-jre
apt install default-jdk
#################################################OpenCv
########################Cmake
echo "Instalando cmake"
apt-get install cmake
########################gcc y g++
echo "Instalando gcc y g++"
apt-get install gcc g++
########################Dependencias python 2 y 3
echo "Instalando dependencias python"
apt-get install python-dev python-numpy
apt-get install python3-dev python3-numpy
########################Dependencias Opencv
echo "Instalando "
apt-get install libavcodec-dev libavformat-dev libswscale-dev
apt-get install libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev
apt-get install libgtk2.0-dev
apt-get install libgtk-3-dev
apt-get install libpng-dev
apt-get install libjpeg-dev
apt-get install libopenexr-dev
apt-get install libtiff-dev
apt-get install libwebp-dev
apt-get install libavresample-dev
echo "Instalando git"
apt-get install git
echo "Clonando repositorio de Opencv"
git clone https://github.com/opencv/opencv.git
mkdir build
cd build
echo "Creando archivo swap"
dd if=/dev/zero of=/swapfile bs=64M count=16
mkswap /swapfile
swapon /swapfile
echo "Compilando openCv"
cmake ../ -DENABLE_PRECOMMPILED_HEADERS=OFF
make
echo "Instalando compilado de OpenCv"
make install
#################################################ROS
echo "Instalando ROS"
sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | apt-key add -
apt update
echo "Instalando ROS Noetic Desktop"
apt install ros-noetic-desktop
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
apt-get install python3-pandas
pip3 install hypothesis
##################################################Instalar matplotlib
echo "Instalando Matplotlib"
python3 -m pip install -U matplotlib
apt install libfreetype6-dev
apt install pkg-config
##################################################Instalar VIM
echo "Instalando Vim"
apt-get install vim
##################################################Ultimo Paso
apt update
apt upgrade
