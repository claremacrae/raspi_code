#!/bin/sh

# From http://nodered.org/docs/hardware/raspberrypi.html

# Install Node.js
curl -sL https://deb.nodesource.com/setup_0.10 | sudo bash -
sudo apt-get install -y build-essential python-dev python-rpi.gpio nodejs

# Install Node-RED
sudo npm install -g --unsafe-perm  node-red

# Install some extra nodes
cd ~/.node-red
npm install node-red-node-pibrella

# Start the server
node-red-pi --max-old-space-size=128

# Load page in browser
hostname -I
# e.g. http://172.17.14.116:1880/#
http://localhost:1880/#
