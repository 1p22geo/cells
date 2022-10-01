# *********************
# The main game file
# v 0.2
# **********************

import pygame
import game as gamefile
import graphics as graphicsfile
import constants as const

pygame.init()

graphics = graphicsfile.Graphics()
clock = pygame.time.Clock()
game = gamefile.Game(graphics.TILE_SIZE, graphics.display)

while game.running:
    clock.tick(const.MAX_FPS)
    game.check_events()
    graphics.check_clicks(game)
    # game.check_cutscenes() # cutscenes will be added later - probably 1.0
    if not game.gamepause:
        game.run_game_loop()
    graphics.update_screen(game)
    pygame.display.flip()

pygame.quit()
