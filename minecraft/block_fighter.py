import sys
sys.path.append( "/home/pi/mcpi/api/python" )

# Give player 60 seconds to hit blocks with swordss, then count  hits

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

mc.postToChat( "Hit with right mouse to gain points" )

import time
time.sleep( 60 )
points = 0

hits = mc.events.pollBlockHits()

for hit in hits:
    x = hit.pos.x
    y = hit.pos.y
    z = hit.pos.z
    print x, y, z
    block = mc.getBlock( x, y, z )
    points = points + block

mc.postToChat( "You got " + str(points) + " points." )

