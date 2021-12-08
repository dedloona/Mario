import random
import json
import os

from pico2d import *
import game_framework
import game_world

from mario_player import Mario
from BG import BackGround
from tile import *
from stage1 import stage1
import server
from collision import collide

name = "MainState"




def enter():

    server.mario = Mario()
    game_world.add_object(server.mario, 1)

    server.bg = BackGround()
    game_world.add_object(server.bg, 0)

    server.stage = stage1

    # server.tiles = [[Tiles() for x in range (200)] for y in range (16)]
    # game_world.add_objects(server.tiles, 1)

    for i in range(16):
        for j in range(200):
            if server.stage[i][j] == 1:
                grass = Grass(j * 16 + 8, i * 16 + 8)
                print(grass.x, grass.y)
                game_world.add_object(grass, 1)
            if server.stage[i][j] == 4:
                pipes = Pipe1(j * 16 + 8, i * 16 + 8)
                game_world.add_object(pipes, 1)
            if server.stage[i][j] == 5:
                pipes = Pipe2(j * 16 + 8, i * 16 + 8)
                game_world.add_object(pipes, 1)
            if server.stage[i][j] == 6:
                pipes = Pipe3(j * 16 + 8, i * 16 + 8)
                game_world.add_object(pipes, 1)
            if server.stage[i][j] == 7:
                pipes = Pipe4(j * 16 + 8, i * 16 + 8)
                game_world.add_object(pipes, 1)



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
            server.mario.handle_event(event)
            pass


def update():

    for game_object in game_world.all_objects():
        game_object.update()








def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()
