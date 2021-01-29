import pygame as pg
import sys
import numpy as np
import os
from random import choice
from dictionnaires import *
from character2 import *
from character import *


pg.init()
screen = pg.display.set_mode((1000, 700))
screen.fill((0, 0, 0))
clock = pg.time.Clock()


font=pg.font.Font('freesansbold.ttf', 20)
levels = os.listdir("teamlanacode\levels")
running = True


while running:
    clock.tick(15)
    nb_level = 0
    while levels != []:
        nb_level += 1
        what_it_replaces = '.'
        
        with open("teamlanacode/levels/" + levels[0], 'r') as file:
            list_map = []
            list_interactions = []
            for line in file:
                list_map.append([x for x in line if x != '\n'])
                list_interactions.append([0 for x in line if x != '\n'])
            n = len(list_map)
        levels = levels[1:]

        """liste_endroits_possibles = []
        liste_endroits_possibles_monstres = []
        for i in range (n):
            for j in range (len(list_map[i])):
                if list_map[i][j] == ".":
                    liste_endroits_possibles.append((i,j))
                if list_map[i][j] == "#":
                    liste_endroits_possibles_monstres.append((i,j))
        pos = choice(liste_endroits_possibles)
        list_interactions[pos[0]][pos[1]] = choice(list(dico_equip.keys()))
        list_map[pos[0]][pos[1]] = "o"
        print(pos)
        pos = choice(liste_endroits_possibles)
        print(pos)
        list_interactions[pos[0]][pos[1]] = choice(list(dico_equip.keys()))
        list_map[pos[0]][pos[1]] = "o"
        pos = choice(liste_endroits_possibles_monstres)
        list_interactions[pos[0]][pos[1]] = choice(list(dico_monstres.keys()))
        list_map[pos[0]][pos[1]] = "M" """

        while what_it_replaces != '=':

            text = font.render(f'LEVEL {nb_level}', 1, (255, 165, 0))
            screen.blit(text, (20, 20))
            for i in range(n):
                for j in range(len(list_map[i])):
                    if list_map[i][j] in ['.', '|', '-', '=', '+', '#', '@','o','M','$','µ']:
                        text = font.render(list_map[i][j], 1, (255, 165, 0))
                        screen.blit(text, (j*15 + 100, i*15 + 150))
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

                """if list_map[i_0][j_0] == "o" :
                    stritem = array_map[i_0][j_0]
                    item = dico_equip[stritem]
                    perso.inventory.append(item) 
                    print (f"vous avez gagné {print(item)}")
            
                if list_map[i_0][j_0] == "$" :
                    perso.money += array_map[i_0][j_0]
                    print (f"vous avez gagné {list_interactions[i_0][j_0]}")

                if list_map[i_0][j_0] == "M" : 
                    strmonstre = array_map[i_0][j_0]
                    monstre = dico_monstre[strmonstre]
                    combat = fight(perso,monstre)
                    while combat.check():
                        combat.turn()
                    if perso.hp > 0 :
                        self.character.money += 20  # gagne de l'argent lorsqu'il tue un monstre
                        print ("vous avez gagné, voici 20$ en récompense")
                    else : 
                        print ("vous etes mort") # Il faut stop le programme 


                if list_map[i_0][j_0] == "µ" :
                    strmarchand = list_interactions[i_0][j_0]"""
            
            pg.display.update()
            screen.fill((0, 0, 0))
    
    screen.fill((0, 0, 0))
    text = font.render('CONGRATULATIONS, YOU WON !', 1, (255, 165, 0))
    screen.blit(text, (320, 300))

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False
    
    pg.display.update()

pg.quit()