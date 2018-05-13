#!/usr/bin/python
# -*- coding: UTF-8 -*-
from __future__ import print_function

# Imported from https://github.com/PiSupply/PiJuice/issues/105

import time
from pijuice import PiJuice

# ---
pijuice = PiJuice(1,0x14)

print(time.strftime( "%Y%m%d%H%M%S", time.localtime( time.time() ) ) )

firmware = pijuice.config.GetFirmwareVersion()
if firmware['error'] == 'NO_ERROR':
   fvers = firmware['data']
   print('firmware: V', fvers['version'], '-', fvers['variant'])
else:
   print('firmware: ', firmware['error'])

charge = pijuice.status.GetChargeLevel()
if charge['error'] == 'NO_ERROR':
   charge = charge['data']
   print('  charge: ', charge, '%')
else:
   print('  charge: ', charge['error'])

temp =  pijuice.status.GetBatteryTemperature()
if temp['error'] == 'NO_ERROR':
   temp = temp['data']
   print('    temp: ', temp, '°C')
else:
   print('    temp: ', temp['error'])

vio =  pijuice.status.GetIoVoltage()
if vio['error'] == 'NO_ERROR':
   vio = vio['data']
   print('  iovolt: ', float(vio)/1000.0, 'V')
else:
   print('     vio: ', vio['error'])
