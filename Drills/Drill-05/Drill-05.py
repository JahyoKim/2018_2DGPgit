from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

# 경로좌표: (203, 535), (132, 243), (535, 470), (477, 203), (715, 136), (316, 225),
#               (510, 92),(692, 518), (682, 336), (712, 349)

def move_p1(): #(203, 535)
    x, y = 203, 535
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, y)

def move_p2(): #(132, 243)
    x, y = 203, 535
    moveX = (203 - 132) // 10
    moveY = (535 - 243) // 10

    while 132 <= x and 243 <= y:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= moveX
        y -= moveY
        delay(0.01)


def move_p3(): #(535, 470)
    x, y = 132, 243
    while x < 535 and y < 470:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += 1
        y += 1
    pass

def move_p4(): #(477, 203)
    x, y = 535, 470
    while 132 < x and 243 < y:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 1
        y -= 1
    pass

def move_p5(): #(715, 136)
    x, y = 477, 203
    while 132 < x and 243 < y:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 1
        y -= 1
    pass

def move_p6(): #(316, 225)
    x, y = 715, 136
    while 132 < x and 243 < y:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 1
        y -= 1
    pass

def move_p7(): #(510, 92)
    x, y = 316, 225
    while 132 < x and 243 < y:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 1
        y -= 1
    pass

def move_p8(): #(692, 518)
    x, y = 510, 92
    while 132 < x and 243 < y:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 1
        y -= 1
    pass

def move_p9(): #(682, 336)
    x, y = 692, 518
    while 132 < x and 243 < y:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 1
        y -= 1
    pass

def move_p10(): #(712, 349)
    x, y = 682, 336
    while 132 < x and 243 < y:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 1
        y -= 1
    pass

def move_to_p1():
    x, y = 712, 349
    while 132 < x and 243 < y:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= 1
        y -= 1
    pass

#move_p1()
move_p2()
#move_p3()
#move_p4()
#move_p5()
#move_p6()
#move_p7()
#move_p8()
#move_p9()
#move_p10()
#move_to_p1()

#while True:
#    move_p1()
#    move_p2()
#   #move_p3()
#   #move_p4()
#   #move_p5()
#   #move_p6()
#   #move_p7()
#   #move_p8()
#   #move_p9()
#   #move_p10()
#   #move_to_p1()

close_canvas()
