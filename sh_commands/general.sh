#/bin/bash
$1 &
if ! pgrep -x $2 > /dev/null
then
		ros2 run $1 $2 &
fi
