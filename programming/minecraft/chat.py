import sys
sys.path.append( "/home/pi/mcpi/api/python" )

# Create a message

import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
prompt = "Enter a message (or '/exit' to quit): "

chatMsg = raw_input( prompt )

while chatMsg != "/exit":
    mc.postToChat( chatMsg )
    chatMsg = raw_input( prompt )
