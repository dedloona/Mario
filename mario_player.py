from pico2d import *
import game_framework

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, JUMP, FIRE = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): JUMP,
    (SDL_KEYDOWN, SDLK_j): FIRE

}

# Boy Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Boy Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


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

    def exit(mario, event):
        if mario == FIRE:
            mario.fire_ball()
        pass

    def do(mario):
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        # mario.timer -= 1
        # if mario.timer == 0:
        #     pass

    def draw(mario):
        if mario.dir == 1:
            mario.image_idle.composite_draw(mario.rad * 4, 'None', mario.x, mario.y, 16, 29)
        else:
            mario.image_idle.composite_draw(mario.rad * 4, 'h', mario.x, mario.y, 16, 29)


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
        if event == JUMP:
            mario.fire_ball()

    def do(mario):
        # boy.frame = (boy.frame + 1) % 8
        mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        mario.x += mario.velocity * game_framework.frame_time
        mario.x = clamp(25, mario.x, 1600 - 25)

    def draw(mario):
        if mario.dir == 1:
            mario.image_walk.clip_composite_draw(mario.frame * 16, 0, 16, 29, mario.rad * 4, 'None', mario.x, mario.y, 16, 29)
        else:
            mario.image_walk.clip_composite_draw(mario.frame * 16, 0, 16, 29, mario.rad * 4, 'h', mario.x, mario.y, 16, 29)


class JumpState:

    def enter(mario, event):
        # mario.total_frames += Mario.FRAMES_PER_ACTION * Mario.ACTION_PER_TIME * game_framework.frame_time
        pass
#         mario.x += mario.dir
#         mario.handle_events()
#         if mario.state_jump:
#             mario.height = (mario.jump_time * mario.power) - (mario.jump_time ** 2 * mario.gravity / 2)
#             mario.set_addpos(0, mario.height)
#             print(mario.height)
#             mario.jump_time += game_framework.frame_time
#             mario.drop += mario.gravity * game_framework.frame_time
#
#             # 중력
#         if mario.height < 0:
#             if mario.y <= 28:
#                 mario.y = 28
#                 mario.drop = 0
#                 mario.state_jump = False
#                 mario.jump_time = 0
#
#             # print(self.dropSpeed)
#         mario.y += mario.drop * game_framework.frame_time
#
#     def exit(mario, event):
#         pass
#
#     def do(mario):
#         mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
#
#     def draw(mario):
#         mario.jump_time += 0.0001
#         if mario.dir == 1:
#             mario.image_jump.composite_draw(mario.rad * 4, 'None', mario.x, mario.y)
#         elif mario.look == -1:
#             mario.image_jump.composite_draw(mario.rad * 4, 'h', mario.x, mario.y)


next_state_table = {
    IdleState: {RIGHT_UP: RunState, LEFT_UP: RunState, RIGHT_DOWN: RunState, LEFT_DOWN: RunState, JUMP: JumpState},
    RunState: {RIGHT_UP: IdleState, LEFT_UP: IdleState, LEFT_DOWN: IdleState, RIGHT_DOWN: IdleState, JUMP: JumpState},
    JumpState: {LEFT_DOWN: RunState, RIGHT_DOWN: RunState, LEFT_UP: RunState, RIGHT_UP: RunState, JUMP: JumpState}
}


class Mario:

    def __init__(self):
        self.image_idle = load_image('mario_idle.png')
        self.image_walk = load_image('walk_animation.png')
        self.image_jump = load_image('mario_jump.png')
        self.x, self.y = 16, 28
        self.width, self.height = 16, 0
        self.frame = 0
        self.look = 1
        self.rad = 1.5708
        self.gravity = 9.8
        self.drop = 0
        self.dir = 0
        self.power = 2.5
        self.jump_time = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def idle(self):
        if self.look == 1:
            self.image_idle.composite_draw(self.rad * 4, 'None', self.x, self.y, 16, 29)
        elif self.look == -1:
            self.image_idle.composite_draw(self.rad * 4, 'h', self.x, self.y, 16, 29)

    def walk(self):
        self.frame = (self.frame + 1) % 3
        if self.look == 1:
            self.image_walk.clip_composite_draw(self.frame * 16, 0, 16, 29, self.rad * 4, 'None', self.x, self.y, 16, 29)
        elif self.look == -1:
            self.image_walk.clip_composite_draw(self.frame * 16, 0, 16, 29, self.rad * 4, 'h', self.x, self.y, 16, 29)

    def jump(self):
        self.jump_time += 0.0001
        if self.look == 1:
            self.image_jump.composite_draw(self.rad * 4, 'None', self.x, self.y)
        elif self.look == -1:
            self.image_jump.composite_draw(self.rad * 4, 'h', self.x, self.y)
        # self.drop += self.gravity

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        # self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
        # fill here

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)
