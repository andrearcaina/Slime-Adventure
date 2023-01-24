import pygame
import configurations

class Player:
    def __init__(self, X, Y):
        self.pos = [X, Y]
        self.img = pygame.transform.scale(pygame.image.load("images/player_sprite.png"), (configurations.SCALE, configurations.SCALE))
        self.rect = pygame.Rect(self.pos[0] * configurations.SCALE, self.pos[1] * configurations.SCALE, configurations.SCALE, configurations.SCALE)

    def movement(self, new_pos):
        self.pos[0] = new_pos[0]
        self.pos[1] = new_pos[1]

    def render(self, screen, camera):
        self.rect = pygame.Rect(self.pos[0] * configurations.SCALE - (camera[0]*configurations.SCALE), self.pos[1] * configurations.SCALE - (camera[1] * configurations.SCALE), configurations.SCALE, configurations.SCALE)
        screen.blit(self.img, self.rect)