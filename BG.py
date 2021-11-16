class BG:
    def __init__(self,x,y):
        self.image = load_image('BG.png')
        self.x = x
        self.y = y
    def draw(self):
        self.image.draw(self.x,self.y)