import pygame
from pygame.locals import *
from random import*
import time
from perso import*

pygame.init()

blanc = (255,255,255)
fenetre = pygame.display.set_mode((750, 1050))

surface=pygame.display.set_mode((1050,750))

fond = pygame.image.load("index.jpeg")
fond = pygame.transform.scale(fond,(1050,750))
surface.blit(fond,(0,0))

pers = pygame.image.load("mario.jpeg")
pers.set_colorkey(blanc)

pygame.display.set_caption("test") 

def principal():
    p = perso(50,50)
    fenetre = False
    while fenetre == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fenetre = True
                pygame.QUIT
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == K_d:
                    print(surface.get_at((p.x+150,p.y+150)))
                    if surface.get_at((p.x+150,p.y+150)) == (198,206,45):
                        p.move(p.x,p.y)
                    else:
                        p.move(p.x+150, p.y+150)
        surface.blit(fond,(0,0))
        surface.blit(pers,(p.x,p.y))
        pygame.display.update()
        




principal()
