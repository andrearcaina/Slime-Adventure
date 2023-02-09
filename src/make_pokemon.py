from support import * 
from pokemon import Pokemon

class Creation:
    def __init__(self):
        self.count = 0

    def create(self,type):
        n = -1

        if type == "G":
            n = rng(1,5)
        
        pokemon = Pokemon(type,n)
        self.count += 1
        return pokemon