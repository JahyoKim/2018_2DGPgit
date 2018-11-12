from pico2d import *

class Background:
    image_init = None

    PIXEL_PER_METER = (10.0 / 0.3)
    SCROLL_SPEED_KMPH = 30.0
    SCROLL_SPEED_MPM = (SCROLL_SPEED_KMPH * 1000.0 / 60.0)
    SCROLL_SPEED_MPS = (SCROLL_SPEED_MPM / 60.0)
    SCROLL_SPEED_PPS = (SCROLL_SPEED_MPS * PIXEL_PER_METER)

    def __init__(self):
        self.stage1_x = 400
        self.stage1_y = 400
        self.frame = 1
        self.speed = 5
        self.distance = 0
        self.count = 0

        if Background.image_init == None:
            self.stage1 = load_image('sprite\\background.png')

            self.bgm = load_music('Sound\\stage1.mp3')
            self.bgm.set_volume(64)
            self.bgm.repeat_play()

        if Background.ChangeState == None:
            self.ChangeState_sound = load_wav('Sound\ChangeState.wav')
            self.ChangeState_sound.set_volume(64)


    def draw(self):
        if self.count >= 7:
            self.ChangeState_sound.play()
            self.stage3.clip_draw(self.frame * 800, 0, 800, 800, self.stage1_x, self.stage1_y)
            delay(0.05)
        else:
            self.stage1.draw(self.stage1_x, self.stage1_y)



    def update(self,frame_time):
        if Background.RUN_SPEED_PPS * frame_time > 7:
            self.distance = 10
        else:
            self.distance = Background.RUN_SPEED_PPS * frame_time



#class Background:

    # Boy Run Speed
    #PIXEL_PER_METER = (10.0 / 0.3)
    #RUN_SPEED_KMPH = 30.0
    #RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    #RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    #RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


    #def __init__(self):
        #self.image = load_image('sprite\\background.png')



    #def draw(self):
    #    x = int(self.left)
    #    w = min(self.image.w - x, self.screen_width)
    #    self.image.clip_draw_to_origin(x, 0, w, self.screen_height,0,0)
    #    self.image.clip_draw_to_origin(0, 0, self.screen_width-w, self.screen_height,w,0)
#
    #def update(self,frame_time):
    #    self.left = (self.left + frame_time * self.speed) % self.image.w
#
    #def handle_event(self,event):
    #    if event.type == SDL_KEYDOWN:
    #        if event.key == SDLK_LEFT: self.speed -= Background.SCROLL_SPEED_PPS
    #        elif event.key == SDLK_RIGHT: self.speed += Background.SCROLL_SPEED_PPS
    #    if event.type == SDL_KEYUP:
    #        if event.key == SDLK_LEFT: self.speed += Background.SCROLL_SPEED_PPS
    #        elif event.key == SDLK_RIGHT: self.speed -= Background.SCROLL_SPEED_PPS