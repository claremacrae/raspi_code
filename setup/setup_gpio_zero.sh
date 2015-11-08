#!/bin/sh
# From https://github.com/RPi-Distro/python-gpiozero

# First, install the dependencies:
sudo apt-get install python-pip python3-pip python-w1thermsensor python3-w1thermsensor python-spidev python3-spidev -y

# Install with pip:
sudo pip install gpiozero
sudo pip-3.2 install gpiozero
