from pico2d import *

class Jungle:
    image_init = None

    def __init__(self):
        self.x = 100
        self.y = 200
        self.frame = 0
        self.frame_2 = 0
        self.state = "run"
        self.jump_state = "up"
        self.slide_state = "slide"

        if self.image_init == None:
            self.run = load_image('jungle_run.png')
            self.jump = load_image('jungle_jump.png')
            self.slide = load_image('jungle_slide.png')

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