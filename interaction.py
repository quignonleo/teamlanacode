import pygame as pg
import sys
import character2

clock = pg.time.clock()
 ###
perso = character(100, [], [], 100)
 ####
while True:

    clock.tick(5)

    charact_position = (i, j)
    what_it_replaces = '.' #on part du principe qu'à la bas il n'est pas dans un couloir

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit(0)
    
    keys = pg.keys.get_pressed()

#on suppose que les éléments sont stockés dans un array nommé "screen"
    if key[pg.K_LEFT] and screen[i-1, j] not in [' ', '|', '-']:
        screen[i-1, j], screen[i, j] = screen[i, j], screen[i-1, j]
        what_it_replaces, screen[i, j] = screen[i, j], what_it_replaces
        charact_pos = charact_pos.move(-1, 0)
    
    if key[pg.K_RIGHT] and screen[i+1, j] not in [' ', '|', '-']:
        screen[i+1, j], screen[i, j] = screen[i, j], screen[i+1, j]
        what_it_replaces, screen[i, j] = screen[i, j], what_it_replaces
        charact_pos = charact_pos.move(1, 0)

    if key[pg.K_DOWN] and screen[i, j-1] not in [' ', '|', '-']:
        screen[i, j-1], screen[i, j] = screen[i, j], screen[i, j-1]
        what_it_replaces, screen[i, j] = screen[i, j], what_it_replaces
        charact_pos = charact_pos.move(0, -1)

    if key[pg.K_UP] and screen[i, j+1] not in [' ', '|', '-']:
        screen[i, j+1], screen[i, j] = screen[i, j], screen[i, j+1]
        what_it_replaces, screen[i, j] = screen[i, j], what_it_replaces
        charact_pos = charact_pos.move(0, 1)
    

## NOUVELLE PARTIE 
    if screen[charact_pos] == "o" :
        stritem = array_map[charact_pos]
        item = dico_equip[stritem]
        perso.inventory.append(item) 
        print (f"vous avez gagné {print(item)}")
    
    if screen[charact_pos] == "$" :
        perso.money += array_map[charact_pos]
        print (f"vous avez gagné {dico_map[charact_pos]}")

    if screen[charact_pos] == "M" : 
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


    if screen[charact_pos] == "µ" :
        strmarchand = dico_map[charact_pos]
        



    