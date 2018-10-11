import game_framework
from pico2d import *
import main_state

pause = None
type = 0

def enter():
    global pause
    pause = load_image('pause.png')

def exit():
    global pause
    del(pause)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type,event.key) ==(SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_p):
                game_framework.pop_state()

def update():
    global type
    if(type == 0) :
        type = 1
    else :
        type = 0

def draw():
    global type
    clear_canvas()
    if (type == 0):
        pause.draw(400, 340)
    main_state.grass.draw()
    main_state.boy.draw()
    delay(0.05)
    update_canvas()

    