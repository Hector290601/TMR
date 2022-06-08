#! /bin/bash

result=`ps aux | grep -i "/home/ubuntu/TMR/Hector/python/GUI/oled/simple_menu.py" | grep -v "grep" | wc -l`
if [ $result -ge 1 ]
	   then
		   echo "script is running"
	   else
		   -E python3 /home/ubuntu/TMR/Hector/python/GUI/oled/simple_menu.py &
fi
