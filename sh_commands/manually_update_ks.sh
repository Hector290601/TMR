#!/bin/sh
echo CRETING BYOBU SESSIONS
byobu new-session -d -s $USER

echo DIVIDING FIRST WINDOW
# Creating windows
byobu rename-window -t $USER:0 'vitalNodes'
byobu split-window -v
byobu split-window -v
byobu split-window -v
byobu select-pane -t 1
byobu split-window -v
byobu select-pane -t 0
byobu split-window -v
byobu select-pane -t 0
byobu split-window -v


echo LAUNCHING VITAL NODES
# Launching vital nodes
byobu select-pane -t 0
byobu send-keys "ros2 run toxic_vision webcam_publisher" C-m
byobu select-pane -t 1
byobu send-keys "ros2 run toxic_vision lane_detector" C-m
byobu select-pane -t 2
byobu send-keys "ros2 run toxic_vision lane_tracker" C-m
byobu select-pane -t 3
byobu send-keys "ros2 run joy_linux joy_linux_node" C-m
byobu select-pane -t 4
byobu send-keys "ros2 run toxic_hardware controller" C-m
byobu select-pane -t 6
byobu send-keys "ros2 run toxic_hardware motor_interface" C-m

