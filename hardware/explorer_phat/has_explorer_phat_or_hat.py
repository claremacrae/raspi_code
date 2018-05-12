#!/usr/bin/env python
# coding: Latin-1

from explorerhat import motor

# If ImportError raised, the library is not installed
# If python exits with the following, then the device is not connected:
# 	Warning, could not find Analog or Touch...
#	Please check your i2c settings!

# On exit:
#	$? is 0 if library and device are available.
#	$? is 1 otherwise.
