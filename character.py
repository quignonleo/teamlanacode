import pygame as pg
import numpy as np


class character :

    def __init__(self, hp, inventory, equipment, money):
        self.hp = hp
        self.inventory = inventory
        self.equipment = equipment 
        self.money = money 
        self.attak = 1
        self.defense = 0

