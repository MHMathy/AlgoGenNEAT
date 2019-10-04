import math
class Voiture:
    def __init__(self,posx=0,posy=0,angle=0,volant=0,vitesse=0):
        self.pos = [posx,posy]
        self.angle = angle
        self.volant = volant
        self.vitesse = vitesse



    def accelerer(self):
        self.vitesse += 2

    def freiner(self):
        self.vitesse -= 1

    def tourne_gauche(self):
        if self.volant<10:
            self.volant += 1

    def tourne_droite(self):
        if self.volant>-10:
            self.volant -= 1

    def retour_neutre(self):
        if self.vitesse!=0:
            self.vitesse += (-1*self.vitesse)/abs(self.vitesse)
        if self.volant!=0:
            self.volant += (-0.5*self.volant)/abs(self.volant)

    def maj_position(self):
        self.angle += self.volant
        dx = math.cos(math.radians(self.angle))
        dy = math.sin(math.radians(self.angle))
        self.pos = (self.pos[0] + dx*self.vitesse, self.pos[1] - dy*self.vitesse)
        self.retour_neutre()
