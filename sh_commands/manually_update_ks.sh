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


echo CREATING SECOND WINDOW
# Creating new window to debug data
byobu new-window -t $USER:1 -n 'debugs'

echo DIVING SECOND WINDOW
# Splitting windows
byobu split-window -v
byobu split-window -v
byobu split-window -v
byobu select-pane -t 1
byobu split-window -v
byobu select-pane -t 0
byobu split-window -v
byobu select-pane -t 0
byobu split-window -v

# Splitting horizontally windows
byobu select-pane -t 0
byobu split-window -h
byobu select-pane -t 2
byobu split-window -h
byobu select-pane -t 4
byobu split-window -h
byobu select-pane -t 6
byobu split-window -h
byobu select-pane -t 8
byobu split-window -h
byobu select-pane -t 10
byobu split-window -h
byobu select-pane -t 12
byobu split-window -h

byobu select-window -t 0

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
byobu select-pane -t 5
byobu send-keys "ros2 run toxic_hardware servo_interface" C-m
byobu select-pane -t 6
byobu send-keys "ros2 run toxic_hardware motor_interface" C-m

byobu select-window -t 1

echo LAUNCHING DEBUGS
byobu select-pane -t 0
byobu send-keys "ros2 topic echo /speed" C-m
byobu select-pane -t 1
byobu send-keys "ros2 topic echo /steering" C-m
byobu select-pane -t 2
byobu send-keys "ros2 topic hz /speed" C-m
byobu select-pane -t 3
byobu send-keys "ros2 topic hz /steering" C-m
byobu select-pane -t 4
byobu send-keys "ros2 topic echo /lines/left" C-m
byobu select-pane -t 5
byobu send-keys "ros2 topic echo /lines/right" C-m
byobu select-pane -t 6
byobu send-keys "ros2 topic hz /lines/left" C-m
byobu select-pane -t 7
byobu send-keys "ros2 topic hz /lines/right" C-m
byobu select-pane -t 8
byobu send-keys "ros2 topic echo /k/rho" C-m
byobu select-pane -t 9
byobu send-keys "ros2 topic echo /k/theta" C-m
byobu select-pane -t 10
byobu send-keys "ros2 topic hz /k/rho" C-m
byobu select-pane -t 11
byobu send-keys "ros2 topic hz /k/theta" C-m
byobu select-pane -t 12
byobu send-keys "ros2 topic echo /max_speed" C-m
byobu select-pane -t 13
byobu send-keys "ros2 topic hz /max_speed" C-m

echo SYSTEM STARTED, ENTERING BYOBU SESSION
sleep 0.5
byobu attach-session -t $USER

