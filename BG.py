from pico2d import *

height = 512
width = 400

class BackGround:

    image = None

    def __init__(self):
        if BackGround.image == None:
            self.image = load_image('BG.png')
        self.x = width//2
        self.y = height//2

    def draw(self):
        for i in range(8):
            self.image.draw(self.x+512,self.y)