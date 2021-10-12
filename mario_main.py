from pico2d import *



canvas_Width = 500
canvas_Height = 412



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

class Grass1:
    def __init__(self):
        self.grass = load_image('grass1.png')
        self.x, self.y = 16,16

    def draw_grass1(self):
        self.grass1.draw(self.x,self.y)


class Grass2:
    def __init__(self):
        self.image = load_image('grass2.png')
        self.x, self.y = 16, 16

    def draw_grass2(self):
        self.image.draw(self.x, self.y)


class BG:
    def __init__(self):
        self.image = load_image('BG.png')
    def draw(self):
        self.image.draw()


class Mario:
    def __init__(self):
        self.image_idle = load_image('mario_idle.png')
        self.image_walk = load_image('walk_animaiton.png')
        self.image_jump = load_image('mario_jump.png')
        self.x, self.y = 0,72
        self.frame = 3

    def idle(self):
        self.image_idle.draw(400, 72)


open_canvas(canvas_Width, canvas_Height)

# prepare images

mario = Mario()
grass2 =
running = True





while running:

    handle_events()
    clear_canvas()
    mario.idle()
    gras


    update_canvas()





close_canvas()




