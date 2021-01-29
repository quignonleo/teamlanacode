import pygame as pg
import numpy as np
from character2 import * 

class character :

    def __init__(self, hp, inventory, equipment, money):
        self.hp = hp
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
            nature = item.nature
            if self.equipment[nature] == []:
                self.equipment[nature] = item
                item.apply(self)
            else :
                item_porté = equipment[nature]
                item_porté.unapply(self)
                self.equipment[nature] = item
                item.apply(self)
            
    def drink(self, potion):
        potion.apply(self)
        self.inventory.remove(potion)

    def grab_money(self, new_money):
        self.money += new_money

    def echange(self, pnj, montant, item):
        self.money -= montant
        pnj.money += montant
        self.inventory.append(item)
        pnj.inventory.remove(item)


class fight :

    def __init__(self, character, monster):
        self.character = character
        self.monster = monster

    def turn(self):
        if self.character.quickness >= self.monster.quickness :
            self.monster.hp -= int(self.character.atk*(100 - self.monster.deff)/100)
            if self.monster.hp > 0 :
                self.character.hp -= int((self.monster.atk*(100 - self.character.deff)/100)**0.5)
        else :
             self.character.hp -= int((self.monster.atk*(100 - self.character.deff)/100)**0.5)
             if self.character.hp > 0 :
                 self.monster.hp -= int(self.character.atk*(100 - self.monster.deff)/100)

    def check(self):
        return self.monster.hp > 0 and self.character.hp > 0  

        