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
from monster import Gumba

name = "MainState"




def enter():

    server.bg = BackGround()
    game_world.add_object(server.bg, 0)

    server.gumba = Gumba(300, 24)
    game_world.add_object(server.gumba, 1)

    server.stage = stage1
    server.mario = Mario()
    game_world.add_object(server.mario, 1)

    for i in range(16):
        for j in range(200):
            if server.stage[i][j] == 1:
                server.tiles = Grass((j * 16 + 8) - server.mario.velocity, 256 - i * 16 - 8)
                game_world.add_object(server.tiles, 1)
            if server.stage[i][j] == 4:
                server.tiles = Pipe1(j * 16 + 8, 256 - i * 16 - 8)
                game_world.add_object(server.tiles, 1)
            if server.stage[i][j] == 5:
                server.tiles = Pipe2(j * 16 + 8, 256 - i * 16 - 8)
                game_world.add_object(server.tiles, 1)
            if server.stage[i][j] == 6:
                server.tiles = Pipe3(j * 16 + 8, 256 - i * 16 - 8)
                game_world.add_object(server.tiles, 1)
            if server.stage[i][j] == 7:
                server.tiles = Pipe4(j * 16 + 8, 256 - i * 16 - 8)
                game_world.add_object(server.tiles, 1)






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
