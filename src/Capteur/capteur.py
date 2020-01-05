import math
import Voiture.voiture
from Outil.outil import Map

## classe Capteur qui calcul la distance par rapport au mur le plus proche
class Capteur:

    ## on recupere la position et l'angle de la voiture pour pouvoir faire les calculs

    ## constructeur qui initialise les variables d'un capteur
    # @param angleCapteur angle du capteur de la voiture
    def __init__(self, angleCapteur): #initialisation capteur
        self.VecDir = [0,0]
        self.DistMur = 0
        self.posActuVoiture = [0,0]
        self.angleVoiture = 0
        self.angleCapteur = angleCapteur
        self.posCapteur = self.posActuVoiture

    ## fonction qui calcul le vecteur directeur de l'angle
    def CalcVecDir(self):
       self.VecDir = [math.cos(math.radians(self.angleCapteur - self.angleVoiture)),
                       math.sin(math.radians(self.angleCapteur - self.angleVoiture))]

    ## fonction qui calcul la distance du mur le plus proche
    def checkMur(self): #regarde la position du mur le plus proche de chaque capteur
        #return True #brainfuck du programme avant de corriger rotozoom
        self.posCapteur = self.posActuVoiture   #et calcul la distance entre la voiture et cette position

        self.CalcVecDir()

        while True:

            x = int(round(self.posCapteur[0]))
            y = int(round(self.posCapteur[1]))

            assert x > 0 and x < 1000
            assert y > 0 and y < 650
            """
            if x<0:
                x=0
            elif x>800:
                x=800
            elif y<0:
                y=0
            elif y>550:
                y=550
            """


            if Map.map[y][x] == (0,0,0): #on trouve du noir on sort de la boucle
                break

            else:
                self.posCapteur = [self.posCapteur[0]+self.VecDir[0]*3, self.posCapteur[1]+self.VecDir[1]*3]

        self.DistMur = math.sqrt((x-self.posActuVoiture[0]) * (x-self.posActuVoiture[0])
                                 + (y-self.posActuVoiture[1]) * (y-self.posActuVoiture[1]))

    def getDistCapteur(self): #retourne la distance d'un capteur par rapport au mur le plus proche
        return self.DistMur


    def setPosActuVoiture(self,val):
        self.posActuVoiture = val
