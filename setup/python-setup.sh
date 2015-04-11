#!/bin/sh
apt-get install python-pip -y
apt-get install python3-pip -y
apt-get install python-dev

pip install pillow
easy_install -U distribute
pip install matplotlib
pip install nose

# to test:     python
# >>> import numpy
# >>> import matplotlib
# >>> import nose
