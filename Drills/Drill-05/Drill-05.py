from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 경로좌표: (203, 535), (132, 243), (535, 470), (477, 203), (715, 136), (316, 225),
#               (510, 92),(692, 518), (682, 336), (712, 349)

def move_p1():
    x, y = 203, 535
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, y)

def move_p2():
    pass

def move_p3():
    pass

def move_p4():
    pass

def move_p5():
    pass

def move_p6():
    pass

def move_p7():
    pass

def move_p8():
    pass

def move_p9():
    pass

def move_p10():
    pass

def move_to_p1():
    pass

while True:
    move_p1()
    move_p2()
    move_p3()
    move_p4()
    move_p5()
    move_p6()
    move_p7()
    move_p8()
    move_p9()
    move_p10()
    move_to_p1()

close_canvas()
