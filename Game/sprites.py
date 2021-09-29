import pygame
from PIL import Image

def set_screen(window):
    global screen, screen_w, screen_h
    screen = window
    w, h = pygame.display.get_surface().get_size()
    screen_w = w * 0.5
    screen_h = h * 0.5


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
        self.size_x = 0
        self.size_y = 0

    def moving(self, x, y):
        self.x += x
        self.y += y


    def resize(self, size):
        self.size_x = int(self.img_width * size)
        self.size_y = int(self.img_height * size)
        self.bitmap = pygame.transform.scale(self.bitmap, (self.size_x, self.size_y))


def render(self, camera):
    if camera == 'NONE':
        screen.blit(self.bitmap, (self.x, self.y))
    else:
        rend_x = self.x - camera.x + screen_w - self.size_x * 0.5
        rend_y = self.y - camera.y + screen_h - self.size_y * 0.5
        screen.blit(self.bitmap, (rend_x, rend_y))



