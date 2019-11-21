import math

import sys


from Capteur.capteur import Capteur


class Voiture:
    def __init__(self,posx=0,posy=0,angle=0,volant=0,vitesse=0): #initialisation de la voiture
        self.pos = [posx,posy]
        self.angle = angle
        self.volant = volant
        self.vitesse = vitesse
        self.listCapt = []

        angleCapt = 0
        for i in range(0,7): #disposition des capteurs dans une liste selon le sens trigonometrique
            self.listCapt.append(Capteur(angleCapt))
            angleCapt += 45

    def accelerer(self): #augmente la vitesse
        self.vitesse += 1.5

    def freiner(self): #reduit la vitesse
        self.vitesse -= 1.2

    def tourne_gauche(self): #permet d'actionner le volant de la voiture pour donner l'ordre de tourner à gauche
        if self.volant<10:
            self.volant += 1

    def tourne_droite(self): #permet d'actionner le volant de la voiture pour donner l'ordre de tourner à droite
        if self.volant>-10:
            self.volant -= 1

    def retour_neutre(self):
        if self.vitesse > -1 and self.vitesse < 1:
            self.vitesse = 0
        else:
            self.vitesse += (-1*self.vitesse)/abs(self.vitesse)

        if self.volant!=0:
                self.volant += (-0.5*self.volant)/abs(self.volant)

    def update(self): #met à jour les paramètres de la voiture (et ses capteurs)
        self.angle += self.volant
        dx = math.cos(math.radians(self.angle))
        dy = math.sin(math.radians(self.angle))
        self.pos = (self.pos[0] + dx*self.vitesse, self.pos[1] - dy*self.vitesse)
        self.retour_neutre()

        Capteur.PosActuVoiture = self.pos
        Capteur.AngleVoiture = self.angle
        for i in range(0,7):
            self.listCapt[i].checkMur()

    def getPos(self): #renvoie la position de la voiture
        return self.pos
    
    def getAngle(self): #renvoie l'angle d'inclinaison de la voiture
        return self.angle

    def getDistRetourCapt(self): #renvoie une liste comportant la distance de chaque capteurs par rapport au mur le plus proche
        listTmp = [0,0,0,0,0,0,0,0]
        for i in range(7):
            listTmp[i] = self.listCapt[i].getDistCapteur()
        return listTmp


