from pico2d import *


class Pipe1:
    image = None

    def __init__(self, x, y):
        if Pipe1.image is None:
            self.image = load_image('Resources/used/tiles/green_pipe1.png')
        self.x = x
        self.y = y
        self.size = 16

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

        self.left = self.x - 8

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.left


class Pipe3:
    image = None

    def __init__(self, x, y):
        if Pipe1.image is None:
            self.image = load_image('Resources/used/tiles/green_pipe3.png')
        self.x = x
        self.y = y
        self.size = 16

        self.left = self.x - 8

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.left


class Pipe4:
    image = None

    def __init__(self, x, y):
        if Pipe1.image is None:
            self.image = load_image('Resources/used/tiles/green_pipe4.png')
        self.x = x
        self.y = y
        self.size = 16

        self.left = self.x - 8

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.left

