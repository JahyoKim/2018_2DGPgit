import game_framework
import title
from pico2d import *


name = "StartState"
image = None
dev = None
logo_time = 0.0


def enter():
    global image, dev, kakao, title
    image = load_image('image\\kpu_credit.png')
    dev = load_image('image\\title_CI.png')

def exit():
    global image, dev, kakao
    del(image)
    del(dev)
    close_canvas()


def update():
    global logo_time

    if (logo_time > 3.0):
        logo_time = 0
        game_framework.push_state(title_state)
    delay(0.01)
    logo_time += 0.01

def draw():
    global image, dev
    clear_canvas()
    image.draw(400,300)
    if(logo_time > 1.0):
        dev.draw(400, 300)
    update_canvas()

def handle_events():
    events = get_events()
    pass


def pause():
    pass

def resume():
    pass
