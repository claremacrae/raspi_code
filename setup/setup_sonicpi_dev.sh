#!/bin/sh

# from https://github.com/samaaron/sonic-pi/blob/master/INSTALL.md#raspberry-pi

for dep in supercollider ruby1.9.3 libqscintilla2-8 libqscintilla2-dev qt4-dev-tools cmake ruby-dev libffi-dev ; do
    echo $dep
    sudo apt-get -y install $dep
done

cd ~
mkdir -p develop
cd       develop

git clone https://github.com/claremacrae/sonic-pi.git
