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
 