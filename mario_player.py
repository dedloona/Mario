from pico2d import *

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, SLEEP_TIMER, SPACE = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}


class IdleState:

    def enter(mario, event):
        if event == RIGHT_DOWN:
            mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mario.velocity += RUN_SPEED_PPS
        mario.timer = 1000

    def exit(boy, event):
        if event == SPACE:
            boy.fire_ball()
        pass

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        mario.timer -= 1
        if mario.timer == 0:
            mario.add_event(SLEEP_TIMER)

    def draw(mario):
        if mario.dir == 1:
            mario.image.clip_draw(int(mario.frame) * 100, 300, 100, 100, mario.x, mario.y)
        else:
            mario.image.clip_draw(int(mario.frame) * 100, 200, 100, 100, mario.x, mario.y)

class RunState:

    def enter(mario, event):
        if event == RIGHT_DOWN:
            mario.velocity += RUN_SPEED_PPS
        elif event == LEFT_DOWN:
            mario.velocity -= RUN_SPEED_PPS
        elif event == RIGHT_UP:
            mario.velocity -= RUN_SPEED_PPS
        elif event == LEFT_UP:
            mario.velocity += RUN_SPEED_PPS
        mario.dir = clamp(-1, mario.velocity, 1)

    def exit(mario, event):
        if event == SPACE:
            mario.fire_ball()

    def do(mario):
        #boy.frame = (boy.frame + 1) % 8
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        mario.x += mario.velocity * game_framework.frame_time
        mario.x = clamp(25, mario.x, 1600 - 25)

    def draw(mario):
        if mario.dir == 1:
            mario.image.clip_draw(int(mario.frame) * 100, 100, 100, 100, mario.x, mario.y)
        else:
            mario.image.clip_draw(int(mario.frame) * 100, 0, 100, 100, mario.x, mario.y)


class JumpState:

    def enter(mario, event):
        mario.frame = 0

    def exit(mario, event):
        pass

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(mario):
        if mario.dir == 1:
            mario.image.clip_composite_draw(int(boy.frame) * 100, 300, 100, 100, 3.141592 / 2, '', mario.x - 25, mario.y - 25, 100, 100)
        else:
            mario.image.clip_composite_draw(int(boy.frame) * 100, 200, 100, 100, -3.141592 / 2, '', mario.x + 25, mario.y - 25, 100, 100)




next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, SLEEP_TIMER: SleepState, SPACE: IdleState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, SPACE: RunState},
    JumpState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, SPACE: IdleState}
}
class Mario:

    PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
    RUN_SPEED_KMPH = 20.0  # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

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
        self.gravity = 9.8
        self.drop = 0
        self.dir = 0
        self.power = 2.5
        self.jump_time = 0
        self.state_jump = False
        self.state_idle = True
        self.state_walk = False

    def set_addpos(self, x, y):
        self.x += x
        self.y += y


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
        if self.state_jump:
            self.jump()
        elif self.state_walk:
            self.walk()
        elif self.state_idle:
            self.idle()

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        self.total_frames += Mario.FRAMES_PER_ACTION * Mario.ACTION_PER_TIME * frame_time

        self.x += self.dir
        self.handle_events()
        if self.state_jump:
            self.height = (self.jump_time * self.power) - (self.jump_time ** 2 * self.gravity / 2)
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