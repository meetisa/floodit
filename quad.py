import pygame as pg
from random import choice
from itertools import cycle

class Quad:
    def __init__(self, size, coords):
        """Size here is (w, h) in pixel"""
        self.surf = pg.Surface(size)
        self.rect = pg.Rect(coords, size)
        self.flooded = False

    def set_color(self, color):
        self.color = color
        self.surf.fill(self.color)

    def values(self):
        return [self.surf, self.rect, self.color]

    def render(self, screen):
        screen.blit(self.surf, self.rect)


class Quads:
    def __init__(self, size, offset, qs):
        """Size here is (rows, cols), while qs is the size of every quad"""
        self.rows, self.cols = range(size[0]), range(size[1])
        coords = lambda x, y: (offset[0] + x*qs, offset[1] + y*qs)
        self.grid = [[Quad((qs, qs), coords(x,y)) for y in self.cols]
                        for x in self.rows]

        self.colors = [
            (66, 135, 245), #Celeste
            (69, 247, 105), #Verde
            (227, 158, 68), #Arancione
            (250, 77, 224), #Fucsia
            (255, 181, 181), #Rosa
            (172, 250, 218) #Azzurro verde
        ]

    def set_pattern(self, randomize=False, *color):
        """The last variable is for set all the grid of the same color"""
        colors = cycle(self.colors)
        for row in self.rows:
            for col in self.cols:
                if color:
                    self.grid[row][col].set_color(color)
                elif randomize:
                    self.grid[row][col].set_color(choice(self.colors))
                else:
                    self.grid[row][col].set_color(next(colors))

    def render(self, screen):
        for row in self.rows:
            for col in self.cols:
                try:
                    self.grid[row][col].render(screen)
                except IndexError:
                    continue
