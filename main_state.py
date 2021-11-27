import random
import json
import os

from pico2d import *
import game_framework
import game_world

from mario_player import Mario
from BG import BackGround
from grass import Grass
import stage1

name = "MainState"

mario = None
bg = []
grass = None
stage =

def enter():
    global mario
    mario = Mario()
    game_world.add_object(mario, 1)

    global bg
    bg = BackGround()
    game_world.add_object(bg, 0)

    global grass
    grass = Grass()
    game_world.add_object(grass, 0)




def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            # mario.handle_event(event)
            pass


def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
