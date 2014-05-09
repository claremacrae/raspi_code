import sys
sys.path.append( "/home/pi/mcpi/api/python" )

# Create a swimming pool

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

block = 4
water = 8

x = 15 # left and right
y = 15 # up and down
z = 15 # back and fowards

x2 = x + 10
y2 = y + 5
z2 = z + 8

mc.setBlocks( x, y, z, x2, y2, z2, block)
mc.setBlocks( x + 1, y + 1, z + 1, x2 - 1, y2, z2 - 1, water )

mc.player.setPos( x-5, y, z-5 )
