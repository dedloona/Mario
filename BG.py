from pico2d import *

height = 400
width = 512

class BackGround:

    image = None

    def __init__(self):
        if BackGround.image == None:
            self.image = load_image('Resources/used/BG/BG.png')
        self.x = width//2
        self.y = height//2
    def update(self):
        pass
    def draw(self):
        for i in range(8):
            self.image.draw((self.x+height*i),self.y)