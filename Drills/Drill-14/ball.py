import random
from pico2d import *
import game_world
import game_framework

class Ball:
    image = None
    back = None

    def __init__(self,back):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y, self.fall_speed = random.randint(0, 1800-1), random.randint(0, 1100-1),0
        if Ball.back == None:
            Ball.back = back

    def get_bb(self):
        return self.x - 10, self.y - 10, self.x + 10, self.y + 10

    def draw(self):
        x, y = self.x-self.back.window_left, self.y-self.back.window_bottom
        self.image.draw(x, y)
        #draw_rectangle(*self.get_bb())

    def update(self):
        self.y -= self.fall_speed * game_framework.frame_time

