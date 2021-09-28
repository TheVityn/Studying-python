import pygame, sys
from sprites import *

def game():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            player.moving(p_speed, 0)
        elif keys[pygame.K_LEFT]:
            player.moving(-p_speed, 0)
        if keys[pygame.K_UP]:
            player.moving(0, -p_speed)
        elif keys[pygame.K_DOWN]:
            player.moving(0, p_speed)

        win.fill((127, 214, 84))
        render(player)
        clock.tick(fps)
        pygame.display.update()

pygame.init()

winWidth = 1900
winHeight = 1050
image = pygame.image.load('img.png')
win = pygame.display.set_mode((winWidth, winHeight))
pygame.display.set_caption('My RPG')
pygame.display.set_icon(image)

setscreen(win)
player = Sprite(20, 20, 'little_warior.png')
fps = 60
clock = pygame.time.Clock()

p_speed = 5
game()