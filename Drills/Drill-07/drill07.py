from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280 // 2 , 1024 // 2


def handle_events():
    global running
    global x, y
    global dir
    global ch_x, ch_y
    global mouse_x, mouse_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.x - 25, KPU_HEIGHT - 1 + 25 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

#현재 캐릭터 좌표 += (마우스 클릭좌표 - 현재좌표) / 10
open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
mouse_x, mouse_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
ch_x, ch_y = KPU_WIDTH // 2, KPU_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand_arrow.draw(x, y)
    if ch_x < mouse_x:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, ch_x, ch_y)
        ch_x += (mouse_x - ch_x) // 10
        ch_y += (mouse_y - ch_y) // 10
    elif ch_x > mouse_x:
        character.clip_draw(frame * 100, 0 * 1, 100, 100, ch_x, ch_y)
        ch_x += (mouse_x - ch_x) // 10
        ch_y += (mouse_y - ch_y) // 10
    update_canvas()
    frame = (frame + 1) % 8
    delay(0.02)
    handle_events()

close_canvas()

