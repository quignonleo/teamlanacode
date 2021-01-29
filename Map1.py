import pygame as pg
import sys
import numpy as np
from random import choice, randint
from dictionnaires import *
from character2 import *
from character import *


pg.init()
screen = pg.display.set_mode((1000, 700))
screen.fill((0, 0, 0))
clock = pg.time.Clock()


font=pg.font.Font('freesansbold.ttf', 20)

with open('map_finale.txt', 'r') as file:
    list_map = []
    list_interactions = []
    for line in file:
        list_map.append([x for x in line if x != '\n'])
        list_interactions.append([0 for x in line if x != '\n'])
    n = len(list_map)


# On remplit ici la map d'objets, marchands et monstres

liste_endroits_possibles = []
liste_endroits_possibles_monstres = []
for i in range (n):
    for j in range (len(list_map[i])):
        if list_map[i][j] == ".":
            liste_endroits_possibles.append((i,j))
        if list_map[i][j] == "#":
            liste_endroits_possibles_monstres.append((i,j))

#Objet n°1            
pos = choice(liste_endroits_possibles)
liste_endroits_possibles.remove(pos)
list_interactions[pos[0]][pos[1]] = choice(list(dico_equip.keys()))
list_map[pos[0]][pos[1]] = "o"
#Objet n°2
pos = choice(liste_endroits_possibles)
liste_endroits_possibles.remove(pos)
list_interactions[pos[0]][pos[1]] = choice(list(dico_equip.keys()))
list_map[pos[0]][pos[1]] = "o"
#Marchand
pos = choice(liste_endroits_possibles)
liste_endroits_possibles.remove(pos)
list_interactions[pos[0]][pos[1]] = choice(list(dico_marchand.keys()))
list_map[pos[0]][pos[1]] = "µ"
#Monstre
pos = choice(liste_endroits_possibles_monstres)
list_interactions[pos[0]][pos[1]] = choice(list(dico_monstres.keys()))
list_map[pos[0]][pos[1]] = "M"
#Monnaie
pos = choice(liste_endroits_possibles)
list_interactions[pos[0]][pos[1]] = randint(20, 100)
list_map[pos[0]][pos[1]] = "$"



what_it_replaces = '.'
running = True 
while running:
    clock.tick(5)

    for i in range(n):
        for j in range(len(list_map[i])):
            if list_map[i][j] in ['.', '|', '-', '=', '+', '#', '@','o','M','$','µ']:
                text = font.render(list_map[i][j], 1, (255, 165, 0))
                screen.blit(text, (j*20 + 100, i*20 + 150))
            if list_map[i][j] == '@':
                charact_pos = (i, j)
            


     #on part du principe qu'à la bas il n'est pas dans un couloir
    i_0, j_0 = charact_pos
    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.KEYDOWN:

    #on suppose que les éléments sont stockés dans un list nommé "list_map"
            if event.key == pg.K_q and list_map[i_0][j_0-1] not in ['a', '|', '-']:
                list_map[i_0][j_0-1], list_map[i_0][j_0] = list_map[i_0][j_0], list_map[i_0][j_0-1]
                what_it_replaces, list_map[i_0][j_0] = list_map[i_0][j_0], what_it_replaces
            
            if event.key == pg.K_d and list_map[i_0][j_0+1] not in ['a', '|', '-']:
                list_map[i_0][j_0+1], list_map[i_0][j_0] = list_map[i_0][j_0], list_map[i_0][j_0+1]
                what_it_replaces, list_map[i_0][j_0] = list_map[i_0][j_0], what_it_replaces
                #charact_pos = (i_0+1, j_0)

            if event.key == pg.K_s and list_map[i_0+1][j_0] not in ['a', '|', '-']:
                list_map[i_0+1][j_0], list_map[i_0][j_0] = list_map[i_0][j_0], list_map[i_0+1][j_0]
                what_it_replaces, list_map[i_0][j_0] = list_map[i_0][j_0], what_it_replaces
                #charact_pos = (i_0, j_0-1)

            if event.key == pg.K_z and list_map[i_0-1][j_0] not in ['a', '|', '-']:
                list_map[i_0-1][j_0], list_map[i_0][j_0] = list_map[i_0][j_0], list_map[i_0-1][j_0]
                what_it_replaces, list_map[i_0][j_0] = list_map[i_0][j_0], what_it_replaces
                #charact_pos = (i_0, j_0+1)

    
    pg.display.update()
    screen.fill((0, 0, 0))

pg.quit()
