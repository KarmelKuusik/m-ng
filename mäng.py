import pygame
from pygame.locals import *
pygame.init()


laius,kõrgus = 500,500
screen = pygame.display.set_mode((laius,kõrgus))
pygame.display.set_caption("koeramäng")

pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()       
pygame.quit()
        