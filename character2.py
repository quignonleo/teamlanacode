import numpy as np

import character

class Potion : 

    def __init__ (self,hp,atk,deff) : 
        self.bonus_hp = hp 
        self.bonus_atk = atk
        self.bonus_def = deff
    
    def apply(self, char) :
        char.hp = char.hp + self.bonus_hp
        char.atk = char.atk + self.bonus_atk
        char.deff = char.deff + self.bonus_deff

class equipment : 

    def __init__(self, atk, deff,nature): 
        self.atk = atk
        self.deff = deff 
        self.nature = nature
    
    def apply(self, char):
        char.atk = char.atk + self.atk
        char.deff = char.deff + self.deff
        
    def unapply(self,char): 
        char.atk = char.atk - self.atk
        char.deff = char.deff - self.deff


