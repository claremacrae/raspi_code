from piglow import PiGlow
import time

def brighten_arm( arm ):

    for i in range( 1, 10 ):
        piglow.arm( arm, i )
        time.sleep( 0.11 )

    time.sleep( 0.5 )
    piglow.arm( arm, 0 )

piglow = PiGlow()

piglow.all(0)

brighten_arm( 1 )
brighten_arm( 2 )
brighten_arm( 3 )

