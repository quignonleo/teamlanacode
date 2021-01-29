import pygame as pg
import numpy as np
from character2 import * 
import random





class character :

    def __init__(self, hp, inventory, equipment, money):
        self.hp = hp
        self.food = 100
        self.water = 100
        self.inventory = inventory
        self.equipment = equipment 
        self.money = money 
        self.atk = 10
        self.deff = 0
        self.quickness = 5
        self.name = ''

    def name(self, name):
        self.name = name
    
    def equip(self, item):
        if item not in self.inventory :
            return "Vous ne possédez pas cet item"
        else : 
            item_réel = dico_equip[item]
            nature = item_réel.nature
            if self.equipment[nature] == '':
                self.equipment[nature] = item
                item_réel.apply(self)
                self.inventory.remove(item)
            else :
                item_porté = equipment[nature]
                item_porté_réel = dico_equip[item_porté]
                item_porté_réel.unapply(self)
                self.equipment[nature] = item
                item_réel.apply(self)
                self.inventory.remove(item)
                self.inventory.append(item_porté)
            
    def drink(self, potion):
        potion.apply(self)
        self.inventory.remove(potion)

    def grab_money(self, new_money):
        self.money += new_money

    def echange(self, pnj, montant, item):
        if self.money >= montant :
            self.money -= montant
            pnj.money += montant
            self.inventory.append(item)
            pnj.inventory.remove(item)
        else : 
            print("pas assez d'argent") # a faire apparaitre à l'écran


class fight :

    def __init__(self, character, monster):
        self.character = character
        self.monster = monster

    def turn(self):
        r = random.random()
        if r<=0.95 :

            if self.character.quickness >= self.monster.quickness :
                self.monster.hp -= int(self.character.atk*(100 - self.monster.deff)/100)
                if self.monster.hp > 0 :
                    self.character.hp -= int((self.monster.atk*(100 - self.character.deff)/100)**0.5)
            else :
                self.character.hp -= int((self.monster.atk*(100 - self.character.deff)/100)**0.5)
                if self.character.hp > 0 :
                    self.monster.hp -= int(self.character.atk*(100 - self.monster.deff)/100)
        else : 
            print("coup raté") # a afficher à l'écran

    def check(self):
        
        return self.monster.hp > 0 and self.character.hp > 0  


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
        char.hp = char.hp + self.hp
        
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

 
