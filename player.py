import pygame
from configurations import *

class Player:
    def __init__(self, X, Y):
        self.pos = [X, Y]
        self.img = pygame.transform.scale(pygame.image.load("images/player_sprite.png"), (SCALE, SCALE))
        self.rect = pygame.Rect(self.pos[0] * SCALE, self.pos[1] * SCALE, SCALE, SCALE)

    def movement(self, new_pos):
        self.pos[0] = new_pos[0]
        self.pos[1] = new_pos[1]

    def render(self, screen, camera):
        self.rect = pygame.Rect(self.pos[0] * SCALE - (camera[0]*SCALE), self.pos[1] * SCALE - (camera[1] * SCALE), SCALE, SCALE)
        screen.blit(self.img, self.rect)