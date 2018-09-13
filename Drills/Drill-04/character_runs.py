from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

x = 0
frame = 0
while(1):
    while(x < 800):
        clear_canvas()
        grass.draw(400,30)
        character.clip_draw(frame*100,100,100,100,x,90)
        update_canvas()
        frame= (frame+1)%8 #애니메이션을 빠르게 돌리고싶으면 (frame+5)%8 이런식으로!
        x+=5 # 속도를 조정하고 싶을땐 이 값을 조정한다.
        delay(0.05)
        get_events()

    while(0 < x):
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 100, 0, 100, 100, x, 90)
        update_canvas()
        frame = (frame + 1) % 8
        x -= 5
        delay(0.05)
        get_events()
close_canvas()

