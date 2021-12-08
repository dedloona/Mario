from pico2d import *

import game_framework
import game_world
import server
import collision

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 60.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.5 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Ball:
    image = None

    def __init__(self, x=400, y=300, velocity=1):

        if Ball.image == None:
            Ball.image = load_image('Resources/used/marioes/fire_ball.png')
        self.x, self.y, self.velocity = x, y, velocity
        self.frame = 0
        self.top = self.y + 4
        self.bottom = self.y - 4
        self.left = self.x - 4
        self.right = self.x + 4

    def draw(self):
        print('ball')
        self.image.clip_draw(int(self.frame) * 8, 0, 8, 8, self.x, self.y)

    def do(self):
        self.frame = int((self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time + 1) % 3)

    def update(self):
        self.x += self.velocity * game_framework.frame_time * RUN_SPEED_PPS

        if self.x < server.mario.x - 1000 or self.x > server.mario.x + 1000:
            game_world.remove_object(self)

    def get_bb(self):
        return self.left, self.right, self.top, self.bottom





