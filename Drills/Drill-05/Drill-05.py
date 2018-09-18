from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def move_from_center_to_right():
    x, y = 800 // 2, 90  # 400을 쓰는 것 보다 개발자의 의도를 이해하기 편안
    while x <800 - 25:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        x += 5
        delay(0.01)

def move_up():
    x, y = 800 - 25, 90
    while y <600 - 50:
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        y += 5
        delay(0.01)

def move_left():
    x, y = 800, 600-50
    while 0 < x:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 5
        delay(0.01)

def move_down():
    x, y = 0, 600
    while 90 < y:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        y -= 5
        delay(0.01)

def move_left_to_center():
    pass

def make_rectangle():
    move_from_center_to_right()
    move_up()
    move_left()
    move_down()
    move_left_to_center()

def make_circle():
    pass

while True:
    make_rectangle()
    make_circle()
    
close_canvas()
