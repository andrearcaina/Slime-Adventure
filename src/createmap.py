import pygame
from configurations import *
from math import ceil
from support import rng

map_tile_image = {
    #images from image folder
    "G": pygame.transform.scale(pygame.image.load("images/grass.png"), (SCALE,SCALE)),
    "W": pygame.transform.scale(pygame.image.load("images/water.png"), (SCALE,SCALE)),
    "T": pygame.transform.scale(pygame.image.load("images/tree.png"), (SCALE,SCALE)),
    "S": pygame.transform.scale(pygame.image.load("images/statue.png"), (SCALE,SCALE)),
    "P": pygame.transform.scale(pygame.image.load("images/path.png"), (SCALE,SCALE)),
    "B": pygame.transform.scale(pygame.image.load("images/bridge.png"), (SCALE,SCALE)), #bridge
    "H": pygame.transform.scale(pygame.image.load("images/building.png"), (SCALE,SCALE)), #hut/building
    "R": pygame.transform.scale(pygame.image.load("images/road.png"), (SCALE,SCALE)), #hut/building
}

class Map:
    def __init__(self,screen):
        self.screen = screen
        self.array = []
        self.camera = [0,0]

    def load(self, f):
        with open('maps/' + f + ".txt") as m:
            for i in m:
                l = []
                for j in range(0, len(i) - 1, 2):
                    l.append(i[j])
                self.array.append(l)

    def generate(self, screen, player, objects):
        self.camera_movement(player)

        y = 0
        for i in self.array:
            x = 0
            for j in i:
                image = map_tile_image[j]
                rect = pygame.Rect(x * SCALE - (self.camera[0]*SCALE), y * SCALE - (self.camera[1] * SCALE), SCALE, SCALE)
                screen.blit(image, rect)
                x += 1
            y += 1

        for object in objects:
            object.render(self.screen, self.camera) #uses render method() from player to generate/render the player
    
    def camera_movement(self, player):
        #camera movement in the y direction
        MAX_Y = len(self.array) - SCREEN_HEIGHT / SCALE
        Y = player.pos[1] - ceil(round(SCREEN_HEIGHT/ SCALE / 2))

        #camera movement in the x direction
        MAX_X = len(self.array) - SCREEN_WIDTH / SCALE
        X = player.pos[0] - ceil(round(SCREEN_WIDTH/ SCALE / 2))

        if X <= MAX_X and X >= 0:
            self.camera[0] = X
        elif X < 0:
            self.camera[0] = 0
        else:
            self.camera[0] = MAX_X

        if Y <= MAX_Y and Y >= 0:
            self.camera[1] = Y
        elif Y < 0:
            self.camera[1] = 0
        else:
            self.camera[1] = MAX_Y