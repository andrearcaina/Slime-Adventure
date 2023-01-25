import math
import pygame
from configurations import *
from player import Player

map_tile_image = {
    #images from image folder
    "G": pygame.transform.scale(pygame.image.load("images/grass.png"), (SCALE,SCALE)),
    "W": pygame.transform.scale(pygame.image.load("images/water.png"), (SCALE,SCALE)),
    "T": pygame.transform.scale(pygame.image.load("images/tree.png"), (SCALE,SCALE)),
    "S": pygame.transform.scale(pygame.image.load("images/statue.png"), (SCALE,SCALE)),
    "P": pygame.transform.scale(pygame.image.load("images/path.png"), (SCALE,SCALE)),
    "B": pygame.transform.scale(pygame.image.load("images/bridge.png"), (SCALE,SCALE)), #bridge
    "H": pygame.transform.scale(pygame.image.load("images/building.png"), (SCALE,SCALE)), #hut/building
}

class PLAY:
    def __init__(self, screen):
        #constructor variables
        self.screen = screen
        self.objects = []
        self.game_state = 0
        self.map = []
        self.camera = [0, 0]

    def create_system(self):
        #create player, append to object list (for player and others), load map
        player = Player(1, 1)
        self.player = player
        self.objects.append(player)
        self.game_state = 1
        self.load("m1")

    def update_events(self):
        self.screen.fill(BLACK)
        self.key_events()
        self.generate(self.screen)
        for object in self.objects:
            object.render(self.screen, self.camera)

    def key_events(self):
        for event in pygame.event.get():
            #quit using escape button
            if event.type == pygame.QUIT:
                self.game_state = 2
            #movement keys
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = 2
                elif event.key == pygame.K_w: # up
                    self.move(self.player, [0, -1])
                elif event.key == pygame.K_s: # down
                    self.move(self.player, [0, 1])
                elif event.key == pygame.K_a: # left
                    self.move(self.player, [-1, 0])
                elif event.key == pygame.K_d: # right
                    self.move(self.player, [1, 0])

    def move(self, character, change):
        new = [character.pos[0] + change[0], character.pos[1] + change[1]]

        if new[0] < 0 or new[0] > (len(self.map[0]) - 1):
            return

        if new[1] < 0 or new[1] > (len(self.map) - 1):
            return

        #collision detection
        if self.map[new[1]][new[0]] == "W":
            print("URHITING WATER")
            return
        
        if self.map[new[1]][new[0]] == "T":
            print("URHITING TrEEE")
            return
        
        if self.map[new[1]][new[0]] == "H":
            print("URHITING HUTOUSE")
            return

        character.movement(new)

    def camera_movement(self):
        MAX_Y = len(self.map) - SCREEN_HEIGHT / SCALE
        Y = self.player.pos[1] - math.ceil(round(SCREEN_HEIGHT/ SCALE / 2))

        MAX_X = len(self.map) - SCREEN_WIDTH / SCALE
        X = self.player.pos[0] - math.ceil(round(SCREEN_WIDTH/ SCALE / 2))

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

    def load(self, f):
        with open('maps/' + f + ".txt") as m:
            for i in m:
                l = []
                for j in range(0, len(i) - 1, 2):
                    l.append(i[j])
                self.map.append(l)

    def generate(self, screen):
        self.camera_movement()

        y = 0
        for i in self.map:
            x = 0
            for j in i:
                image = map_tile_image[j]
                rect = pygame.Rect(x * SCALE - (self.camera[0]*SCALE), y * SCALE - (self.camera[1] * SCALE), SCALE, SCALE)
                screen.blit(image, rect)
                x += 1
            y += 1