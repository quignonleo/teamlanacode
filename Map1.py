import pygame as pg
import sys


pg.init()
screen = pg.display.set_mode((1000, 700))
screen.fill((0, 0, 0))
clock = pg.time.Clock()


font=pg.font.Font('freesansbold.ttf', 20)

running = True 
while running:
    clock.tick(5)

    with open('map_finale.txt', 'r') as f:
        F = f.readlines()
        for i, ligne in enumerate(F):
            ligne.strip
            for j, symbole in enumerate(ligne):
                if symbole in ['.', '|', '-', '=', '+', '#', '@']:
                    text = font.render(symbole, 1, (255, 165, 0))
                    screen.blit(text, (j*20 + 100, i*20 + 150))
                if symbole == '@':
                    charact_position = (j*20 + 100, i*20 + 150)





    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False
        
        keys = pg.keys.get_pressed()
        
        what_it_replaces = '.' #on part du principe qu'à la bas il n'est pas dans un couloir

    #on suppose que les éléments sont stockés dans un array nommé "screen"
        if key[pg.K_LEFT] and screen[i-20, j] not in [' ', '|', '-']:
            screen[i-20, j], screen[i, j] = screen[i, j], screen[i-20, j]
            what_it_replaces, screen[i, j] = screen[i, j], what_it_replaces
            charact_pos = charact_pos.move(-20, 0)
        
        if key[pg.K_RIGHT] and screen[i+20, j] not in [' ', '|', '-']:
            screen[i+20, j], screen[i, j] = screen[i, j], screen[i+20, j]
            what_it_replaces, screen[i, j] = screen[i, j], what_it_replaces
            charact_pos = charact_pos.move(20, 0)

        if key[pg.K_DOWN] and screen[i, j-20] not in [' ', '|', '-']:
            screen[i, j-20], screen[i, j] = screen[i, j], screen[i, j-20]
            what_it_replaces, screen[i, j] = screen[i, j], what_it_replaces
            charact_pos = charact_pos.move(0, -20)

        if key[pg.K_UP] and screen[i, j+20] not in [' ', '|', '-']:
            screen[i, j+20], screen[i, j] = screen[i, j], screen[i, j+20]
            what_it_replaces, screen[i, j] = screen[i, j], what_it_replaces
            charact_pos = charact_pos.move(0, 20)
    
    

    

  

    
    

    pg.display.update()


    
    




pg.quit()