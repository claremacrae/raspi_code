#!/bin/sh

# Taken from http://www.startpi.co.uk/getting-started-with-pi-face.html

sudo sed --in-place=backup -e '/^blacklist spi-bcm2708/ s/^/#/' /etc/modprobe.d/raspi-blacklist.conf

# Download and run the installation script - no longer needed
# wget http://pi.cs.man.ac.uk/download/install.txt

# Install python interfaces
sudo apt-get update
sudo apt-get install python3-pifacedigitalio python-pifacedigitalio -y

# Install the emulator and to use with scratch run 
sudo apt-get install python3-pifacedigital-emulator python3-pifacedigital-scratch-handler -y

echo "Now reboot with 'sudo reboot'"

