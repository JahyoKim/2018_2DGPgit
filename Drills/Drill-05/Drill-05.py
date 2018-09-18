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
        delay(0.05)


def move_p3(): #(535, 470)
    x, y = 132, 243
    moveX = (535 - 132) // 10
    moveY = (470 - 243) // 10

    while x <= 535 and y <= 470:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += moveX
        y += moveY
        delay(0.05)

def move_p4(): #(477, 203)
    x, y = 535, 470
    moveX = (535 - 477) // 10
    moveY = (470 - 203) // 10

    while 477 <= x and 203 <= y:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= moveX
        y -= moveY
        delay(0.05)

def move_p5(): #(715, 136)
    x, y = 477, 203
    moveX = (715 - 477) // 10
    moveY = (203 - 136) // 10

    while x <= 715 and 136 <= y:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x += moveX
        y -= moveY
        delay(0.05)
##########################
def move_p6(): #(316, 225)
    x, y = 715, 136
    moveX = (715 - 316) // 10
    moveY = (225 - 136) // 10

    while 316 <= x and y <= 225:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= moveX
        y += moveY
        delay(0.05)

def move_p7(): #(510, 92)
    x, y = 316, 225
    moveX = (203 - 132) // 10
    moveY = (535 - 243) // 10

    while 132 <= x and 243 <= y:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= moveX
        y -= moveY
        delay(0.05)

def move_p8(): #(692, 518)
    x, y = 510, 92
    moveX = (203 - 132) // 10
    moveY = (535 - 243) // 10

    while 132 <= x and 243 <= y:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= moveX
        y -= moveY
        delay(0.05)

def move_p9(): #(682, 336)
    x, y = 692, 518
    moveX = (203 - 132) // 10
    moveY = (535 - 243) // 10

    while 132 <= x and 243 <= y:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= moveX
        y -= moveY
        delay(0.05)

def move_p10(): #(712, 349)
    x, y = 682, 336
    moveX = (203 - 132) // 10
    moveY = (535 - 243) // 10

    while 132 <= x and 243 <= y:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= moveX
        y -= moveY
        delay(0.05)

def move_to_p1():
    x, y = 712, 349
    moveX = (203 - 132) // 10
    moveY = (535 - 243) // 10

    while 132 <= x and 243 <= y:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, y)
        x -= moveX
        y -= moveY
        delay(0.05)

move_p1()
move_p2()
move_p3()
move_p4()
move_p5()
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
