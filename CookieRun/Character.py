from pico2d import *

class Jungle:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

open_canvas()
jungle = Jungle()
running = True

while running:
    handle_events()
    jungle.update()

    clear_canvas()
    jungle.draw()
    update_canvas()
    delay(0.05)


close_canvas()