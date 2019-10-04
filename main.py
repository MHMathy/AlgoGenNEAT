import pygame, sys
from pygame.locals import *

from Voiture.voiture import Voiture


#

def main():
    pygame.init()
    mainClock = pygame.time.Clock()

    WHITE = 250,250,250
    rect2 = pygame.rect = (100,100,50,50)
    WINDOWWIDTH = 1200
    WINDOWHEIGHT = 750
    thing = pygame.image.load('test/car.png')
    screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('Teh test')
    gauche = False
    droite = False
    accel = False
    frein = False

    v = Voiture(100,100)

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
        thing2 = pygame.transform.rotozoom(thing,v.angle,0.2)

        #thing2 = pygame.transform.scale(thing2,(100,50))
        v.maj_position()
        print(v.vitesse)
        screen.blit(thing2, v.pos)
        pygame.display.update()
        mainClock.tick(60)

main()
