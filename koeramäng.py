import pygame
from pygame.locals import *
pygame.init()

laius = 500
kõrgus = 500
aken = pygame.display.set_mode((laius,kõrgus))
pygame.display.set_caption("koeramäng")
taust = pygame.image.load("taust.png")
taust = pygame.transform.scale(taust,(laius,kõrgus))
kell = pygame.time.Clock()

tegelane = pygame.image.load("tegelane.png")
takistus = pygame.image.load("takistus.png")

i = 0

pygame.display.flip()

running = True

while running:
    aken.fill((0,0,0))
    aken.blit(taust,(i,0))
    aken.blit(taust,(laius+i,0))
    if (i==-laius):
        aken.blit(taust,(laius+i,0))
        i=0
    i-=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #keys = pygame.key.get_pressed()
    #if jump == False:
        #if keys[pygame.K_SPACE]:
            #jump = True
    
    aken.blit(tegelane, ((laius * -0.5),(kõrgus * 0.5)))
    
    pygame.display.update()
    kell.tick(100)
pygame.quit()
        