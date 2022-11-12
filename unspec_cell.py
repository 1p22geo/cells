import math


class Cell:
    def __init__(self):
        self.active = True
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

    def act(self, game):
        """"
        Why don't we have abstract methods in Python?
        Honestly, that would be useful
        """
        pass

    def divide(self, board):
        x = board.tile_selected.tilex
        y = board.tile_selected.tiley
        neighbor_tiles = self.generate_neighbor_indexes(x, y)
        for tile_index in neighbor_tiles:
            if tile_index[0] < 0 or tile_index[0] > 9 or tile_index[1] < 0 or tile_index[1] > 9:
                continue
            tile = board.tiles[tile_index[0]][tile_index[1]]
            if not tile.dataType:
                tile.add_cell(Cell())
                break

    def is_tile_invalid(self, tile_index):
        if tile_index[0] < 0 or tile_index[0] > 9 or tile_index[1] < 0 or tile_index[1] > 9:
            return True
        return False

    def generate_neighbor_indexes(self, x, y):
        return \
            [
                [x+1, y],
                [x+1, y+1],
                [x, y+1],
                [x-1, y+1],
                [x-1, y],
                [x-1, y-1],
                [x, y-1],
                [x+1, y-1]
            ]

    def run(self, game, pos):

        debuff = math.log10(int(game.visibility)+1)-3
        if debuff < 1:
            debuff = 1
        x = pos[0]
        y = pos[1]
        neighbor_tiles = self.generate_neighbor_indexes(x, y)

        types = ["data", "mass data", "prime numbers", "pi decimals"]
        needed = []
        supporting_tiles = {}
        for a in range(len(self.produced)):
            if self.produced[a] != 0:
                needed.append(a)
        for tile_index in neighbor_tiles:
            if self.is_tile_invalid(tile_index):
                continue
            tile = game.board.tiles[tile_index[0]][tile_index[1]]
            if not tile.dataType or tile.cell:
                continue
            if types.index(tile.dataType) in needed:
                if self.produced[types.index(tile.dataType)] < 0 and tile.dataCount < 0:
                    continue
                supporting_tiles[tile.dataType] = tile
                needed.remove(types.index(tile.dataType))
        if not needed:
            self.active = True
            for type, tile in supporting_tiles.items():
                tile.dataCount += self.produced[types.index(type)]
        else:
            self.active = False

        #game.data += self.produced[0]*debuff
        # the antivirus notices any changes made to the System, including data processing
        game.visibility += abs(self.produced[0])
        #game.mass_data += self.produced[1]*debuff
        game.visibility += abs(self.produced[1])*10
        #game.prime_numbers += self.produced[2]*debuff
        game.visibility += abs(self.produced[2])*100
        #game.pi += self.produced[3]*debuff
        game.visibility += abs(self.produced[3])
        if self.active:
            self.act(game)
            self.cooldown -= self.cooldownSpeed

    def specA(self, game, tile):
        import cells
        import user_terminal_cell
        if self.type == "Unspecialised cell":
            tile.cell = cells.DataCollector()
        elif self.type == "Data collector cell":
            tile.cell = cells.MassCollector()
        elif self.type == "Mass data collector":
            tile.cell = cells.PrimeCollector()
        elif self.type == "Prime number collector":
            tile.cell = cells.PiCollector()
        elif self.type == "Pi decimals calculator":
            tile.cell = cells.EffPrime()

        elif self.type == "Replicator cell":
            if not game.terminal_already_exists:
                tile.cell = user_terminal_cell.User_terminal()
                game.terminal_already_exists = True

    def specB(self, tile):
        import cells
        if self.type == "Data collector cell":
            tile.cell = cells.Camo_Cell()
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
            self.spec_cost = [0, 0, 100, 0]
        self.cooldown = 100
