import pygame
from config import *

class Menu:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

    def run(self):
        self.img = pygame.image.load("images/menu.png")
        self.screen.fill(BLACK)
        self.screen.blit(self.img, pygame.Rect(1, 1, 2, 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.mode = 2
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.mode = 2
                elif event.key == pygame.K_SPACE:
                    self.game.startup()
                    self.game.mode = 1