sudo apt update
sudo apt install -y python3-pip git python3-dev python3-libgpiod ffmpeg
git clone https://github.com/itsactuallyluna9/EC-Robot-Project
cd EC-Robot-Project
git config pull.rebase false
sudo -H python3 -m venv ./venv
sudo -H /home/c4/EC-Robot-Project/venv/bin/python3 -m pip install -e '.[physical]'
sudo cp -v ./bin/robot-project.service /lib/systemd/system/
sudo systemctl enable robot-project.service
sudo reboot now
