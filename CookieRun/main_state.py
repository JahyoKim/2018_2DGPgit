import random
from pico2d import *
from Stage import *
from Character import *
from Background import *
from Hurdle import *
from Jelly import *
from score import *

import game_framework
import title_state
import main_state2
import result

running = None
current_time = 0.0
stage = None
character = None
background = None
hurdle = None
hurdle2 = None
jelly = None
hp = None
jellysound = None
hpjellysound = None
score = None
ascore = 0
name = "MainState"

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def enter():
    global stage, character, background, running, hurdle, hurdle2, jelly, hp, jellysound, hpjellysound, font, score
    background = Background()
    stage = Stage()
    character = Character()
    hurdle = Hurdle1().create()
    hurdle2 = Hurdle12().create()
    jelly = Jelly().create()
    hp = Hp().create()
    jellysound = Jelly()
    hpjellysound = Hp()
    score = Score()
    font = load_font('sprite\\ENCR10B.TTF')

    running = True

def get_frame_time():
    global current_time

    frame_time = get_time() - current_time
    current_time += frame_time
    return frame_time

def exit():
    global stage, character, background, running, hurdle, hurdle2, jelly, hp
    del (stage)
    del (character)
    del (background)
    for hur in hurdle:
        hurdle.remove(hur)
        del (hur)
    del (hurdle)

    for hur in hurdle2:
        hurdle2.remove(hur)
        del (hur)
    del (hurdle2)

    for jel in jelly:
        jelly.remove(jel)
        del (jel)
    del (jelly)

    for hpj in hp:
        hp.remove(hpj)
        del (hpj)
    del (hp)


def pause():
    pass


def resume():
    pass

def update():
    global running, background, character, stage, hurdle, ascore
    handle_events()
    frame_time = get_frame_time()
    background.update(frame_time)
    character.update()
    stage.update(frame_time)
    score.stage1_score()
    ascore = score.score
    print("Stage1 Clear Time : ", score.score)
    for hur in hurdle:
        hur.update(frame_time)
        if collide(character, hur):
            #character.collide_sound.play()
            character.state = "collide"

    for hur in hurdle2:
        hur.update(frame_time)
        if collide(character, hur):
            # character.collide_sound.play()
            character.state = "collide"

    for jel in jelly:
        jel.update(frame_time)
        if collide(character, jel):
            jellysound.jellyitem_sound.play()
            jelly.remove(jel)
            score.score += 100

    for hpj in hp:
        hpj.update(frame_time)
        if collide(character, hpj):
            hpjellysound.hpitem_sound.play()
            hp.remove(hpj)
            character.heal()

    if character.hp <= 0:
        game_framework.change_state(result)



def handle_events():
    global running, background

    if background.frame >= 8:
        # background.ChangeState_sound.play()
        game_framework.change_state(main_state2)

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        else:
            if event.type == SDL_KEYDOWN and event.key == SDLK_z:
                character.jump_sound.play()
                character.state = "jump"
            elif event.type == SDL_KEYDOWN and event.key == SDLK_x:
                character.slide_sound.play()
                if character.state != "jump":
                    character.state = "slide"
            elif event.type == SDL_KEYUP and event.key == SDLK_x:
                if character.state == "slide":
                    character.state = "run"
                    character.y = 180
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.type == SDL_KEYDOWN and event.key == SDLK_2:
                game_framework.change_state(main_state2)
            elif event.type == SDL_KEYDOWN and event.key == SDLK_3:
                game_framework.change_state(result)
def draw():
    global background, stage, character, running
    clear_canvas()
    background.draw()
    stage.draw()

    for hur in hurdle:
        hur.draw()
        # hur.draw_bb()

    for hur in hurdle2:
        hur.draw()
        # hur.draw_bb()

    for jel in jelly:
        jel.draw()
        # jel.draw_bb()

    for hpj in hp:
        hpj.draw()
        # hpj.draw_bb()

    font.draw(100, 550, 'Score : %3.2d' % score.score, (255, 255, 255))
    character.draw()

    delay(0.04)
    update_canvas()

#    close_canvas()
