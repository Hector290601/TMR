# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.16

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/ubuntu/TMR/Hector/cpp/basics/perspectiva

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/ubuntu/TMR/Hector/cpp/basics/perspectiva

# Include any dependencies generated for this target.
include CMakeFiles/perspectiva.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/perspectiva.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/perspectiva.dir/flags.make

CMakeFiles/perspectiva.dir/main.cpp.o: CMakeFiles/perspectiva.dir/flags.make
CMakeFiles/perspectiva.dir/main.cpp.o: main.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/ubuntu/TMR/Hector/cpp/basics/perspectiva/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/perspectiva.dir/main.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/perspectiva.dir/main.cpp.o -c /home/ubuntu/TMR/Hector/cpp/basics/perspectiva/main.cpp

CMakeFiles/perspectiva.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/perspectiva.dir/main.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/ubuntu/TMR/Hector/cpp/basics/perspectiva/main.cpp > CMakeFiles/perspectiva.dir/main.cpp.i

CMakeFiles/perspectiva.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/perspectiva.dir/main.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/ubuntu/TMR/Hector/cpp/basics/perspectiva/main.cpp -o CMakeFiles/perspectiva.dir/main.cpp.s

# Object files for target perspectiva
perspectiva_OBJECTS = \
"CMakeFiles/perspectiva.dir/main.cpp.o"

# External object files for target perspectiva
perspectiva_EXTERNAL_OBJECTS =

perspectiva: CMakeFiles/perspectiva.dir/main.cpp.o
perspectiva: CMakeFiles/perspectiva.dir/build.make
perspectiva: /usr/local/lib/libopencv_gapi.so.4.5.3
perspectiva: /usr/local/lib/libopencv_highgui.so.4.5.3
perspectiva: /usr/local/lib/libopencv_ml.so.4.5.3
perspectiva: /usr/local/lib/libopencv_objdetect.so.4.5.3
perspectiva: /usr/local/lib/libopencv_photo.so.4.5.3
perspectiva: /usr/local/lib/libopencv_stitching.so.4.5.3
perspectiva: /usr/local/lib/libopencv_video.so.4.5.3
perspectiva: /usr/local/lib/libopencv_videoio.so.4.5.3
perspectiva: /usr/local/lib/libopencv_dnn.so.4.5.3
perspectiva: /usr/local/lib/libopencv_imgcodecs.so.4.5.3
perspectiva: /usr/local/lib/libopencv_calib3d.so.4.5.3
perspectiva: /usr/local/lib/libopencv_features2d.so.4.5.3
perspectiva: /usr/local/lib/libopencv_flann.so.4.5.3
perspectiva: /usr/local/lib/libopencv_imgproc.so.4.5.3
perspectiva: /usr/local/lib/libopencv_core.so.4.5.3
perspectiva: CMakeFiles/perspectiva.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/ubuntu/TMR/Hector/cpp/basics/perspectiva/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable perspectiva"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/perspectiva.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/perspectiva.dir/build: perspectiva

.PHONY : CMakeFiles/perspectiva.dir/build

CMakeFiles/perspectiva.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/perspectiva.dir/cmake_clean.cmake
.PHONY : CMakeFiles/perspectiva.dir/clean

CMakeFiles/perspectiva.dir/depend:
	cd /home/ubuntu/TMR/Hector/cpp/basics/perspectiva && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/ubuntu/TMR/Hector/cpp/basics/perspectiva /home/ubuntu/TMR/Hector/cpp/basics/perspectiva /home/ubuntu/TMR/Hector/cpp/basics/perspectiva /home/ubuntu/TMR/Hector/cpp/basics/perspectiva /home/ubuntu/TMR/Hector/cpp/basics/perspectiva/CMakeFiles/perspectiva.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/perspectiva.dir/depend

