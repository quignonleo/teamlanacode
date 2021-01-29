import numpy as np

import character




class Potion: 

    def __init__ (self,hp,atk,deff) : 
        self.bonus_hp = hp 
        self.bonus_atk = atk
        self.bonus_def = deff
    
    def apply(self, char) :
        char.hp = char.hp + self.bonus_hp
        char.atk = char.atk + self.bonus_atk
        char.deff = char.deff + self.bonus_deff
    def __repr__(self) :
        return(f"bonus HP : {self.bonus_hp}, bonus atk : {self.bonus_atk}, bonus deff : {self.bonus_deff}")

class equipment: 

    def __init__(self, nature, atk, deff, hp): 
        self.atk = atk
        self.deff = deff 
        self.nature = nature
        self.hp = hp

    def __repr__(self):
        return f"nature : {self.nature}, attaque : {self.atk}, défense : {self.deff}"        
    
    def apply(self, char):
        char.atk = char.atk + self.atk
        char.deff = char.deff + self.deff
        
    def unapply(self,char): 
        char.atk = char.atk - self.atk
        char.deff = char.deff - self.deff


class monster: 
    def __init__ (self, atk, deff,hp,quickness) : 
        self.atk = atk
        self.deff = deff
        self.hp = hp
        self.quickness = quickness
    
    def hp_modiff(self,vie):
        "la vie peut être négative ici"
        self.hp = self.hp + vie


class pnj: 

    def __init__ (self,inventory,money):
        self.money = money
        self.inventory = inventory
    
    def open_invetory(self) :
        textsurface = myfont.render('Some Text', False, (0, 0, 0)) 
        screen.blit(textsurface,(0,0))


dico_equip = {
"anneau_vie": equipment("anneau", 0, 0, 10),
"épée longue":equipment("arme",10,0,0),
"bouclier en bois":equipment("bouclier",0,10,0),
"casque de mineur":equipment("casque",0,4,0),
"armure de fer":equipment("armure",0,15,0),
"pistolet laser":equipment("arme", 20, 0, 0),
"maillot de Lens":equipment("armure",1, 10, 35),
"bob coloré":equipment("casque", 0, 14, 0),
"porte de la meuh":equipment("bouclier", 10, 20, 0),
"épée porteuse du tétanos":equipment("arme", 40, 0, -10),
"foudre de Zeus":equipment("arme", 30, 0, 0),
"grosse chevalière":equipment("anneau", 10, 0, 8),
"perruque coupe mulet":equipment("casque", 5, 10, 5),
"vaccin contre le COVID" : equipment("arme", 50, 50, -50)
}
