#!/bin/sh

# From http://nodered.org/docs/hardware/raspberrypi.html

# Start the server
node-red-pi --max-old-space-size=128

# Load page in browser
hostname -I
# e.g. http://172.17.14.116:1880/#
http://localhost:1880/#
