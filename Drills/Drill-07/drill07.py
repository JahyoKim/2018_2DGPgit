from pico2d import *
import random

KPU_WIDTH, KPU_HEIGHT = 1280 // 2 , 1024 // 2
character = load_image('animation_sheet.png')
kpu_ground = load_image('KPU_GROUND.png')

def draw_point(p):
    pass

def random_move(p1,p2):
    #clear_canvas_now()

    for i in range(0,100+1,2):
        t = i/100
        x = (1-t)*p1[0]+t*p2[0]
        y = (1 - t) * p1[1] + t * p2[1]
        character.draw_now((x, y))
        draw_point(p2)



size = 20
points = [(random.randint(-500,500),random.randint(-350,350)) for
           i in range(size)]
n = 1

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

while True:
    random_move(points[n-1], points[n])
    n = (n+1)%size

close_canvas()




