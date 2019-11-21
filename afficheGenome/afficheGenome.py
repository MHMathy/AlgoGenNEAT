import pygame
import sys
import math

sys.path.append('./')

from IA.genome import Genome
from IA.noeudgene import NoeudGene
from IA.connectiongene import ConnectionGene
from IA.innovation import Innovation

class AfficheGenome:

    def __init__(self,genome):
        self.genome = genome
        self.posnoeud = []

    def set_posNoeud(self):
        posInn = [100,100]
        posHidn = [300,130]
        posOutn = [500,170]
        self.posNoeud = []
        tmpL = self.genome.get_listNoeuds()

        for i in range(0,len(tmpL)):
            if tmpL[i].get_type()=="input":
                self.posnoeud.append(posInn)
                posInn = [posInn[0],posInn[1]+150]
            elif tmpL[i].get_type()=="hidden":
                self.posnoeud.append(posHidn)
                posHidn = [posHidn[0],posHidn[1]+150]
            elif tmpL[i].get_type()=="output":
                self.posnoeud.append(posOutn)
                posOutn = [posOutn[0],posOutn[1]+150]
        #print(self.posnoeud)


    def draw_noeud(self, surf):
        tmpL = self.genome.get_listNoeuds()
        color = (0,0,0)
        for i in range(0,len(tmpL)):
            if tmpL[i].get_type()=="input":
                color = (0,255,0)
            elif tmpL[i].get_type()=="hidden":
                color = (0,0,255)
            elif tmpL[i].get_type()=="output":
                color = (255,0,0)
            pygame.draw.circle(surf,color,(self.posnoeud[i]),20)

    def draw_line_co(self,inn, outn, surf):
        dX = outn[0] - inn[0]
        dY = outn[1] - inn[1]
        Len = math.sqrt(dX* dX + dY * dY)
        udX = dX / Len
        udY = dY / Len
        end = [outn[0]-15 * udX, outn[1]-15 * udY]
        end = list(map(lambda x: int(x),end))
        #print(end)
        pygame.draw.line(surf,(0,0,0),inn,end,2)

        pygame.draw.circle(surf,(0,0,0),[end[0],end[1]],5)


    def draw_connec(self, surf):
        tmpL = self.genome.get_listConnections()
        #print(self.posnoeud)
        for c in tmpL:
            #print("in",self.genome.get_noeud(c.get_noeudin()).get_type())
            #print("out",self.genome.get_noeud(c.get_noeudout()).get_type())
            #print(c.get_actif())
            if c.get_actif()==True:
                self.draw_line_co(self.posnoeud[c.get_noeudin()-1],self.posnoeud[c.get_noeudout()-1], surf)
                self.draw_line_co(self.posnoeud[c.get_noeudin()-1],self.posnoeud[c.get_noeudout()-1])



pygame.init()
screen = pygame.display.set_mode((800, 600))
screen.fill([255,255,255])
mainClock = pygame.time.Clock()
ino = Innovation
G = Genome(ino)

l = []
l.append(NoeudGene("input", 1))
l.append(NoeudGene("input", 2))
l.append(NoeudGene("output", 3))
l.append(NoeudGene("output", 4))
l.append(NoeudGene("input", 5))
for n in l:
    G.ajout_noeud(n)


for i in range(0,4):
    G.ajout_connec_mutation()




screen.fill((255,255,255))

AG = AfficheGenome(G)
AG.set_posNoeud()
AG.draw_noeud()
AG.draw_connec()
done = False
while not done:


    AG = AfficheGenome(G)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
            if event.key == pygame.K_m:
                screen.fill((255,255,255))
                G.ajout_noeud_mutation()
                AG.set_posNoeud()
                AG.draw_noeud()
                AG.draw_connec()
            #if event.key == pygame.K_q:

    pygame.display.update()
    mainClock.tick(30)
pygame.quit()
sys.exit()
