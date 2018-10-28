from pico2d import *

class Background:

    # Boy Run Speed
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 30.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)


    def __init__(self):
        self.background = load_image('sprite\\background.png')

    def draw(self):
        x = int(self.left)
        w = min(Self.image.w - x, self.screen_width)
        self.image.clip_draw_to_origin(x, 0, w, self.screen_height,0,0)
        self.image.clip_draw_to_origin(0, 0, self.screen_width-w, self.screen_height,w,0)

    def update(self,frame_time):
        self.left = (self.left + frame_time * self.speed) % self.image.w

    def handle_event(self,event):
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT: self.speed -= Background.SCROLL_SPEED_PPS
            elif event.key == SDLK_RIGHT: self.speed += Background.SCROLL_SPEED_PPS
        if event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT: self.speed += Background.SCROLL_SPEED_PPS
            elif event.key == SDLK_RIGHT: self.speed -= Background.SCROLL_SPEED_PPS