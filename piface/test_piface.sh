#!/bin/sh

piface_examples_dir=/usr/share/doc/python-pifacedigitalio/examples

echo "available examples - run with python:"
find   $piface_examples_dir -type f

echo "\nAn LED should now blink - hit CTRL+C to stop it"
python $piface_examples_dir/blink.py

