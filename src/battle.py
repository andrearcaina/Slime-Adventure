import pygame
from config import *

class Battle:
    def __init__(self, screen, pokemon, player):
        self.screen = screen
        self.pokemon = pokemon
        self.player = player

    def render(self):
        self.screen.fill(WHITE)
        rect = pygame.Rect(320, 20, 2, 2)
        self.screen.blit(self.pokemon.img, rect)
        self.screen.blit(self.player.img, (20, 320))

        font = pygame.font.SysFont(None, 24)
        img = font.render("HP: " + str(self.pokemon.hp) + " ATK: " + str(self.pokemon.atk), True, BLACK)
        self.screen.blit(img, (20, 120))

        img = font.render("press space to attack!", True, BLACK)
        self.screen.blit(img, (20, 220))
        
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("dont even try quitting the game")
            #     handle key events
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.pokemon.hp -= 1