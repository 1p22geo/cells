import pygame
import program.data.cells as cells
import program.data.constants as const

class Graphics:
    def __init__(self):
        self.images = [
            pygame.image.load("images\\backdrop_dark.png"),
            pygame.image.load("images\\death_screen.png")
        ]
        self.SCREEN_WIDTH = 1200
        self.SCREEN_HEIGHT = 800
        self.MAP_X = 100
        self.MAP_Y = 100
        self.MAP_SIZE = [10, 10]
        self.TILE_SELECTED_DIALOGUE_POS = [700, 100]
        self.TILE_SIZE = 50
        self.CELL_SIZE = 40
        self.ICON_SIZE = 20
        self.XBUTTONPOS = (360, 20)
        self.display = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

    def check_clicks(self,game):
        for click in game.clicks:
            if game.gamepause:
                game.gamepause -=1
            else:
                tile = game.board.click_handle(click)
                if tile:
                    if game.place_cell:
                        tile.add_cell(game.place_cell)
                        game.place_cell = None
                    game.board.tile_selected = tile

                if game.board.tile_selected:  # the X button
                    
                    game.panel.check_click(game.board.tile_selected,click,game)
                    if game.panel.is_x_clicked(click):
                        game.board.tile_selected = None
                        

        game.clicks = []

    def update_screen(
        self,
        game
    ):
        if game.gamepause:
            self.display.blit(game.cutscene_displayed, (0,0))
        else:
            self.display.fill((0, 0, 0))
            self.display.blit(self.images[0], (0, 0))
            m = 0  # displaying tiles
            n = 0
            for row in game.board.tiles:
                n = 0
                for tile in row:
                    self.display.blit(tile.image, [m * tile.size + self.MAP_X, n * tile.size + self.MAP_Y])
                    if tile.dataType == "cell":
                        tile.draw_cell(self.display)
                    elif tile.dataType:
                        tile.draw(self.display)
                    n += 1
                m += 1
            if game.board.tile_selected:  # selected tile dialogue
                font = pygame.font.Font(None, 40)
                font_small = pygame.font.Font(None, 30)
                game.panel.blit(self.display,game)


                if game.board.tile_selected.cell:
                    cell_type = game.board.tile_selected.cell.type
                else:
                    cell_type = None

                if game.board.tile_selected.cell and cell_type != "User terminal":
                    game.panel.draw_1(game.board.tile_selected)
                elif cell_type == "User terminal":
                    game.panel.draw_2(game.terminal_level)
                elif not game.board.tile_selected.cell :
                    game.panel.draw_3(game.board.tile_selected)

            font = pygame.font.Font(None, 35)
            disp_string_4 = "Visibility"
            disp_text_surface_4 = font.render(disp_string_4, 1, (0, 0, 255))
            self.display.blit(disp_text_surface_4, (100, 650))

            font = pygame.font.Font(None, 35)
            disp_string_5 = str(int(game.visibility))
            disp_text_surface_5 = font.render(disp_string_5, 1, (0, 0, 255))
            self.display.blit(disp_text_surface_5, (100, 700))

            if game.gameover:
                self.display.fill((0,0,0))
                self.display.blit(self.images[1],(0,0))