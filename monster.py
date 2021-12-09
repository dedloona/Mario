from pico2d import *
import game_framework
import server
from ball import Ball
import game_world
from collision import collide

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 0.1  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 0.3


class Gumba:
    image = None

    def __init__(self, x, y):
        if Gumba.image is None:
            self.image = load_image('Resources/used/monster/gumba.png')
        self.x = x
        self.y = y

        self.frame = 0
        self.velocity = 0
        self.dir = -1

        self.top = self.y + 8
        self.bottom = self.y - 8
        self.left = self.x - 8
        self.right = self.x + 8

    def update(self):

        if self.dir == -1:
            self.velocity -= RUN_SPEED_PPS
            self.x += self.velocity * game_framework.frame_time
        else:
            self.velocity += RUN_SPEED_PPS
            self.x += self.velocity * game_framework.frame_time

        if collide(server.mario, self):
            game_world.remove_object(self)

        if self.x < 50:
            self.dir = 1
        elif self.x >= 900:
            self.dir = -1
        self.x = clamp(25, self.x, 900)

    def draw(self):
        self.frame = int((self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time + 1) % 2)
        self.image.clip_draw(self.frame * 16, 0, 16, 16,self.x, self.y)

    def get_bb(self):
        return self.left, self.right, self.top, self.bottom
