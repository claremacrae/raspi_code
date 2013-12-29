#!/bin/sh

# Taken from http://www.recantha.co.uk/blog/?p=2582

sudo apt-get install i2c-tools
sudo sed --in-place=backup -e '/^blacklist i2c-bcm2708/ s/^/#/' /etc/modprobe.d/raspi-blacklist.conf

# TODO Change these so they actually edit the file
grep -q '^i2c-bcm2708' /etc/modules || echo 'ERROR Add i2c-bcm2708 to /etc/modules'
grep -q '^i2c-dev'     /etc/modules || echo 'ERROR Add i2c-dev     to /etc/modules'

# To allow use of I2C with python:
sudo apt-get install python-smbus python-psutil -y

# Taken from https://github.com/Boeeerb/PiGlow
wget https://raw.github.com/Boeeerb/PiGlow/master/piglow.py
wget https://raw.github.com/Boeeerb/PiGlow/master/Examples/test.py

echo Now reboot the pi

