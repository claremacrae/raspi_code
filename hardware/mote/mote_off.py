from mote import Mote

def turn_off_lights():
    mote = Mote()

    mote.configure_channel(1, 16, False)
    mote.configure_channel(2, 16, False)
    mote.configure_channel(3, 16, False)
    mote.configure_channel(4, 16, False)

    mote.clear()
    mote.show()

if __name__ == "__main__":
    turn_off_lights()
