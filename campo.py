import pygame as pg
import random as rn

from personal.text import Text

class Campo:
    def __init__(self):
        self.colors = [
            (66, 135, 245), #Celeste
            (69, 247, 105), #Verde
            (227, 158, 68), #Arancione
            (250, 77, 224), #Fucsia
            (255, 181, 181), #Rosa
            (172, 250, 218) #Azzurro verde
        ]

        self.moves = 0

        self.panel = self.grid((3, 2), (30, 25))
        for i, q in enumerate(self.panel):
            q[0].fill(self.colors[i])
            q.append(self.colors[i])

        self.field = self.grid((11, 11), (210, 25))
        for q in self.field:
            color = rn.choice(self.colors)
            q[0].fill(color)
            q.append(color)

        self.flooded = [self.field[0]]
        self.field.pop(0)

    def grid(self, size, offset):
        return [[pg.Surface((50, 50)), pg.Rect((offset[0] + x*50, offset[1] + y*50, 50, 50))]
                     for y in range(size[1]) for x in range(size[0])]

    def across(self, rect):
        coords = [(-50, 0), (0, -50), (0, 50), (50, 0)]
        val = [pg.Rect((rect.x + x, rect.y + y, 50, 50)) for x, y in coords]
        return [i for i, q in enumerate(self.field) for v in val if v in q]

    def restart(self):
        self.moves = 0
        self.field = self.grid((11, 11), (210, 25))
        for q in self.field:
            color = rn.choice(self.colors)
            q[0].fill(color)
            q.append(color)

        self.flooded = [self.field[0]]
        self.field.pop(0)
        
    def update(self, event):
        for surf, rect, color in self.panel:
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rect.collidepoint(pg.mouse.get_pos()):
                        self.moves += 1
                        for s, r, c in self.flooded:
                            for quad in self.across(r):
                                if self.field[quad][2] == color:
                                    self.flooded.append(self.field[quad])
                                    self.field.pop(quad)
                            s.fill(color)
                        
    def render(self, screen):
        for surf, rect, color in self.panel:
            screen.blit(surf, rect)

        for surf, rect, color in self.field:
            screen.blit(surf, rect)

        for surf, rect, color in self.flooded:
            screen.blit(surf, rect)

        Text(f'{self.moves}', size=30).render(screen, False, 50, 200)
