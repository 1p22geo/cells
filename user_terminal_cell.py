import pygame, math
from unspec_cell import Cell
import constants as const

class User_terminal(Cell):
    def __init__(self):
        self.level = 0
        self.type = "User terminal"
        self.description = [
            "- Contacts with the User",
            "  in order for him to",
            "  notice we're useful.",
            "- Requires sacrifices from",
            "  different types of data",
            "",
        ]
        self.produced = [0,0,0,0]
        self.cooldownSpeed = 0
        self.spec_cost = [0, 0, 50, 500]
        self.cooldown = 100
        self.specBpossible = False

    def raise_level(self, game):
        print(1)
        current_type = const.terminal_level_req_unit[self.level]
        needed = const.terminal_level_req[self.level]
        x = game.board.tile_selected.tilex
        y = game.board.tile_selected.tiley
        neighbor_tiles = \
        [
            [x+1,y],
            [x+1,y+1],
            [x,y+1],
            [x-1,y+1],
            [x-1,y],
            [x-1,y-1],
            [x,y-1],
            [x+1,y-1]
        ]
        for tile_index in neighbor_tiles:
            print(2)
            if tile_index[0]<0 or tile_index[0]>9 or tile_index[1]<0 or tile_index[1]>9:
                continue
            tile = game.board.tiles[tile_index[0]][tile_index[1]]
            if tile.dataType == current_type:
                print(3)
                if tile.dataCount >= needed: # debug
                    tile.dataCount -= needed
                    self.level +=1
                    break