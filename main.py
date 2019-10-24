import pygame, sys
from pygame.locals import *

from IA.genome import Genome
from Voiture.voiture import Voiture
from Capteur.capteur import Capteur


#cd Documents/L3/LifProjet/mathymartinet/


def main():
    pygame.init() #initialisation sdl
    mainClock = pygame.time.Clock() #initialisation timer

    WHITE = 250,250,250
    rect2 = pygame.rect = (100,100,50,50)
    WINDOWWIDTH = 1000
    WINDOWHEIGHT = 650

    #gestion images pygames
    thing = pygame.image.load('images/car.png')
    circuit = pygame.image.load('images/course.png')
    circuit = pygame.transform.scale(circuit,(1000,650))
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('Teh test')


    gauche = False
    droite = False
    accel = False
    frein = False

    v = Voiture(250,150)

    #event clavier
    while True:
        rect2 = pygame.rect = (100,100,50,50)
        if gauche == True:
            v.tourne_gauche()
        if droite == True:
            v.tourne_droite()
        if accel == True:
            v.accelerer()
        if frein == True:
            v.freiner()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == ord('q'):
                    gauche = True
                if event.key == ord('d'):
                    droite = True
                if event.key == ord('z'):
                    accel = True
                if event.key == ord('s'):
                    frein = True
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == KEYUP:
                if event.key == ord('q'):
                    gauche = False
                if event.key == ord('d'):
                    droite = False
                if event.key == ord('z'):
                    accel = False
                if event.key == ord('s'):
                    frein = False

        pygame.draw.rect(screen,WHITE,rect2)

        screen.fill((40, 40, 40))
        thing2 = pygame.transform.rotozoom(thing,v.angle,0.05)
        v.update()
        screen.blit(circuit,(0,0))
        screen.blit(thing2, v.pos)

        pygame.display.update()
        mainClock.tick(30)

main()
