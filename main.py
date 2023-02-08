import pygame
from configurations import *
from game import Play
from menu import Menu

pygame.init()
pygame.display.set_caption("Something Pokemon Gmae")
game = Play(pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)))
menu = Menu(pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)), game)
clock = pygame.time.Clock()

# 0 = menu
# 1 = game
# 2 = quit

while game.mode != 2: 
    clock.tick(60)
    
    if game.mode == 0:
        menu.run()

    if game.mode == 1:
        game.run()

    pygame.display.flip()