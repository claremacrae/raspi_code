#!/bin/sh

cd ~/Pictures/Christmas || echo "Error - run ~develop/raspi_code/setup/download_sample_pictures.sh"
sudo fbi -T 2 -d /dev/fb1 -noverbose -a -t 2 -u *.jpg
