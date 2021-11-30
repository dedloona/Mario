from pico2d import *

class Grass:
    image = None
    def __init__(self, x, y):
        if Grass.image == None:
            self.image = load_image('Resources/used/tiles/grass2.png')
        self.x = x
        self.y = y
        self.size = 32


    def update(self):
        pass

    def draw(self):
        self.image.draw((self.x)+self.size, self.y,32,32)


    def get_bb(self):
        return 0, 0, 0, 0