import pygame
import configurations
from game_play import GameState
from game import PLAY

pygame.init()
pygame.display.set_caption("Something Pokemon Gmae")
game = PLAY(pygame.display.set_mode((configurations.SCREEN_WIDTH, configurations.SCREEN_HEIGHT)))
game.create_system()
clock = pygame.time.Clock()

while game.game_state == GameState.R:
    clock.tick(60)
    game.update_events()
    pygame.display.flip()