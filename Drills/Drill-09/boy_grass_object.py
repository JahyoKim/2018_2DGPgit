from pico2d import *
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700),90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = random.randint(0,7)
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)


class Ball:
    def __init__(self):
        self.x, self.y = random.randint(50, 750), 600
        self.smallBall = load_image('ball21x21.png')
        self.bigBall = load_image('ball41x41.png')
        self.type = random.randint(0,1)

    def update(self):
        self.y -= 5

    def draw(self):
        if self.type % 2 == 0:
            self.smallBall.draw(self.x, self.y)
        elif self.type % 2 == 1:
            self.bigBall.draw(self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()

grass = Grass()
boy = Boy()
team = [Boy() for i in range(11)]

running = True

while running:
    handle_events()

    for boy in team:
        boy.update()
    clear_canvas()
    for boy in team:
        boy.draw()
        grass.draw()
    boy.draw()
    update_canvas()

    delay(0.05)

close_canvas()