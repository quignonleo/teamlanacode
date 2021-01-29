import pygame as pg
import sys

clock = pg.time.clock()

while True:

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
    

