import json


from pico2d import *
import game_framework
import game_world

import world_build_state


name = "RankingState"

menu = None

def enter():
    hide_cursor()
    hide_lattice()

def exit():
    pass

def pause():
    pass

def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(world_build_state)


def update():
    pass

def draw():
    clear_canvas()
    # total ranking 출력
    update_canvas()






