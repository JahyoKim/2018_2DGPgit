import random
from pico2d import *
from Character import *
from Background import *

import game_framework
import title_state

running = None
current_time = 0.0
character = None
Background = None

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
    global character, background, running, font
    background = Background()
    character = Character()
    font = load_font('image\\ENCR10B.TTF')

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
    pass
#    global running, backstage
#
#    if backstage.frame >= 8:
#        #backstage.ChangeState_sound.play()
#        game_framework.change_state(main_state2)
#
#
#    events = get_events()
#    for event in events:
#        if event.type == SDL_QUIT:
#            running = False
#        #elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
#         #   running = False
#        else:
#
#            if event.type == SDL_KEYDOWN and event.key == SDLK_z:
#                character.jump_sound.play()
#                character.state = "jump"
#            elif event.type == SDL_KEYDOWN and event.key == SDLK_x:
#                character.slide_sound.play()
#                character.state = "slide"
#            elif event.type == SDL_KEYUP and event.key == SDLK_x:
#                character.state = "run"
#                character.y = 240
#            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
#                game_framework.change_state(title_state)
#            elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
#                game_framework.change_state(main_state2)
#            elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
#                game_framework.change_state(result)

def draw():
    global background, character, running
    clear_canvas()
    background.draw()

    character.draw()

    delay(0.04)
    update_canvas()

#    close_canvas()
