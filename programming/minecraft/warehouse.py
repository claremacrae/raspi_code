import sys
sys.path.append( "/home/pi/mcpi/api/python" )

# Create a building shell - fully enclosed

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

block = 4
air = 0
x = 10
y = 11
z = 12

x2 = x + 10
y2 = y + 5
z2 = z + 8

mc.setBlocks( x, y, z, x2, y2, z2, block)
mc.setBlocks( x + 1, y + 1, z + 1, x2 - 1, y2 - 1, z2 - 1, air )
