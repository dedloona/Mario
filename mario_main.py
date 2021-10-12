from pico2d import *
import mario_player
import time



canvas_Width = 512
canvas_Height = 400
s_time = time.time()
e_time = time.time()





class Grass1:
    def __init__(self):
        self.grass = load_image('grass1.png')
        self.x, self.y = 16,16

    def draw_grass1(self):
        self.grass.draw(self.x,self.y)


class Grass2:
    def __init__(self):
        self.image = load_image('grass2.png')
        self.x, self.y = 16, 16

    def draw_grass2(self,x ,y):
        self.image.draw(x, y)


class BG:
    def __init__(self,x,y):
        self.image = load_image('BG.png')
        self.x = x
        self.y = y
    def draw(self):
        self.image.draw(self.x,self.y)






open_canvas(canvas_Width, canvas_Height)

# prepare images

mario = mario_player.Mario()

bg1 = BG(canvas_Width/2-canvas_Width,canvas_Height/2)
bg2 = BG(canvas_Width/2,canvas_Height/2)
bg3 = BG((canvas_Width/2)+canvas_Width,canvas_Height/2)
grasses = [Grass2() for i in range(1, 32+1)]

running = True

current_time = time.time()

while running:

    frame_time = time.time() - current_time
    current_time += frame_time

    mario.update(frame_time)
    clear_canvas()

    # if mario.x == canvas_Width:
    #     del (bg1)
    # elif mario.x == 0:
    #     del (bg3)
    bg1.draw()
    bg2.draw()
    bg3.draw()

    mario.draw()


    i = 0

    for grass in grasses:
        grass.draw_grass2(8+i*16,8)
        i += 1



    update_canvas()





close_canvas()




