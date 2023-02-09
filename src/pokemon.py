import pygame

class Pokemon:
    def __init__(self,type,id):
        print("pokemon created")
        self.type = type
        self.hp = 10
        self.atk = 10
        self.count = 0
        self.id = id
        self.img = pygame.image.load("images/pokemon/" + f"{self.id:03d}" + ".png")