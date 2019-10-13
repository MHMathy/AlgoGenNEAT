import pygame
import math
import Voiture.voiture

class Capteur:
    circuit = pygame.image.load("./images/course.png")
    circuit = pygame.transform.scale(circuit,(1000,650))
    PosActuVoiture = [0,0]
    AngleVoiture = 0

    def __init__(self, angleCapteur): #initialisation capteur
        self.VecDir = [0,0] 
        self.DistMur = 0
        self.angleCapteur = angleCapteur

    
    def CalcVecDir(self):
       self.VecDir = [math.cos(math.radians(self.angleCapteur + self.AngleVoiture)),
                       math.sin(math.radians(self.angleCapteur + self.AngleVoiture))] 

    def checkMur(self, surface = circuit): #regarde la position du mur le plus proche de chaque capteur 
        posCapteur = self.PosActuVoiture   #et calcul la distance entre la voiture et cette position
    
        self.CalcVecDir()

        while True:
            x = int(round(posCapteur[0]))
            y = int(round(posCapteur[1]))
            assert x > 0 and x < 1000
            assert y > 0 and y < 650

            if surface.get_at([x,y]) == (0,0,0):
                
                break
            else:
                posCapteur = [posCapteur[0]+self.VecDir[0]*3, posCapteur[1]+self.VecDir[1]*3]
        
        self.DistMur = math.sqrt((x-self.PosActuVoiture[0]) * (x-self.PosActuVoiture[0])
                                 + (y-self.PosActuVoiture[1]) * (y-self.PosActuVoiture[1])) 
                            
    def getDistCapteur(self): #retourne la distance d'un capteur par rapport au mur le plus proche
        return self.DistMur

       




