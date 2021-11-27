from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('Resources/used/tiles/grass2.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(400, 30)
        self.image.draw(200, 30)


    def get_bb(self):
        return 0, 0, 0, 0