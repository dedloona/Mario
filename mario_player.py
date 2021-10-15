from pico2d import *
import time







class Mario:

    TIME_PER_ACTION = 0.1
    ACTION_PER_TIME = 0.3 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 4
    total_frames = 0.0

    def __init__(self):
        self.image_idle = load_image('mario_idle.png')
        self.image_walk = load_image('walk_animaiton.png')
        self.image_jump = load_image('mario_jump.png')
        self.x, self.y = 16,28
        self.widht, self.height = 16,0
        self.frame = 0
        self.look = 1
        self.rad = 1.5708
        self.vel = 0.0
        self.gravity = 9.8
        self.drop = 0
        self.dir = 0
        self.power = 10
        self.jump_time = 0
        self.state_jump = False
        self.state_idle = True
        self.state_walk = False

    def set_addpos(self, x, y):
        self.x += x
        self.y += y

    def set_state(self,idle,walk,jump):
        self.state_idle = idle
        self.state_walk = walk
        self.state_jump = jump


    def idle(self):
        if self.look == 1:
            self.image_idle.composite_draw(self.rad * 4, 'None', self.x, self.y, 16, 29)
        elif self.look == -1:
            self.image_idle.composite_draw(self.rad * 4, 'h', self.x, self.y, 16, 29)

    def walk(self):
        self.frame = (self.frame + 1)% 3
        if self.look == 1:
            self.image_walk.clip_composite_draw(self.frame * 16, 0, 16, 29, self.rad * 4, 'None', self.x, self.y, 16, 29)
        elif self.look == -1:
            self.image_walk.clip_composite_draw(self.frame * 16, 0, 16, 29, self.rad * 4, 'h', self.x, self.y, 16, 29)

    def jump(self):
        self.jump_time += 0.0001
        if self.look == 1:
            self.image_jump.composite_draw(self.rad*4,'None',self.x,self.y )
        elif self.look == -1:
            self.image_jump.composite_draw(self.rad * 4, 'h', self.x, self.y)
        # self.drop += self.gravity

    def draw(self):
        if self.get_state_jump():
            self.jump()
        elif self.get_state_walk():
            self.walk()
        elif self.get_state_idle():
            self.idle()

    def update(self,frame_time):

        self.total_frames += Mario.FRAMES_PER_ACTION * Mario.ACTION_PER_TIME * frame_time

        self.x += self.dir
        self.handle_events()
        if self.state_jump:
            self.height = (self.jump_time * 2.5) - (self.jump_time ** 2 * self.gravity / 2)
            self.set_addpos(0,self.height)
            print(self.height)
            self.jump_time += frame_time
            self.drop += self.gravity * frame_time

            # 중력
        if self.height < 0:
            if self.y  <= 28:
                self.y = 28
                self.drop = 0
                self.state_jump = False
                self.jump_time = 0

            # print(self.dropSpeed)
        self.y += self.drop * frame_time


    def handle_events(self):

        events = get_events()
        for event in events:
            # if event.type == SDL_QUIT:
            #     running = False
            # elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            #     # running = False
            # 좌우 이동
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_a:
                    self.look = -1
                    self.dir = -0.5
                    self.state_walk = True
                elif event.key == SDLK_d:
                    self.look = 1
                    self.dir = 0.5
                    self.state_walk = True
                elif event.key == SDLK_j:

                    self.state_jump = True
                    self.drop = self.power

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_a:
                    self.state_idle = True
                    self.state_walk = False
                    self.dir = 0
                if event.key == SDLK_d:
                    self.state_idle = True
                    self.state_walk = False
                    self.dir = 0