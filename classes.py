# *****************************
# The class defining file
# - All the objects and items in the game are defined here as classes
#   and then created as instances via other class methods or the game file
# *****************************

import pygame
import constants as const
from tile import Tile


class Board:
    def __init__(self, size, tilesize, ref):
        self.tiles = []
        self.tile_selected = None
        self.ref = ref
        self.size = size
        self.tilesize = tilesize
        for m in range(size[0]):
            self.tiles.append([])
            for n in range(size[1]):
                self.tiles[-1].append(Tile(m, n, tilesize, ref))

    def click_handle(self, click):
        if click[0] > self.ref[0] and click[0] < self.ref[0]+self.size[0]*self.tilesize:
            if click[1] > self.ref[1] and click[1] < self.ref[1]+self.size[1]*self.tilesize:
                x = int((click[0]-self.ref[0])/self.tilesize)
                y = int((click[1]-self.ref[1])/self.tilesize)
                return self.tiles[x][y]


class Button:
    def __init__(self, image, pos, panel_pos):
        self.image = image
        self.pos = pos
        self.panel_pos = panel_pos
        self.size = (260, 40)  # TODO scale image to the size

    def blit(self, display):
        display.blit(
            self.image, (self.pos[0]+self.panel_pos[0], self.pos[1]+self.panel_pos[1]))
