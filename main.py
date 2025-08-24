import pygame
from pygame.locals import *

pygame.init()

window = pygame.display.set_mode((600, 600))

pygame.display.set_caption('Player Movement')

image = pygame.image.load(r'soldier.png')

# win = False
#if body touch flag :
#     win = True
#
# while win == False:

window = pygame.display.set_mode((1000, 700))

pygame.display.set_caption('Player Movement')

image = pygame.image.load(r'soldier.png')

x = 100
y = 100

velocity = 15

run = True
while run:

    window.fill((120, 250, 100))

    window.blit(image, (x, y))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                x -= velocity

            if event.key == pygame.K_RIGHT:
                x += velocity

            if event.key == pygame.K_UP:
                y -= velocity

            if event.key == pygame.K_DOWN:
                y += velocity
        if x<-100 or y<-10:
            run = False
        if x>500 or y>205:
            run = False

        pygame.display.update()


