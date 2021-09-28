import pygame

def setscreen(window):
    global screen
    screen = window


class Sprite:
    def __init__(self, posx, posy, filename):
        self.x = posx
        self.y = posy
        self.bitmap = pygame.image.load(filename)

def render(self):
    screen.blit(self.bitmap, (self.x, self.y))
