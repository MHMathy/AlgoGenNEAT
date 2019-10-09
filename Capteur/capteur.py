import pygame
import math
import Voiture.voiture


class Capteur:
    circuit = pygame.image.load("./images/course.png")
    circuit = pygame.transform.scale(circuit,(1000,650))

    def __init__(self, angleCapteur, posV):
        self.VecDir = [0,0]
        self.DistMur = 0
        self.angleCapteur = angleCapteur
        self.PosActuVoiture = posV

        self.VecDir = [math.cos(math.radians(angleCapteur)),
            math.sin(math.radians(angleCapteur))] 

    def CalcVecDir(self):
        self.VecDir = [math.cos(math.radians(angleCapteur)),
                       math.sin(math.radians(angleCapteur))] 

    def checkMur(self, surface = circuit):
        #Capteur.CalcVecDir() Appel marche pas
        posCapteur = self.PosActuVoiture

        while surface.get_at((int(round(posCapteur[0])), int(round(posCapteur[1])))) != (0,0,0):
            posCapteur = [posCapteur[0]+self.VecDir[0]*3, posCapteur[1]+self.VecDir[1]*3]

        self.DistMur = math.sqrt((posCapteur[0]-self.PosActuVoiture[0]) * (posCapteur[0]-self.PosActuVoiture[0])
                                 + (posCapteur[1]-self.PosActuVoiture[1]) * (posCapteur[1]-self.PosActuVoiture[1])) 
                            

    def getCapteur(self):
        return self.DistMur
       




