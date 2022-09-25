# ************************
# Special class defining file for cell types
# - Contains C  E  L  L  S
# You know, just in case
# *********************

import pygame, math

class Cell:
    def __init__(self):
        self.type = "Unspecialised cell"
        self.spec_cost = 0
        self.produced = [-0.02, 0, 0, 0]
        self.specBpossible = False
        self.cooldown = 100
        self.cooldownSpeed = 0
        self.description = [
                "- Consumes Data",
                "- Can be specialised",
                "into a data collector",
                "- Can be divided",
                "- Spec cost : 10",
                "",
            ]

    def divide(self,board):
        x = board.tile_selected.tilex
        y = board.tile_selected.tiley
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
            tile = board.tiles[tile_index[0]][tile_index[1]]
            if not tile.dataType:
                tile.add_cell(Cell())
                break

    def run(self, game, pos):

        debuff = math.log10(int(game.visibility)+1)-3
        if debuff < 1:
             debuff = 1

        x = pos[0]
        y = pos[1]
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
        types = ["data","mass data", "prime numbers", "pi decimals"]
        types_produced = []
        m = 0
        for a in self.produced:
            if a != 0:
                types_produced.append(m)
            m +=1
        active = True
        a = 0
        for current_type in types_produced:
            a = 0
            for tile_index in neighbor_tiles:
                if tile_index[0]<0 or tile_index[0]>9 or tile_index[1]<0 or tile_index[1]>9:
                    continue
                tile = game.board.tiles[tile_index[0]][tile_index[1]]
                if tile.dataType == types[current_type] and tile.dataCount >= (-1)*self.produced[current_type]:
                    a = 1
                    break
            if a == 0:
                active = False
            break
        if active:
            for current_type in list(range(4)):
                for tile_index in neighbor_tiles:
                    if tile_index[0]<0 or tile_index[0]>9 or tile_index[1]<0 or tile_index[1]>9:
                        continue
                    tile = game.board.tiles[tile_index[0]][tile_index[1]]
                    if tile.dataType == types[current_type]:
                        tile.dataCount += self.produced[current_type]




        #game.data += self.produced[0]*debuff
        game.visibility += abs(self.produced[0])# the antivirus notices any changes made to the System, including data processing
        #game.mass_data += self.produced[1]*debuff
        game.visibility += abs(self.produced[1])*10
        #game.prime_numbers += self.produced[2]*debuff
        game.visibility += abs(self.produced[2])*100
        #game.pi += self.produced[3]*debuff
        game.visibility += abs(self.produced[3])

        self.cooldown -= self.cooldownSpeed
        if self.type == "Camouflage cell" and game.visibility > 100:
            game.visibility -= 100
        

    def specA(self, game, tile):
        if self.type == "Unspecialised cell":
            tile.cell = DataCollector()
        elif self.type == "Data collector cell":
            self.type = "Mass data collector"
            self.spec_cost = [100, 0, 0, 0]
            self.produced = [-0.4, 0.05, 0, 0]
            self.description = [
                "- Produces Mass data",
                "- Can't be divided",
                "- Can be re-specialised",
                "  into a prime number",
                "  collector",
                "",
            ]
            self.specBpossible = False
            self.cooldownSpeed = 0
        elif self.type == "Mass data collector":
            self.type = "Prime number collector"
            self.spec_cost = [0, 200, 0, 0]
            self.produced = [-0.2, -0.15, 0.01, 0]
            self.description = [
                "- Finds prime numbers",
                "  using a simple method",
                "- uses mass data",
                "- Opens new possibilities",
                "- Has two possible respecs",
                "",
            ]
            self.specBpossible = True
            self.cooldownSpeed = 0
        elif self.type == "Prime number collector":
            self.type = "Pi decimals calculator"
            self.produced = [-0.4, 0, -0.005, 15]
            self.description = [
                "- Calculates the decimal",
                "  places of the pi constant",
                "- They can be used",
                "  for decreasing visibility",
                "- Unlocks new possibilities",
                "",
            ]
            self.specBpossible = False
            self.cooldownSpeed = 0
            self.spec_cost = [0, 0, 100, 0]
            self.cooldown = 100
        elif self.type == "Pi decimals calculator":
            self.type = "Eff-prime cell"
            self.produced = [-0.2, -0.05, 0.005, -3]
            self.description = [
                "- Calculates prime numbers",
                "  more efficiently using",
                "  less input data.",
                "- Produces less prime numbers",
                "  than the original",
                "",
            ]
            self.specBpossible = False
            self.cooldownSpeed = 0
            self.spec_cost = [0, 0, 100, 1000]
            self.cooldown = 100

        elif self.type == "Replicator cell":
            if not game.terminal_already_exists:
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
                game.terminal_already_exists = True
    
    def specB(self, tile):
        if self.type == "Data collector cell":
            self.type = "Camouflage cell"
            self.spec_cost = [0, 0, 0, 100]
            self.produced = [0, 0, 0, -10]
            self.description = [
                "- Decreases Visibility",
                "  to remove debuffs",
                "- You will need",
                "  a lot of them",
                "  to cover everything",
                "",
            ]
            self.specBpossible = False
            self.cooldownSpeed = 0
        elif self.type == "Prime number collector":
            self.type = "Replicator cell"
            self.produced = [-0.5, -0.2, 0, 0]
            self.description = [
                "- Divides auromatically",
                "- Uses only mass data",
                "- Can be reversed into",
                "  an unspecialiced cell",
                "- Replicating can't be stopped",
                "",
            ]
            self.specBpossible = False
            self.cooldownSpeed = 0.5
            self.spec_cost = [0,0,100,0]
        self.cooldown = 100
class DataCollector(Cell):
    def __init__(self):
        super().__init__()
        self.type = "Data collector cell"
        self.spec_cost = [10, 0, 0, 0]
        self.produced = [0.2, 0, 0, 0]
        self.description = [
            "- Produces Data",
            "- Can't be divided",
            "- Can be re-specialised",
            "  into a Mass",
            "  Data collector",
            "",
        ]
        self.specBpossible = True
        self.cooldownSpeed = 0
