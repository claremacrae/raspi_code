"""
A script to show off certain Raspberry Pi features automatically,
without needing to interact with the Pi to start commands.

I'm intending this to be run at startup, perhaps if no keyboard
is connected?

To run this automatically, see
http://www.raspberrypi-spy.co.uk/2013/07/running-a-python-script-at-boot-using-cron/

Add this line to the root contab file
@reboot python /home/pi/develop/raspi_code/demo/demo_my_pi.py --keyboard_check &
"""

import os.path
import sys
import subprocess

hat_product_file = "/proc/device-tree/hat/product"

def get_hat_name():
    if not os.path.exists(hat_product_file):
        return None

    with file(hat_product_file) as f:
        line = f.read()
        return line

def is_keyboard_attached():
    # From http://stackoverflow.com/a/8265634
    import subprocess
    df = subprocess.check_output("lsusb", shell=True)
    return 'keyboard' in df.lower()

if '--keyboard_check' in sys.argv and is_keyboard_attached():
    print "Keyboard attached - skipping demo"
    sys.exit()

hat_name = get_hat_name()
if not hat_name:
    print "No HAT connected"
    sys.exit()
print hat_name

script_name = None
if hat_name.startswith("Unicorn HAT"):
    script_name = "/home/pi/Pimoroni/unicornhat/rainbow.py"

print script_name
if os.path.exists(script_name):
    subprocess.call(['sudo', 'python', script_name])
