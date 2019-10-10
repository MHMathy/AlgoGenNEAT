import pygame, sys
from pygame.locals import *

from Voiture.voiture import Voiture
from Capteur.capteur import Capteur

thing = pygame.image.load('images/car.png') 
circuit = pygame.image.load('images/course.png')
circuit = pygame.transform.scale(circuit,(1000,650))
screen = pygame.display.set_mode((1000, 650), 0, 32)
pygame.display.set_caption('Teh test')
WHITE = (0,0,0)
def main():
    (x,y) = (250,150)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        while circuit.get_at((x,y)) != (0,0,0):
            print(circuit.get_at((x,y)))
            print((x,y))
            (x,y) = (x-1,y)
        print(circuit.get_at((x,y)))
            
        screen.fill((40, 40, 40))
        screen.blit(circuit,(0,0))
        pygame.draw.circle(screen,(255,0,0),(164,y),20)

        pygame.display.update()
            
        
main()