import pygame as pg
import sys
import numpy as np
from character2 import *
from character import *

pg.init()
screen = pg.display.set_mode((1000, 700))
screen.fill((0, 0, 0))
clock = pg.time.Clock()

perso = character(100,[],[],100)

font=pg.font.Font('freesansbold.ttf', 20)

with open('map_finale.txt', 'r') as file:
    list_map = []
    for line in file:
        list_map.append([x for x in line if x != '\n'])
    n = len(list_map)


what_it_replaces = '.'
running = True 
while running:
    clock.tick(5)

    for i in range(n):
        for j in range(len(list_map[i])):
            if list_map[i][j] in ['.', '|', '-', '=', '+', '#', '@']:
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

    #on suppose que les éléments sont stockés dans un list nommé "screen"
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


## NOUVELLE PARTIE 

    if list_map[charact_pos[0]][charact_pos[1]] == "o" :
        stritem = array_map[charact_pos]
        item = dico_equip[stritem]
        perso.inventory.append(item) 
        print (f"vous avez gagné {print(item)}")
    
    if list_map[charact_pos[0]][charact_pos[1]] == "$" :
        perso.money += array_map[charact_pos]
        print (f"vous avez gagné {dico_map[charact_pos]}")

    if list_map[charact_pos[0]][charact_pos[1]] == "M" : 
        strmonstre = array_map[charact_pos]
        monstre = dico_monstre[strmonstre]
        combat = fight(perso,monstre)
        while combat.check():
            combat.turn()
        if perso.hp > 0 :
            self.character.money += 20  # gagne de l'argent lorsqu'il tue un monstre
            print ("vous avez gagné, voici 20$ en récompense")
        else : 
            print ("vous etes mort") # Il faut stop le programme 


    if list_map[charact_pos[0]][charact_pos[1]] == "#" :
        strmarchand = dico_map[charact_pos]
        marchand = dico_marchand[strmarchand]
        #marchand.open_inventory()

        #item = #selection de l'item

        running = True
        while running : 
            clock.tick(5)
            for event2 in pg.event.get() :
                if event.key == pq.K_p :
                    running = False
                if event.key == pq.K_Y :
                    text = font.render("test", 1, (255, 255, 255))
                    screen.blit(text, charact_pos)

        echange(perso,marchand,item)

        print(f"vous avez acheté l'objet {print(item)}")

    pg.display.update()
    screen.fill((0, 0, 0))

pg.quit()



    