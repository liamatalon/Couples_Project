import pygame
from pygame.locals import *
import consts

screen = pygame.display.set_mode(
        (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

pygame.display.set_caption('Player Movement')

image = pygame.image.load(r'soldier.png')



pygame.display.update()
