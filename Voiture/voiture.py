import math

import sys
sys.path.append('../')

from Capteur.capteur import Capteur


class Voiture:
    def __init__(self,posx=0,posy=0,angle=0,volant=0,vitesse=0):
        self.pos = [posx,posy]
        self.angle = angle
        self.volant = volant
        self.vitesse = vitesse
        self.listCapt = []

        angleCapt = 0
        for i in range(0,7):
            self.listCapt.append(Capteur(angleCapt + self.angle, self.pos))
            angleCapt += 45

    def accelerer(self):
        self.vitesse += 1.5

    def freiner(self):
        self.vitesse -= 1.2

    def tourne_gauche(self):
        if self.volant<10:
            self.volant += 1

    def tourne_droite(self):
        if self.volant>-10:
            self.volant -= 1

    def retour_neutre(self):
        if self.vitesse > -1 and self.vitesse < 1:
            self.vitesse = 0
        else:
            self.vitesse += (-1*self.vitesse)/abs(self.vitesse)

        if self.volant!=0:
                self.volant += (-0.5*self.volant)/abs(self.volant)

    def update(self):
        self.angle += self.volant
        dx = math.cos(math.radians(self.angle))
        dy = math.sin(math.radians(self.angle))
        self.pos = (self.pos[0] + dx*self.vitesse, self.pos[1] - dy*self.vitesse)
        self.retour_neutre()

        for i in range(0,7):
            self.listCapt[i].checkMur()

    def getPos(self):
        return self.pos
    
    def getAngle(self):
        return self.angle


