import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame as pg
import sys

import campo

pg.init()

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Flood it!')

c = campo.Campo()

clock = pg.time.Clock()
done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
            break

        c.update(event)
        
    screen.fill((0, 0, 0))

    c.render(screen)
    pg.display.update()
    clock.tick(30)

pg.quit()
sys.exit()

