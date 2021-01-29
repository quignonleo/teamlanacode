import numpy as np

import character


Dico_equip = {"Modele":(nature,atk,deff,hp),
"anneau_vie":("anneau",0,0,10),
"épée longue":("épée",10,0,0),
"bouclier en bois":("bouclier",0,10,0),
"casque de mineur":("casque",0,4,0),
"armure de fer":("armure",0,15,0)
}

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

    def __init__(self, atk, deff,nature,nom): 
        self.atk = atk
        self.deff = deff 
        self.nature = nature
        
    
    def apply(self, char):
        char.atk = char.atk + self.atk
        char.deff = char.deff + self.deff
        
    def unapply(self,char): 
        char.atk = char.atk - self.atk
        char.deff = char.deff - self.deff


class monster : 
    def __init__ (self, atk, deff,hp,vitesse) : 
        self.atk = atk
        self.deff = deff
        self.hp = hp
        self.vitesse = vitesse
    
    def hp_modiff(self,vie):
        "la vie peut être négative ici"
        self.hp = self.hp + vie


class pnj : 

    def __init__ (self,inventory,money):
        self.money = money
        self.inventory = inventory
