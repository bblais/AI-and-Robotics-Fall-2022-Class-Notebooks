#!/bin/sh 
echo "Starting: `date`"
ssh pi@dex.local /bin/bash <<'ENDSSH'
#commands to run on remote host

echo "update start: `date`" >> setup_brick.log
sudo apt-get -y update
echo "update end: `date`" >> setup_brick.log


echo "full upgrade start: `date`" >> setup_brick.log
sudo apt-get -y full-upgrade
echo "full upgrade end: `date`" >> setup_brick.log

echo "apt-get start: `date`" >> setup_brick.log
sudo apt-get -y install fswebcam
sudo apt-get -y install libatlas-base-dev
sudo apt-get -y install python3-matplotlib python3-pandas python3-scipy ipython3 python3-audioread python3-biopython
sudo apt-get -y install realvnc-vnc-server
sudo systemctl start vncserver-virtuald.service
sudo systemctl enable vncserver-virtuald.service
echo "apt-get end: `date`" >> setup_brick.log



echo "pip3 start: `date`" >> setup_brick.log
sudo pip3 install scikit-learn
pip3 install "git+https://github.com/bblais/NumpyNet" --upgrade
pip3 install "git+https://github.com/bblais/Robot373" --upgrade
pip3 install "git+https://github.com/bblais/Game" --upgrade
pip3 install "git+https://github.com/bblais/classy" --upgrade
sudo pip3 install tqdm 
echo "pip3 end: `date`" >> setup_brick.log

echo "misc start: `date`" >> setup_brick.log
git -C Documents clone "https://github.com/bblais/Robot373"
mkdir python
cp Documents/Robot373/Examples/motorAB_test.py python
sudo rm /usr/bin/python
sudo ln -s /usr/bin/python3.5 /usr/bin/python
echo "misc end: `date`" >> setup_brick.log
exit
ENDSSH

echo "Remember to:"
echo "ssh pi@dex.local"
echo "sudo raspi-config"
echo "    - advanced/expand filesystem"
echo "    - localization/timezone"
echo " "
echo "Ending: `date`"

# sudo shutdown -h now