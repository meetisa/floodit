import pygame as pg

class Quad:
    def __init__(self, size, coords):
        self.surf = pg.Surface((size, size))
        self.rect = pg.Rect(coords, (size, size))

    def set_color(self, color):
        self.surf.fill(color)
        self.color = color

    def render(self, screen):
        screen.blit(self.surf, self.rect)
