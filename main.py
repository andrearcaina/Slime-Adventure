import pygame
from configurations import *
from game import PLAY

pygame.init()
pygame.display.set_caption("Something Pokemon Gmae")
game = PLAY(pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)))
game.create_system()
clock = pygame.time.Clock()

while game.game_state == 1:
    clock.tick(60)
    game.update_events()
    pygame.display.flip()