cmake_minimum_required(VERSION 3.0.2)
project(parking)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
)

catkin_package(
)

include_directories(
# include
  ${catkin_INCLUDE_DIRS}
)

catkin_install_python(PROGRAMS
  scripts/lane_detector_canny_hough.py
  scripts/lane_tracking.py
  scripts/obstacle_detection.py
  scripts/parking.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
