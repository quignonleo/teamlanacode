
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

    HP=300
    attaque=1
    defense=5
    equipement=['f', 'g']

            

    vie = font.render(f'HP = {HP}', 1, (255, 255, 255))
    screen.blit(vie, (10, 580))
    attaque = font.render(f'attaque = {attaque}', 1, (255, 255, 255))
    screen.blit(attaque, (10, 600))
    defense = font.render(f'défense = {defense}', 1, (255, 255, 255))
    screen.blit(defense, (10, 620))
    equipement = font.render(f'équipement = {equipement}', 1, (255, 255, 255))
    screen.blit(equipement, (10, 640))

    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False
    pg.display.update()

pg.quit()