from pico2d import *


class Grass:
    image = None

    def __init__(self, x, y):
        if Grass.image is None:
            self.image = load_image('Resources/used/tiles/grass2.png')
        self.x = x
        self.y = y
        self.size = 16
        self.top = self.y + 8
        self.bottom = self.y - 8
        self.left = self.x - 8
        self.right = self.x + 8

    def update(self):
        pass

    def draw(self):
        self.image.draw(self.x, self.y)

    def get_bb(self):
        return self.left, self.right, self.top, self.bottom
