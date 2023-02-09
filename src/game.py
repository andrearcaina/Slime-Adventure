import pygame
from support import rng
from configurations import *

from player import Player
from make_pokemon import Creation
from createmap import Map
from battle import Battle

# when self.mode = 0,1,2 {menu,game,quit}
# when self.view = 0,1 {map,battle}

class Play:
    def __init__(self, screen):
        #constructor variables
        self.screen = screen
        self.objects = []
        self.mode = 0
        self.view = 0 #view map = 0
        self.moved = False
        self.creation = Creation()
        self.map = Map(screen)
        self.battle = None

    def startup(self):
        #create player, append to object list (for player and others), load map
        player = Player(1, 1)
        self.player = player
        self.objects.append(player)
        self.mode = 1
        self.map.load("m1")

    def run(self):
        if self.view == 0:
            self.moved = False
            self.screen.fill(BLACK)
            self.key_events()
            self.map.generate(self.screen,self.player,self.objects)
            
            if self.moved:
                print("player has moved")
                self.findpokemon()

        elif self.view == 1: #view = 1 is battle pokeomn
            self.battle.update()
            self.battle.render()

            if self.battle.pokemon.hp <= 0:
                self.view = 0

    def findpokemon(self):
        print("method has run")
        tile = self.map.map_arr[self.player.pos[1]][self.player.pos[0]]
        print(tile)
        
        if tile == "R":
            return

        self.found(tile)

    def found(self, tile):
        numb = rng(1,10)

        if numb <= 2:
            founded = self.creation.create(tile)
            print("you found a monster!")
            print("Monster Type: " + founded.type)
            print("Attack: " + str(founded.atk))
            print("Health: " + str(founded.hp))

            self.battle = Battle(self.screen, founded, self.player)
            self.view = 1

    def key_events(self):
        for event in pygame.event.get():
            #quit using escape button
            if event.type == pygame.QUIT:
                self.mode = 2
            #movement keys
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.mode = 2
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

        if new[0] < 0 or new[0] > (len(self.map.map_arr[0]) - 1):
            return

        if new[1] < 0 or new[1] > (len(self.map.map_arr) - 1):
            return

        #collision detection
        if self.map.map_arr[new[1]][new[0]] == "W":
            print("URHITING WATER")
            return
        
        if self.map.map_arr[new[1]][new[0]] == "T":
            print("URHITING TrEEE")
            return
        
        if self.map.map_arr[new[1]][new[0]] == "H":
            print("URHITING HUTOUSE")
            return

        character.movement(new)