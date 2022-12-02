sudo rm -rf .local/lib/python3.5
sudo rm -rf /usr/local/lib/python3.5/dist-packages/sklearn
sudo rm -rf /usr/local/lib/python3.5/dist-packages/scikit_learn*
sudo apt-get -y install python3-sklearn
pip install "git+https://github.com/bblais/Game" --upgrade
pip install "git+https://github.com/bblais/Robot373" --upgrade
pip install "git+https://github.com/bblais/classy" --upgrade
