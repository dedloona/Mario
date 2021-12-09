from pico2d import *
import game_framework
import game_world
import server


class Grass:
    image = None

    def __init__(self,x,y):
        if Grass.image is None:
            self.image = load_image('Resources/used/tiles/grass2.png')


        self.x = x
        self.y = y
        self.size = 16
        self.top = self.y + 8
        self.bottom = self.y - 8
        self.left = self.x - 8
        self.right = self.x + 8
        self.w = 16*200
        self.h = 16*16
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()
        self.window_left = clamp(0, int(server.mario.x) - self.canvas_width // 2, self.w - self.canvas_width)
        self.window_bottom = clamp(0, int(server.mario.y) - self.canvas_height // 2, self.h - self.canvas_height)

    def update(self):
        pass

    def scroll(self, move):
        self.x -= move

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.left, self.right, self.top, self.bottom


class Pipe1:
    image = None

    def __init__(self, x, y):
        if Pipe1.image is None:
            self.image = load_image('Resources/used/tiles/green_pipe1.png')
        self.x = x
        self.y = y
        self.size = 16
        self.top = self.y + 8
        self.left = self.x - 8

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.left


class Pipe2:
    image = None

    def __init__(self, x, y):
        if Pipe1.image is None:
            self.image = load_image('Resources/used/tiles/green_pipe2.png')
        self.x = x
        self.y = y
        self.size = 16
        self.top = self.y + 8
        self.right = self.x + 8

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.right


class Pipe3:
    image = None

    def __init__(self, x, y):
        if Pipe1.image is None:
            self.image = load_image('Resources/used/tiles/green_pipe3.png')
        self.x = x
        self.y = y
        self.size = 16

        self.left = self.x - 8
        self.top = self.y + 8
        self.bottom = self.y - 8

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.left, self.top


class Pipe4:
    image = None

    def __init__(self, x, y):
        if Pipe1.image is None:
            self.image = load_image('Resources/used/tiles/green_pipe4.png')
        self.x = x
        self.y = y
        self.size = 16

        self.top = self.y + 8
        self.right = self.x + 8

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.top, self.right
