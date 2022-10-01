import pygame
import constants as const
import classes as classes


class Panel:
    def __init__(self, pos, display):
        self.image = pygame.image.load("images\\tile_selected_dblue.png")
        self.X_image = pygame.image.load("images\\X_button_red.png")
        self.data_image = pygame.image.load("images\\data_icon_yellow.png")
        self.mass_data_image = pygame.image.load("images\\mass_data_icon.png")
        self.prime_image = pygame.image.load("images\\prime_data_icon.png")
        self.pi_image = pygame.image.load("images\\pi_data_icon.png")
        self.active = False
        self.display = display
        self.pos = pos
        self.font = pygame.font.Font(None, 40)
        self.font_small = pygame.font.Font(None, 30)
        self.XBUTTONPOS = (360, 20)
        self.XBUTTONSIZE = 20
        self.button1a = classes.Button(pygame.image.load(
            "images\\divide_button_blue.png"), (40, 400), self.pos)
        self.button1b = classes.Button(pygame.image.load(
            "images\\spec_button_blue.png"), (40, 400), self.pos)
        self.button2 = classes.Button(pygame.image.load(
            "images\\spec_button_blue.png"), (40, 450), self.pos)
        self.button3 = classes.Button(pygame.image.load(
            "images\\move_button_blue.png"), (40, 500), self.pos)
        self.button3b = classes.Button(pygame.image.load(
            "images\\terminal_upgrade.png"), (40, 500), self.pos)

    def is_x_clicked(self, click):
        if click[0] > self.pos[0]+self.XBUTTONPOS[0] and click[0] < self.pos[0]+self.XBUTTONPOS[0] + self.XBUTTONSIZE:
            if click[1] > self.pos[1]+self.XBUTTONPOS[1] and click[1] < self.pos[1]+self.XBUTTONPOS[1] + self.XBUTTONSIZE:
                return True

    def blit(self, display, game):
        display.blit(self.image, self.pos)
        display.blit(
            self.X_image, (self.pos[0]+self.XBUTTONPOS[0], self.pos[1] + self.XBUTTONPOS[1]))
        disp_string_1 = (
            "Tile " + str(game.board.tile_selected.tilex) +
            ", " + str(game.board.tile_selected.tiley)
        )
        if game.board.tile_selected.cell:
            cell_type = game.board.tile_selected.cell.type
            disp_string_2 = game.board.tile_selected.cell.type
        else:
            disp_string_2 = (
                str(game.board.tile_selected.dataType)).capitalize()
            cell_type = None
        disp_text_surface_1 = self.font.render(disp_string_1, 1, (0, 0, 255))
        disp_text_surface_2 = self.font.render(disp_string_2, 1, (0, 0, 255))
        self.display.blit(
            disp_text_surface_1,
            (
                self.pos[0] + 40,
                self.pos[1] + 40,
            ),
        )
        self.display.blit(
            disp_text_surface_2,
            (
                self.pos[0] + 40,
                self.pos[1] + 100,
            ),
        )

    def check_click(self, tile_selected, click, game):
        if tile_selected.cell:
            if (tile_selected.cell.specBpossible):
                if (click[0] >= self.pos[0] + 40 and click[0] <= self.pos[0] + 300 and click[1] >= self.pos[1] + 400 and click[1] <= self.pos[1] + 440):
                    tile_selected.cell.specB(tile_selected)
            elif (tile_selected.cell.type == "Unspecialised cell"):
                if (click[0] >= self.pos[0] + 40 and click[0] <= self.pos[0] + 300 and click[1] >= self.pos[1] + 400 and click[1] <= self.pos[1] + 440):
                    tile_selected.cell.divide(game.board)
            if (click[0] >= self.pos[0] + 40 and click[0] <= self.pos[0] + 300 and click[1] >= self.pos[1] + 450 and click[1] <= self.pos[1] + 490):
                tile_selected.cell.specA(game, tile_selected)

            if (click[0] >= self.pos[0] + 40 and click[0] <= self.pos[0] + 300 and click[1] >= self.pos[1] + 500 and click[1] <= self.pos[1] + 540):
                if tile_selected.cell.type == "User terminal":
                    tile_selected.cell.raise_level(game)
                else:
                    temp = tile_selected.pop_cell()
                    game.place_cell = temp
        else:
            if (click[0] >= self.pos[0] + 50 and click[0] <= self.pos[0] + 70 and click[1] >= self.pos[1] + 300 and click[1] <= self.pos[1] + 320):
                tile_selected.dataType = "data"
            elif (click[0] >= self.pos[0] + 100 and click[0] <= self.pos[0] + 120 and click[1] >= self.pos[1] + 300 and click[1] <= self.pos[1] + 320):
                tile_selected.dataType = "mass data"
            elif (click[0] >= self.pos[0] + 150 and click[0] <= self.pos[0] + 170 and click[1] >= self.pos[1] + 300 and click[1] <= self.pos[1] + 320):
                tile_selected.dataType = "prime numbers"
            elif (click[0] >= self.pos[0] + 50 and click[0] <= self.pos[0] + 70 and click[1] >= self.pos[1] + 350 and click[1] <= self.pos[1] + 370):
                tile_selected.dataType = "pi decimals"

    def draw_1(self, tile_selected):

        disp_string_3 = ["", "", "", "", "", ""]
        if tile_selected.cell:
            if tile_selected.cell.description:
                disp_string_3 = tile_selected.cell.description

        disp_text_surface_3 = self.font_small.render(
            disp_string_3[0], 1, (0, 0, 255))
        disp_text_surface_4 = self.font_small.render(
            disp_string_3[1], 1, (0, 0, 255))
        disp_text_surface_5 = self.font_small.render(
            disp_string_3[2], 1, (0, 0, 255))
        disp_text_surface_6 = self.font_small.render(
            disp_string_3[3], 1, (0, 0, 255))
        disp_text_surface_7 = self.font_small.render(
            disp_string_3[4], 1, (0, 0, 255))
        disp_text_surface_8 = self.font_small.render(
            disp_string_3[5], 1, (0, 0, 255))

        self.display.blit(
            disp_text_surface_3,
            (
                self.pos[0] + 40,
                self.pos[1] + 160,
            ),
        )
        self.display.blit(
            disp_text_surface_4,
            (
                self.pos[0] + 40,
                self.pos[1] + 200,
            ),
        )
        self.display.blit(
            disp_text_surface_5,
            (
                self.pos[0] + 40,
                self.pos[1] + 240,
            ),
        )
        self.display.blit(
            disp_text_surface_6,
            (
                self.pos[0] + 40,
                self.pos[1] + 280,
            ),
        )
        self.display.blit(
            disp_text_surface_7,
            (
                self.pos[0] + 40,
                self.pos[1] + 320,
            ),
        )
        self.display.blit(
            disp_text_surface_8,
            (
                self.pos[0] + 40,
                self.pos[1] + 360,
            ),
        )

        if tile_selected.cell.type == "Unspecialised cell":
            self.button1a.blit(self.display)
        elif tile_selected.cell.specBpossible:
            self.button1b.blit(self.display)
        self.button2.blit(self.display)
        self.button3.blit(self.display)

    def draw_2(self, terminal_level):
        disp_text_surface_3 = self.font_small.render(
            "level "+str(terminal_level), 1, (0, 0, 255))
        disp_text_surface_4 = self.font_small.render(
            str(const.terminal_level_req[terminal_level]), 1, (0, 0, 255))
        disp_text_surface_5 = self.font_small.render(
            str(const.terminal_level_req_unit[terminal_level]), 1, (0, 0, 255))
        disp_text_surface_6 = self.font_small.render(
            "Needed for next level", 1, (0, 0, 255))

        self.display.blit(
            disp_text_surface_3,
            (
                self.pos[0] + 40,
                self.pos[1] + 160,
            ),
        )
        self.display.blit(
            disp_text_surface_4,
            (
                self.pos[0] + 40,
                self.pos[1] + 200,
            ),
        )
        self.display.blit(
            disp_text_surface_5,
            (
                self.pos[0] + 40,
                self.pos[1] + 240,
            ),
        )
        self.display.blit(
            disp_text_surface_6,
            (
                self.pos[0] + 40,
                self.pos[1] + 280,
            ),
        )
        self.button3b.blit(self.display)

    def draw_3(self, tile_selected):

        self.display.blit(
            self.data_image,
            (
                self.pos[0] + 50,
                self.pos[1] + 300,
            ),
        )
        self.display.blit(
            self.mass_data_image,
            (
                self.pos[0] + 100,
                self.pos[1] + 300,
            ),
        )
        self.display.blit(
            self.prime_image,
            (
                self.pos[0] + 150,
                self.pos[1] + 300,
            ),
        )
        self.display.blit(
            self.pi_image,
            (
                self.pos[0] + 50,
                self.pos[1] + 350,
            ),
        )
        disp_text_surface_4 = self.font_small.render(
            str(int(tile_selected.dataCount)), 1, (0, 0, 255))
        self.display.blit(
            disp_text_surface_4,
            (
                self.pos[0] + 40,
                self.pos[1] + 200,
            ),
        )
