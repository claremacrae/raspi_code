#!/usr/bin/env python
import unicornhathd
import os

try:
    unicornhathd.set_pixel(0, 0, 255, 255, 255)
    unicornhathd.set_pixel(15, 0, 255, 255, 255)
    unicornhathd.set_pixel(0, 15, 255, 255, 255)
    unicornhathd.set_pixel(15, 15, 255, 255, 255)
    unicornhathd.show()
    raw_input("Press the <ENTER> key or <CTRL+C> to exit...")
except KeyboardInterrupt:
    pass
unicornhathd.off()
