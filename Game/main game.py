import pygame, sys
from sprites import *

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        win.fill((127, 214, 84))
        render(player)

        pygame.display.update()

pygame.init()

winWidth = 1280
winHeight = 720
image = pygame.image.load('img.png')
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption('My RPG')
pygame.display.set_icon(image)

setscreen(win)
player = Sprite(0, 0, 'litle_ninja.png')

game()