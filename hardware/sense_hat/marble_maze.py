# based on https://www.raspberrypi.org/learning/sense-hat-marble-maze/worksheet/

from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

r = (255, 0, 0 )
b = (0,0,0)
w = (255, 255, 255 )

x = 1
y = 1

maze = [[r,r,r,r,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,r,r,b,r,b,b,r],
        [r,b,r,b,r,r,r,r],
        [r,b,b,b,b,b,b,r],
        [r,b,r,r,r,r,b,r],
        [r,b,b,r,b,b,b,r],
        [r,r,r,r,r,r,r,r]]

def move_marble(pitch, roll, x, y):
    new_x = x
    new_y = y
    if 1 < pitch < 179:
        new_x -= 1
    elif 359 > pitch > 181:
        new_x += 1
    return new_x, new_y

game_over = False

while not game_over:
    pitch = sense.get_orientation()['pitch']
    roll = sense.get_orientation()['roll']
    x,y = move_marble(pitch, roll, x, y)
    maze[y][x] = w
    sense.set_pixels(sum(maze,[]))

