import random
from pico2d import *
from Character import *
from Background import *
import Background
import game_framework
import title_state
from score import *

running = None
current_time = 0.0
character = None
Background = None
jellysound = None
hpjellysound = None
score = None
ascore = 0

name = "MainState"

def collid(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def enter():
    global background, character, running, font
    background = Background()
    character = Character()
    jellysound = Jelly()
    hpjellysound = Hp()
    score = Score()
    #font = load_font('image\\ENCR10B.TTF')

    running = True

def get_frame_time():
    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def exit():
    global character, background, running
    del(character)
    del(background)


def pause():
    pass


def resume():
    pass

def update():
    global running, background, character
    handle_events()
    frame_time = get_frame_time()
    background.update(frame_time)
    character.update()


def handle_events():
    global running, background

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        if event.type == SDL_KEYDOWN and event.key == SDLK_z:
            character.state = "jump"
        elif event.type == SDL_KEYDOWN and event.key == SDLK_x:
            if character.state != "jump":
                character.state = "slide"
        elif event.type == SDL_KEYUP and event.key == SDLK_x:
            if character.state == "slide":
                character.state = "run"
                character.y = 180
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def draw():
    global background, character, running
    clear_canvas()
    background.draw()

    character.draw()

    delay(0.04)
    update_canvas()

#    close_canvas()
