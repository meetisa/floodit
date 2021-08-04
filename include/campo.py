import pygame as pg

from personal.text import Text
from quad import Quads

class Panel(Quads):
    def __init__(self, *file):
        if file:
            super().__init__((3, 2), (30, 25), 50, file)
        else:
            super().__init__((3, 2), (30, 25), 50)
        self.moves = 0
        self.set_pattern()
        self.click = False

    def update(self, event):
        for row in self.rows:
            for col in self.cols:
                surf, rect, color = self.grid[row][col].values()
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    if rect.collidepoint(pg.mouse.get_pos()):
                        self.moves += 1
                        Quads.color = color
                        self.click = True
                else:
                    self.click = False
                    
    def restart(self):
        self.moves = 0


class Field(Quads):
    def __init__(self, ease, *file):
        """ease set the difficulty of the game, maintaining the same
        size for both mode
        """
        if file:
            super().__init__((11 * ease, 11 * ease), (210, 25), 50 / ease, file)
        else:
            super().__init__((11 * ease, 11 * ease), (210, 25), 50 / ease)
        self.set_pattern(randomize=True)
        Quads.color = self.grid[0][0].color
        self.grid[0][0].flooded = True
        self.points = 0
        self.update()

    def update(self): 
        for row in self.rows:
            for col in self.cols:
                if self.grid[row][col].flooded:
                    self.grid[row][col].set_color(Quads.color)
                    for r, c in self.across(row, col):
                        if self.grid[r][c].color == Quads.color:
                            self.grid[r][c].flooded = True
        if all([q.flooded for c in self.grid for q in c]):
            self.points += 1
            return 'vittoria'

    def restart(self):
        for row in self.rows:
            for col in self.cols:
                self.grid[row][col].flooded = False
        self.grid[0][0].flooded = True
        self.set_pattern(randomize=True)
            
    def across(self, r, c, values=False):
        coords = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        return [(r+x, c+y) for x, y in coords
                if 0 <= r+x < len(self.rows) and 0 <= c+y < len(self.cols)]
