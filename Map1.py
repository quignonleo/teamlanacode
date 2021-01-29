import pygame as pg
import sys
import numpy as np
from random import choice, randint
import os
from dictionnaires import *
from character2 import *
from character import *


pg.init()
screen = pg.display.set_mode((1000, 700))
screen.fill((0, 0, 0))
clock = pg.time.Clock()

perso = character(100, [], {}, 100)
perso.name = "Ralf le Rouge"

font = pg.font.Font('freesansbold.ttf', 20)
levels = os.listdir("levels")
running = True 

while running:
    clock.tick(10)
    nb_level = 0
    while levels != [] and running:
        nb_level += 1
        what_it_replaces = '.'

        with open("levels/" + levels[0], 'r') as file:
            list_map = []
            list_interactions = []
            for line in file:
                list_map.append([x for x in line if x != '\n'])
                list_interactions.append([0 for x in line if x != '\n'])
            n = len(list_map)
        levels = levels[1:]

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

        while what_it_replaces != '=' and running:
            text = font.render(f'LEVEL {nb_level}', 1, (255, 165, 0))
            screen.blit(text, (20, 20))
            for i in range(n):
                for j in range(len(list_map[i])):
                    if list_map[i][j] in ['.', '|', '-', '=', '+', '#', '@','o','M','$','µ']:
                        text = font.render(list_map[i][j], 1, (255, 165, 0))
                        screen.blit(text, (j*15 + 100, i*15 + 150))
                    if list_map[i][j] == '@':
                        charact_pos = (i, j)
            
            vie = font.render(f'HP = {perso.hp}', 1, (255, 255, 255))
            screen.blit(vie, (10, 580))
            attaque = font.render(f'attaque = {perso.atk}', 1, (255, 255, 255))
            screen.blit(attaque, (10, 600))
            defense = font.render(f'défense = {perso.deff}', 1, (255, 255, 255))
            screen.blit(defense, (10, 620))
            equipement = font.render(f'équipement = {perso.equipment}', 1, (255, 255, 255))
            screen.blit(equipement, (10, 640))
            monaie = font.render(f'{perso.name} possède {perso.money} $', 1, (255, 255, 255))
            screen.blit(monaie, (10, 660))

            pg.display.update()
            screen.fill((0, 0, 0))
            #on part du principe qu'à la base il n'est pas dans un couloir
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
            
            if list_map[i_0][j_0] == "o" :
                stritem = list_interactions[i_0][j_0]
                item = dico_equip[stritem]
                perso.inventory.append(item) 
                pg.display.update()
                txt = font.render(str(item), False, (255, 255, 255))
                screen.blit(txt,(500,500))
                pg.display.update()
                print (f"vous avez gagné {print(item)}")
                list_map[i_0][j_0] = "."
                list_interactions[i_0][j_0] = 0


            if list_map[i_0][j_0] == "$" :
                perso.money += list_interactions[i_0][j_0]
                list_map[i_0][j_0] = "."
                list_interactions[i_0][j_0] = 0
                text = font.render(f"vous avez gagné{list_interactions[i_0][j_0]}", 1, (255, 255, 255))
                screen.blit(text, (500,500))
                pg.display.update()
                print(f"vous avez gagné {list_interactions[i_0][j_0]}")

            if list_map[i_0][j_0] == "M" : 
                strmonstre = list_interactions[i_0][j_0]
                monstre = dico_monstres[strmonstre]
                combat = fight(perso,monstre)
                while combat.check():
                    combat.turn()
                list_map[i_0][j_0] = "."
                list_interactions[i_0][j_0] = 0
                if perso.hp > 0 :
                    perso.grab_money(20)  # gagne de l'argent lorsqu'il tue un monstre
                    txt = font.render("vous avez gagné, voici 20$ en récompense", False, (255, 255, 255))
                    screen.blit(txt,(500,500))
                    pg.display.update()
                    print ("vous avez gagné, voici 20$ en récompense")
                else : 
                    print ("vous etes mort") # Il faut stop le programme
                

            if list_map[i_0][j_0] == "µ" :
                strmarchand = list_interactions[i_0][j_0]
                marchand = dico_marchand[strmarchand]
                #marchand.open_inventory()

                #item = #selection de l'item

                running2 = True
                while running2 : 
                    clock.tick(5)
                    for event in pg.event.get() :
                        if event.type == pg.QUIT:
                                running2 = False
                        if event.type == pg.KEYDOWN : 
                            if event.key == pg.K_y :
                                text = font.render(str (marchand.inventory), 1, (255, 255, 255))
                                screen.blit(text, (500,500))
                                pg.display.update()
                                screen.fill((0, 0, 0))
                            if event.key == pg.K_p :
                                running2 = False
                pg.display.update()
                screen.fill((0, 0, 0))


        #echange(perso,marchand,item)

        #print(f"vous avez acheté l'objet {print(item)}")


                pg.display.update()
                screen.fill((0, 0, 0))
                
    
    #screen.fill((0, 0, 0))
    if levels == []:
        text = font.render('CONGRATULATIONS, YOU WON !', 1, (255, 165, 0))
        screen.blit(text, (320, 300))
    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False
    
    pg.display.update()        


pg.quit()
