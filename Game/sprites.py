import pygame
from Pillow import image

def setscreen(window):
    global screen
    screen = window


class Sprite:
    def __init__(self, posx, posy, filename):
        self.x = posx
        self.y = posy
        self.bitmap = pygame.image.load(filename)

    def moving(self, x, y):
        self.x += x
        self.y += y

def render(self):
    screen.blit(self.bitmap, (self.x, self.y))

def resize(self, size):
    self.bitmap = pygame
