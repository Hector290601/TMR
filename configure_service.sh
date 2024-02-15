#/bin/bash
sudo cp ./pumas_autonomous_car.service /etc/systemd/system/pumas_autonomous_car.service
sudo cp ./sh_commands/waker_up.sh /usr/bin/pumas_autonomous_car_waker_up.sh
sudo systemctl daemon-reload
sudo systemctl enable pumas_autonomous_car.service
