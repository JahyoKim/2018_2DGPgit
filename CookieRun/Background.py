from pico2d import *

class Background:
    def __init__(self):
        self.background = load_image('background.png')

    def draw(self):
        x = int(self.left)
        w = min(Self.image.w - x, self.screen_width)
        self.image.clip_draw_to_origin(x, 0, w, self.screen_height,0,0)
        self.image.clip_draw_to_origin(0, 0, self.screen_width-w, self.screen_height,w,0)

    def update(self,frame_time):
        self.left = (self.left + frame_time * self.speed) % self.image.w

    