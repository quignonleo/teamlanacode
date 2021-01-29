import pygame as pg
import sys
import numpy as np


pg.init()
screen = pg.display.set_mode((1000, 700))
screen.fill((0, 0, 0))
clock = pg.time.Clock()


font=pg.font.Font('freesansbold.ttf', 20)

with open('map_finale.txt', 'r') as file:
    list_map = []
    for line in file:
        list_map.append([x for x in line if x != '\n'])
    n = len(list_map)

running = True 
while running:
    clock.tick(5)

    for i in range(n):
        for j in range(len(list_map[i])):
            if list_map[i][j] in ['.', '|', '-', '=', '+', '#', '@']:
                text = font.render(list_map[i][j], 1, (255, 165, 0))
                screen.blit(text, (j*20 + 100, i*20 + 150))
            if list_map[i][j] == '@':
                charact_pos = (j, i)
            


    what_it_replaces = '.' #on part du principe qu'à la bas il n'est pas dans un couloir
    charact_pos = i_0, j_0
    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False
        
        if event.type == pg.KEYDOWN:

    #on suppose que les éléments sont stockés dans un list nommé "screen"
            if event.key == pg.K_LEFT and list_map[i_0-1][j_0] not in ['a', '|', '-']:
                list_map[i_0-1][j_0], list_map[i_0][j_0] = list_map[i_0][j_0], list_map[i_0-1][j_0]
                what_it_replaces, list_map[i_0][j_0] = list_map[i_0][j_0], what_it_replaces
            
            if event.key == pg.K_RIGHT and list_map[i_0+1][j_0] not in ['a', '|', '-']:
                list_map[i_0+1][j_0], list_map[i_0][j_0] = list_map[i_0][j_0], list_map[i_0+1][j_0]
                what_it_replaces, list_map[i_0][j_0] = list_map[i_0][j_0], what_it_replaces
                #charact_pos = (i_0+1, j_0)

            if event.key == pg.K_DOWN and list_map[i_0][j_0-1] not in ['a', '|', '-']:
                list_map[i_0][j_0-1], list_map[i_0][j_0] = list_map[i_0][j_0], list_map[i_0][j_0-1]
                what_it_replaces, list_map[i_0][j_0] = list_map[i_0][j_0], what_it_replaces
                #charact_pos = (i_0, j_0-1)

            if event.key == pg.K_UP and list_map[i_0][j_0+1] not in ['a', '|', '-']:
                list_map[i_0][j_0+1], list_map[i_0][j_0] = list_map[i_0][j_0], list_map[i_0][j_0+1]
                what_it_replaces, list_map[i_0][j_0] = list_map[i_0][j_0], what_it_replaces
                #charact_pos = (i_0, j_0+1)
    
    pg.display.update()

pg.quit()
