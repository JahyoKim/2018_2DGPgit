from pico2d import *
#import Background

class Jungle:
    image_init = None

    def __init__(self):
        self.x = 200
        self.y = 200
        self.frame = 0
        self.frame_2 = 0
        self.state = "run"
        self.jump_state = "up"
        self.slide_state = "slide"

        if self.image_init == None:
            self.run = load_image('sprite\\jungle_run.png')
            self.jump = load_image('sprite\\jungle_jump.png')
            self.slide = load_image('sprite\\jungle_slide.png')


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

class Jelly:
    image_init = None

    def __init__(self):
        self.x = 200
        self.y = 300
        self.frame = 0

        if self.image_init == None:
            self.life_jelly = load_image('sprite\\life_jelly.png')

    def update(self):
        self.frame +=1
        if self.frame == 2:
            self.frame = 0

    def draw(self):
        self.life_jelly.clip_draw(self.frame * 72, 0, 72, 70, self.x, self.y)



class Hurdle:
    image_init = None

    def __init__(self):
        self.x = 200
        self.y = 400
        self.frame = 0

        if self.image_init == None:
            self.hurdle1_1 = load_image('sprite\\hurdle1-1.png')

    def update(self):
        pass

    def draw(self):
        #self.draw(self.x, self.y)
        pass




def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_z:
                jungle.state = "jump"
            elif event.type == SDL_KEYDOWN and event.key == SDLK_x:
                if jungle.state != "jump":
                    jungle.state = "slide"
            elif event.type == SDL_KEYUP and event.key == SDLK_x:
                if jungle.state == "slide":
                    jungle.state = "run"
                    jungle.y = 200
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                running = False



open_canvas()
jungle = Jungle()
jelly = Jelly()
hurdle = Hurdle()
#background = Background()

running = True

while running:
    handle_events()
    jungle.update()
    #background.update()
    jelly.update()

    clear_canvas()
    jungle.draw()
    #background.draw()
    jelly.draw()
    hurdle.draw()
    update_canvas()
    delay(0.05)


close_canvas()



