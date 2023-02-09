import pygame
from configurations import *
from support import rng

class Battle:
    def __init__(self, screen, pokemon, player):
        self.screen = screen
        self.pokemon = pokemon
        self.player = player

    def render(self):
        self.screen.fill(WHITE)
        rect = pygame.Rect(1, 1, 2, 2)
        self.screen.blit(self.pokemon.image, rect)
        self.screen.blit(self.player.image, (320, 40))

        font = pygame.font.SysFont(None, 24)
        img = font.render("HP: " + str(self.pokemon.hp) + " ATK: " + str(self.pokemon.atk), True, BLACK)
        self.screen.blit(img, (20, 120))

        img = font.render("press c to attack!", True, BLACK)
        self.screen.blit(img, (20, 220))
        
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.mode = 2
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game.mode = 2
                if event.key == pygame.K_c:
                    self.pokemon.hp -= 1