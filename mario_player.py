from pico2d import *
import game_framework
import server
from ball import Ball
import game_world
from collision import collide

RIGHT_DOWN, LEFT_DOWN, RIGHT_UP, LEFT_UP, JUMP, SPACE, TO_RUN = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYDOWN, SDLK_LEFT): LEFT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYUP, SDLK_LEFT): LEFT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_j): JUMP

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
FRAMES_PER_ACTION = 1


# class IdleState:
#
#     def enter(mario, event):
#         if event == RIGHT_DOWN:
#             mario.velocity += RUN_SPEED_PPS
#         elif event == LEFT_DOWN:
#             mario.velocity -= RUN_SPEED_PPS
#         elif event == RIGHT_UP:
#             mario.velocity -= RUN_SPEED_PPS
#         elif event == LEFT_UP:
#             mario.velocity += RUN_SPEED_PPS
#
#     def exit(mario, event):
#         if mario == FIRE:
#             mario.fire_ball()
#         pass
#
#     def do(mario):
#         mario.frame = (mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
#         # mario.timer -= 1
#         # if mario.timer == 0:
#         #     pass
#
#     def draw(mario):
#         if mario.dir == 1:
#             mario.image_idle.composite_draw(mario.rad * 4, 'None', mario.x, mario.y, 16, 29)
#         else:
#             mario.image_idle.composite_draw(mario.rad * 4, 'h', mario.x, mario.y, 16, 29)


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

        # mario.dir = clamp(-1, mario.velocity, 1)

    def exit(mario, event):
        if event == SPACE:
             mario.fire_ball()


    def do(mario):
        # boy.frame = (boy.frame + 1) % 8
        mario.frame = int((mario.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time + 1) % 3)
        mario.x += mario.velocity * game_framework.frame_time

        # mario.x = clamp(25, mario.x, 600 - 25)
        if mario.x >= 570:
            mario.x = clamp(525 , mario.x ,575)

    def draw(mario):

        # cx, cy = mario.x - server.background.window_left, mario.y - server.background.window_bottom
        if mario.velocity > 0:
            mario.image_walk.clip_composite_draw(mario.frame * 16, 0, 16, 29, mario.rad * 4, 'None', mario.x, mario.y, 16, 29)
            mario.dir = 1

        elif mario.velocity < 0:
            mario.image_walk.clip_composite_draw(mario.frame * 16, 0, 16, 29, mario.rad * 4, 'h', mario.x, mario.y, 16, 29)
            mario.dir = -1

        else:
    #  velocity == 0
            if mario.dir == 1:
                mario.image_idle.composite_draw(mario.rad * 4, 'None', mario.x, mario.y, 16, 29)

            else:
                mario.image_idle.composite_draw(mario.rad * 4, 'h', mario.x, mario.y, 16, 29)




class JumpState:

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

        if collide(mario, server.tiles):
            event = TO_RUN

    def do(mario):

        mario.jump_time += game_framework.frame_time + 0.0001
        mario.drop += mario.gravity * game_framework.frame_time
        mario.x += mario.velocity * game_framework.frame_time

        mario.height = (mario.jump_time * mario.power) - (mario.jump_time ** 2 * mario.gravity / 2)
        mario.y += mario.height + (mario.drop * game_framework.frame_time)

        if mario.height < 0:
            if mario.y <= 28:
                mario.y = 28
                mario.drop = 0
                mario.jump_time = 0
                mario.add_event(TO_RUN)
        if mario.x >= 570:
            mario.x = clamp(525 , mario.x ,575)




    def draw(mario):

        if mario.dir == 1:
            mario.image_jump.composite_draw(mario.rad * 4, 'None', mario.x, mario.y)
        else:
            mario.image_jump.composite_draw(mario.rad * 4, 'h', mario.x, mario.y)








next_state_table = {

    RunState: {RIGHT_UP: RunState, LEFT_UP: RunState, LEFT_DOWN: RunState, RIGHT_DOWN: RunState,JUMP: JumpState, SPACE: RunState},
    JumpState: {LEFT_DOWN: JumpState, RIGHT_DOWN: JumpState, LEFT_UP: JumpState, RIGHT_UP: JumpState, JUMP: JumpState, SPACE: JumpState, TO_RUN: RunState}
}




class Mario:

    def __init__(self):
        self.image_idle = load_image('Resources/used/marioes/mario_idle.png')
        self.image_walk = load_image('Resources/used/marioes/walk_animation.png')
        self.image_jump = load_image('Resources/used/marioes/mario_jump.png')
        self.x, self.y = 16, 28
        self.width, self.height = 16, 0
        self.frame = 0
        self.rad = 1.5708
        self.gravity = 9.8
        self.drop = 2.5
        self.dir = 1
        self.velocity = 0
        self.power = 3.5
        self.jump_time = 0
        self.event_que = []
        self.cur_state = RunState
        self.cur_state.enter(self, None)
        self.top = self.y + 14
        self.bottom = self.y - 14
        self.left = self.x - 8
        self.right = self.x + 8

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        # print(self.dir, self.velocity)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        if server.mario.x >= 1000 // 2:
            server.tiles.x += -(self.velocity * game_framework.frame_time)
            server.bg.x += -(self.velocity * game_framework.frame_time)

        if self.height <0:
            if collide(self, server.tiles):
                self.y = server.tiles.top
                self.drop = 0

        print(self.height)

    def draw(self):
        self.cur_state.draw(self)
        # self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))

    def fire_ball(self):
        ball = Ball(self.x, self.y, self.dir)
        game_world.add_object(ball, 1)



    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):
        return self.left, self.right, self.top, self.bottom
