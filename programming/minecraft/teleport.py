import sys
sys.path.append( "/home/pi/mcpi/api/python" )

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

x = 10
y = 11
z = 12
mc.player.setPos( x, y, z )
