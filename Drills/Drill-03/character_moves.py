from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


def draw(x,y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)

while(1):
    x = 400
    y = 90

    while(x < 800):
        draw(x, y)
        x = x + 5
        
    while(y < 600):
        draw(x, y)
        y = y + 5
        
    while(0 < x):
        draw(x, y)
        x = x - 5
        
    while(90 < y):
        draw(x, y)
        y = y - 5

    x = 400
    y = 90
    i = 0

    while(i <= 360):    
       draw(x,y)
       x = 400 - 200 * math.sin(math.radians(i))
       y = 300 - 200 * math.cos(math.radians(i))
       i = i + 1
    
    
close_canvas()
