from pico2d import *


class Character:
    image_init = None
    state_init = None
    collidetime = 0
    score = 0

    def __init__(self):
        self.x = 200
        self.y = 180
        self.frame = 0
        self.frame_2 = 0
        self.state = "run"
        self.jump_state = "up"
        self.slide_state = "slide"
        self.hp = 500
        self.score = 0

        if self.image_init == None:
            self.run = load_image('sprite\\jungle_run.png')
            self.jump = load_image('sprite\\jungle_jump_1.png')
            self.slide = load_image('sprite\\jungle_slide_1.png')
            self.collide = load_image('sprite\\jungle_collide.png')
            self.hpbar = load_image('sprite\\hp.png')

        if self.state_init == None:
            self.jump_sound = load_wav('Sound\\jump.wav')
            self.jump_sound.set_volume(64)
            self.slide_sound = load_wav('Sound\\slide.wav')
            self.slide_sound.set_volume(64)
            self.collide_sound = load_wav('Sound\\collide.wav')
            self.collide_sound.set_volume(64)


    def heal(self):
        self.hp += 100


    def get_score(self):
        return self.score


    def update(self):
        self.hp -= 1

        self.frame +=1
        if self.frame == 4:
            self.frame = 0
        #self.frame_2 +=1
        #if self.frame_2 == 2:
        #    self.frame_2 = 0

        if self.state == "collide":

            self.collidetime += 1
            if self.collidetime == 1:
                self.collide_sound.play()
                self.hp -= 50
            if(self.collidetime >= 10):
                self.state = "run"
                self.y = 180
                self.collidetime = 0

        if self.state == "jump" and self.jump_state == "up":
            if self.y >= 240:
                self.jump_state = "down"
            self.y += 10

        if self.state == "jump" and self.jump_state == "down":
            if self.y >= 180:
                self.y -= 10

        if self.state == "jump" and self.y == 180:
            self.state = "run"
            self.jump_state = "up"

        if self.state == "slide":
            self.y = 170


    def get_bb(self):
        return self.x - 30, self.y - 40, self.x + 25, self.y + 35

    def draw_bb(self):
        draw_rectangle(*self.get_bb())


    def draw(self):
        if self.state == "run":
            self.run.clip_draw(self.frame * 100, 0, 100, 62, self.x, self.y)
        elif self.state == "jump":
            self.jump.clip_draw(self.frame * 90, 0, 90, 63, self.x, self.y)
        elif self.state == "slide":
            self.slide.clip_draw(self.frame * 97, 0, 96, 40, self.x, self.y)
        elif self.state == "collide":
            self.collide.draw(self.x, self.y)
        self.hpbar.draw_to_origin(0, 500, self.hp, 50)



#open_canvas(800,600)
#jungle = Jungle()
#jelly = Jelly()
#hurdle = Hurdle()
#background = Background()
#
#running = True
#
#while running:
#    handle_events()
#    background.update()
#    jelly.update()
#    jungle.update()
#
#    clear_canvas()
#    background.draw()
#    jelly.draw()
#    hurdle.draw()
#    jungle.draw()
#    update_canvas()
#    delay(0.05)
#
#
#close_canvas()
#
#

