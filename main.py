import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame as pg
import sys

from personal.text import Text
from campo import Panel, Field

pg.init()

ease = int(input("1)Easy mode\n2)Difficult mode\n>"))

screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Flood it!')

panel = Panel()
field = Field(ease)

clock = pg.time.Clock()
done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
            break

        panel.update(event)
        if panel.click:
            if field.update() == 'vittoria':
                panel.restart()
                field.restart()
        
    screen.fill((0, 0, 0))

    panel.render(screen)
    field.render(screen)
    
    Text(f'{panel.moves}', size=30).render(screen, False, 50, 200)
    Text(f'{field.points}', size=30).render(screen, False, 50, 230)
    
    pg.display.update()
    clock.tick(30)

pg.quit()
sys.exit()

