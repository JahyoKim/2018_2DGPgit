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
        self.frame +=1
        if self.frame == 4:
            self.frame = 0
        self.frame_2 +=1
        if self.frame_2 == 2:
            self.frame_2 = 0

        if self.state == "jump" and self.jump_state == "up":
            if self.y >= 260:
                self.jump_state = "down"
            self.y += 10

        if self.state == "jump" and self.jump_state == "down":
            if self.y >= 200:
                self.y -= 10

        if self.state == "jump" and self.y == 200:
            self.state = "run"
            self.jump_state = "up"

        if self.state == "slide":
            self.y = 190


    def draw(self):
        if self.state == "run":
            self.run.clip_draw(self.frame * 100, 0, 100, 62, self.x, self.y)
        elif self.state == "jump":
            self.jump.clip_draw(self.frame_2 * 90, 0, 90, 63, self.x, self.y)
        elif self.state == "slide":
            self.slide.clip_draw(self.frame_2 * 97, 0, 96, 40, self.x, self.y)



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
