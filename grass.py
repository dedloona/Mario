from pico2d import *
import game_framework



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
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()

    def update(self):
        pass

    def scroll(self, move):
        self.x -= move*game_framework.frame_time

    def draw(self):
        self.image.draw(self.x, self.y)
        tile_left = self.window_left // 800
        tile_right = min((self.window_left + self.canvas_width) // 800 + 1, 3)
        left_offset = self.window_left % 800
        tile_bottom = self.window_bottom // 600
        tile_top = min((self.window_bottom + self.canvas_height) // 600 + 1, 3)
        bottom_offset = self.window_bottom % 600

        for ty in range(tile_bottom, tile_top):
            for tx in range(tile_left, tile_right):
                self.image[ty][tx].draw_to_origin(-left_offset + (tx - tile_left) * 800, -bottom_offset + (ty - tile_bottom) * 600)

    def get_bb(self):
        return self.left, self.right, self.top, self.bottom
