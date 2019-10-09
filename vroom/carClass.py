import math
import copy

class car:
    def __init__(self):
        self.pos = [250,150]
        self.dx = 0
        self.dy = 0

        self.angle = 0
        self.actionMoteur = 0
        self.volant = 0
        self.moteur = 0
        self.speed = 0


    def moove(self):
    #    angleTmp = self.angle
     #   angleTmp += self.volant*2
    #    posTmp = copy.deepcopy(self.pos)
     #   posTmpExtra = ([posTmp[0]+self.dx*100,posTmp[1]+self.dy*100])
     #   self.dx = math.cos(math.radians(angleTmp))
      #  self.dy = math.sin(math.radians(angleTmp))
       # self.pos[0] =int(self.pos[0] + (self.dx * self.speed))
       # self.pos[1] = int(self.pos[1] + (self.dy * self.speed))
        #self.angle = math.degrees(math.atan2(posTmpExtra[1] - posTmp[1],posTmpExtra[0] - posTmp[0]))
        #print(posTmpExtra)

    #    self.dx = math.cos(math.radians(self.angle))
     #   self.dy = math.sin(math.radians(self.angle))
      #  self.pos[0] = int(self.pos[0] + (self.dx * self.speed))
       # self.pos[1] = int(self.pos[1] + (self.dy * self.speed))
        #self.angle = math.degrees(math.atan2(self.pos[1], self.pos[0]))
        #print(self.angle)
        self.actionMoteur = self.speed

        if self.actionMoteur > self.moteur:
            if self.actionMoteur > self.moteur + self.speed:
                self.moteur += self.speed
            else:
                self.moteur = self.actionMoteur

        elif self.actionMoteur < self.moteur:
            if self.actionMoteur - self.moteur - self.speed:
                self.moteur -= self.speed
            else:
                self.moteur = self.actionMoteur

        ratioMoteur = self.moteur / 128
        ratioRoue = self.volant / 128

        if ratioMoteur >= 0:
            self.angle += ratioRoue * (0.5 + 0.5*ratioMoteur / 128) * 180 * 0.03
        else:
            self.angle += ratioRoue * (-0.5 + 0.5*ratioMoteur / 128) * 180 * 0.03

    
    def tournerG(self):
        if  self.volant > -10:
            self.volant -= 9
    
    def tournerD(self):
        if  self.volant < 10:
            self.volant += 9
             
    def accel(self):
        self.speed += 1

    def frein(self):
        self.speed -= 1
