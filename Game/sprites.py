import pygame
from PIL import Image

def setscreen(window):
    global screen
    screen = window

class Camera:
    def __init__(self, object):
        self.x = object.x
        self.y = object.y
        self.object = object

    def update(self):
        self.x = self.object.x
        self.y = self.object.y


class Sprite:
    def __init__(self, posx, posy, filename):
        self.x = posx
        self.y = posy
        self.bitmap = pygame.image.load(filename)
        self.img = Image.open(filename)
        (self.img_width, self.img_height) = self.img.size

    def moving(self, x, y):
        self.x += x
        self.y += y


    def resize(self, size):
        self.bitmap = pygame.transform.scale(self.bitmap, (int(self.img_width * size), int(self.img_height * size)))

def render(self, camera):
    if camera:
        screen.blit(self.bitmap, (self.x - camera.x, self.y - camera.y))
    else:
        screen.blit(self.bitmap, (self.x, self.y))


