#/bin/bash

output=$(ls /dev/input/js* 2> /dev/null | wc -w)
while [ "$output" = "0" ]
do
		output=$(ls /dev/input/js* 2> /dev/null | wc -w)
		sleep 0.5
done
if ! [ "$output" = "0" ]
then
		ros2 run toxic_hardware automate
fi
