import pygame, sys
from pygame.locals import *

from IA.genome import Genome
from Voiture.voiture import Voiture
from Capteur.capteur import Capteur
from classeMain.ClasseMain import Main

#cd Documents/L3/LifProjet/mathymartinet/

## initialisation d'un main, et lancement de son execution
def main():
    main = Main()
    main.execution()

main()