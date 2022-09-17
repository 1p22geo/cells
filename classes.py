# *****************************
# The class defining file
# - All the objects and items in the game are defined here as classes
#   and then created as instances via other class methods or the game file
# *****************************

import pygame
import program.data.constants as const


class Tile:
    def __init__(self, tilex, tiley, size,ref):
        self.tiley = tiley
        self.ref = ref
        self.tilex = tilex
        self.cell = None
        self.dataType = None
        self.ICON_SIZE = 20
        self.CELL_SIZE = 40
        self.dataCount = 0
        self.size = size
        self.image = pygame.image.load("images\\Tile_dark_gradient_2.png")
        self.data_image = pygame.image.load("images\\data_icon_yellow.png")
        self.mass_data_image = pygame.image.load("images\\mass_data_icon.png")
        self.prime_image = pygame.image.load("images\\prime_data_icon.png")
        self.pi_image = pygame.image.load("images\\pi_data_icon.png")
        self.images = [
            pygame.image.load("images\\Tile_dark_gradient_2.png"),
            pygame.image.load("images\\backdrop_dark.png"),
            pygame.image.load("images\\cell_unspecialised_dblue.png"),
            pygame.image.load("images\\tile_selected_dblue.png"),
            pygame.image.load("images\\X_button_red.png"),
            pygame.image.load("images\\divide_button_blue.png"),
            pygame.image.load("images\\spec_button_blue.png"),
            pygame.image.load("images\\move_button_blue.png"),
            pygame.image.load("images\\data_icon_yellow.png"),
            pygame.image.load("images\\cell_datacollect_yellow_digits.png"),
            pygame.image.load("images\\mass_data_icon.png"),#10
            pygame.image.load("images\\mass_data_collector.png"),
            pygame.image.load("images\\death_screen.png"),
            pygame.image.load("images\\select_respec.png"),
            pygame.image.load("images\\cell_prime_collect.png"),
            pygame.image.load("images\\prime_data_icon.png"),#15
            pygame.image.load("images\\cell_replicate_rubarb.png"),
            pygame.image.load("images\\pi.png"),
            pygame.image.load("images\\camo_cell.png"),
            pygame.image.load("images\\pi_data_icon.png"),
            pygame.image.load("images\\eff_prime_finder.png"),#20
            pygame.image.load("images\\user_terminal_cell.png"),
        ]

    def add_cell(self, cell):
        self.cell = cell
        self.dataType = "cell"

    def pop_cell(self):
        self.dataType = None
        temp = self.cell
        self.cell = None
        return temp

    def draw(self,display):
        if self.dataType == "data":
            display.blit(
                self.data_image, [self.tilex* self.size + self.ref[0] + (self.size-self.ICON_SIZE)/2, self.tiley* self.size + self.ref[1] + (self.size-self.ICON_SIZE)/2]
            )
        if self.dataType == "mass data":
            display.blit(
                self.mass_data_image, [self.tilex* self.size + self.ref[0] + (self.size-self.ICON_SIZE)/2, self.tiley* self.size + self.ref[1] + (self.size-self.ICON_SIZE)/2]
            )
        if self.dataType == "prime numbers":
            display.blit(
                self.prime_image, [self.tilex* self.size + self.ref[0] + (self.size-self.ICON_SIZE)/2, self.tiley* self.size + self.ref[1] + (self.size-self.ICON_SIZE)/2]
            )
        if self.dataType == "pi decimals":
            display.blit(
                self.pi_image, [self.tilex* self.size + self.ref[0] + (self.size-self.ICON_SIZE)/2, self.tiley* self.size + self.ref[1] + (self.size-self.ICON_SIZE)/2]
            )

    def draw_cell(self,display):
        if self.cell.type == "Unspecialised cell":
            display.blit(
                self.images[2], [self.tilex * self.size + self.ref[0] + (self.size-self.CELL_SIZE)/2, self.tiley* self.size + self.ref[1] + (self.size-self.CELL_SIZE)/2]
            )
        if self.cell.type == "Data collector cell":
            display.blit(
                self.images[9], [self.tilex* self.size + self.ref[0] + (self.size-self.CELL_SIZE)/2, self.tiley* self.size + self.ref[1] + (self.size-self.CELL_SIZE)/2]
            )
        if self.cell.type == "Mass data collector":
            display.blit(
                self.images[11], [self.tilex* self.size + self.ref[0] + (self.size-self.CELL_SIZE)/2, self.tiley* self.size + self.ref[1] + (self.size-self.CELL_SIZE)/2]
            )
        if self.cell.type == "Prime number collector":
            display.blit(
                self.images[14], [self.tilex* self.size + self.ref[0] + (self.size-self.CELL_SIZE)/2, self.tiley* self.size + self.ref[1] + (self.size-self.CELL_SIZE)/2]
            )
        if self.cell.type == "Pi decimals calculator":
            display.blit(
                self.images[17], [self.tilex* self.size + self.ref[0] + (self.size-self.CELL_SIZE)/2, self.tiley* self.size + self.ref[1] + (self.size-self.CELL_SIZE)/2]
            )
        if self.cell.type == "Replicator cell":
            display.blit(
                self.images[16], [self.tilex* self.size + self.ref[0] + (self.size-self.CELL_SIZE)/2, self.tiley* self.size + self.ref[1] + (self.size-self.CELL_SIZE)/2]
            )
        if self.cell.type == "Camouflage cell":
            display.blit(
                self.images[18], [self.tilex* self.size + self.ref[0] + (self.size-self.CELL_SIZE)/2, self.tiley* self.size + self.ref[1] + (self.size-self.CELL_SIZE)/2]
            )
        if self.cell.type == "Eff-prime cell":
            display.blit(
                self.images[20], [self.tilex* self.size + self.ref[0] + (self.size-self.CELL_SIZE)/2, self.tiley* self.size + self.ref[1] + (self.size-self.CELL_SIZE)/2]
            )
        if self.cell.type == "User terminal":
            display.blit(
                self.images[21], [self.tilex* self.size + self.ref[0] + (self.size-self.CELL_SIZE)/2, self.tiley* self.size + self.ref[1] + (self.size-self.CELL_SIZE)/2]
            )


class Board:
    def __init__(self, size,tilesize, ref):
        self.tiles = []
        self.tile_selected = None
        self.ref = ref
        self.size = size
        self.tilesize = tilesize
        for m in range(size[0]):
            self.tiles.append([])
            for n in range(size[1]):
                self.tiles[-1].append(Tile(m, n, tilesize,ref))
    
    def click_handle(self,click):
        if click[0] > self.ref[0] and click[0] < self.ref[0]+self.size[0]*self.tilesize:
            if click[1] > self.ref[1] and click[1] < self.ref[1]+self.size[1]*self.tilesize:
                x = int((click[0]-self.ref[0])/self.tilesize)
                y = int((click[1]-self.ref[1])/self.tilesize)
                return self.tiles[x][y]



class Button:
    def __init__(self,image,pos,panel_pos):
        self.image = image
        self.pos = pos
        self.panel_pos = panel_pos
        self.size = (260,40)   #TODO scale image to the size

    def blit(self,display):
        display.blit(self.image,(self.pos[0]+self.panel_pos[0],self.pos[1]+self.panel_pos[1]))