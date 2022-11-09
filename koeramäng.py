import pygame
from pygame.locals import *
pygame.init()

# mängu aken
laius = 500
kõrgus = 500
aken = pygame.display.set_mode((laius,kõrgus))
# akna pealkiri
pygame.display.set_caption("koeramäng")
# pildid
taust = pygame.image.load("taust.png")
taust = pygame.transform.scale(taust,(laius,kõrgus))
tegelane = pygame.image.load("tegelane.png")
takistus = pygame.image.load("takistus.png")
# liikumise kiirus
kell = pygame.time.Clock()

# tegelase koordinaadid
x = laius * -0.5
y = kõrgus * 0.5

# hüppamine
y_gravitatsioon = 1
hüppe_kõrgus = 20
y_kiirus = hüppe_kõrgus

i = 0

pygame.display.flip()

jumping = False

running = True

while running:
    # liikuv taust
    aken.fill((0,0,0))
    aken.blit(taust,(i,0))
    aken.blit(taust,(laius+i,0))
    if (i==-laius):
        aken.blit(taust,(laius+i,0))
        i=0
    i-=1
    # mängu lõpetamine
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # hüppamine tühiku vajutamisel
    keys_pressed = pygame.key.get_pressed() 
    if keys_pressed[pygame.K_SPACE]:
        jumping = True
    
    aken.blit(tegelane, ((x),(y)))
    
    if jumping:
        y -= y_kiirus
        y_kiirus -= y_gravitatsioon
        if y_kiirus < -hüppe_kõrgus:
            jumping = False
            y_kiirus = hüppe_kõrgus
    
    pygame.display.update()
    # liikumise kiirus
    kell.tick(100)
pygame.quit()
        