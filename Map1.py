import pygame as pg


pg.init()
screen = pg.display.set_mode((1000, 700))
screen.fill((0, 0, 0))
clock = pg.time.Clock()


font=pg.font.Font('freesansbold.ttf', 20)

running = True 
while running:
    with open('map_finale.txt', 'r') as f:
        F = f.readlines()
        for i, ligne in enumerate(F):
            ligne.strip

            for j, symbole in enumerate(ligne):
                if symbole in ['.', '|', '-', '=', '+', '#']:
                    text = font.render(symbole, 1, (255, 165, 0))

                    screen.blit(text, (j*20 + 100, i*20 + 150))




    for event in pg.event.get():

        if event.type == pg.QUIT:
            running = False

    pg.display.update()





pg.quit()