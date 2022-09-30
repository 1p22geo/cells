# ******************************
# The game class file
# - holds all the game objects and sprites
# - holds most of the game variables
# *****************************
import pygame
from random import choice, randint
import math
import classes as classes
import constants as const
import unspec_cell as cell
import panel as panel

class Game:
    def __init__(self, tilesize,display):
        self.running = True
        self.mousePos = [0, 0]
        self.clicks = []
        self.board = classes.Board(const.MAP_SIZE, tilesize,(100,100))

        self.TILE_SELECTED_DIALOGUE_POS = [700, 100]
        self.panel = panel.Panel(self.TILE_SELECTED_DIALOGUE_POS,display)
        self.tile_selected = None
        self.cell_divide = False
        self.place_cell = None
        self.visibility = 0
        self.board.tiles[4][4].add_cell(cell.Cell())
        self.terminal_already_exists = False
        self.gameover = False
        self.gamepause = 0
        self.cutscene = 0
        self.terminal_level = 0
        self.cutscene_displayed = None

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.clicks.append(self.mousePos)
            if event.type == pygame.MOUSEMOTION:
                self.mousePos = list(event.pos)

    def run_game_loop(self):
        m = 0
        for row in self.board.tiles:
            n = 0
            for tile in row:

                if tile.cell:
                    if tile.cell.type == "Replicator cell":
                        if tile.cell.cooldown <= 0:
                            x = tile.tilex
                            y = tile.tiley
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
                                if tile_index[0]<0 or tile_index[0]>9 or tile_index[1]<0 or tile_index[1]>9:
                                    continue
                                tile_c = self.board.tiles[tile_index[0]][tile_index[1]]
                                if not tile.dataType:
                                    tile_c.add_cell(cell.Cell())
                                    break
                            tile.cell.cooldown = 100
                    
                    tile.cell.run(self, (m,n))
                   
                    
                    if self.visibility >= 10_000:
                        chance = int(math.pow(10,(7.5-math.log10(self.visibility+1))))
                        if chance < 10:
                            chance= 10
                        if randint(1,chance) == 1:
                            tile.pop_cell()
                    if self.visibility >= 50_000:
                        self.data -= int(math.pow(10,(math.log10(self.visibility+1))-4))
                        
                n += 1
            m += 1

    def check_cutscenes(self):
        if self.cutscene == 0:
            self.gamepause = 2
            self.cutscene_displayed = pygame.image.load("images\\cutscene_1.png")
            self.cutscene = 1
        elif self.cutscene == 1:
            pass
        
