#!/bin/sh

date

cd ~/develop/sonic-pi

# Compile the server extensions by cding into the directory 
cd app/server/bin
./compile-extensions.rb
cd ../../..

# Qt GUI
cd app/gui/qt/
./rp-build-app
cd ../../..

# Run
cd app/gui/qt/
./rp-app-bin

date
