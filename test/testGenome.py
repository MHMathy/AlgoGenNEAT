import pygame
import sys
sys.path.append('../')

from mathymartinet.IA.genome import Genome
from mathymartinet.IA.noeudgene import NoeudGene
from mathymartinet.IA.connectiongene import ConnectionGene

class AfficheGenome:

    def __init__(self,genome):
        self.genome = genome
        self.posnoeud = []

    def set_posNoeud(self):
        posInn = [100,100]
        posHidn = [300,100]
        posOutn = [500,100]
        tmpL = self.genome.get_listNoeuds()
        for i in range(0,len(tmpL)):
            if tmpL[i].get_type()=="input":
                self.posnoeud.append(posInn)
                posInn = [posInn[0],posInn[1]+150]
            elif(tmpL[i].get_type()=="hidden"):
                self.posnoeud.append(posHidn)
                posHidn = [posHidn[0],posHidn[1]+150]
            elif(tmpL[i].get_type()=="output"):
                self.posnoeud.append(posOutn)
                posOutn = [posOutn[0],posOutn[1]+150]
        #print(self.posnoeud)


    def draw_noeud(self):
        tmpL = self.genome.get_listNoeuds()
        color = (0,0,0)
        for i in range(0,len(tmpL)):
            if(tmpL[i].get_type()=="input"):
                color = (0,255,0)
            elif(tmpL[i].get_type()=="hidden"):
                color = (0,0,255)
            elif(tmpL[i].get_type()=="output"):
                color = (255,0,0)
            pygame.draw.circle(screen,color,(self.posnoeud[i]),20)

    def draw_connec(self):
        tmpL = self.genome.get_listConnections()
        for c in tmpL:
            pygame.draw.line(screen,(0,0,0),self.posnoeud[c.get_noeudin()-1],self.posnoeud[c.get_noeudout()-1])




pygame.init()
screen = pygame.display.set_mode((800, 600))
done = False
screen.fill([0,0,0])
mainClock = pygame.time.Clock()

G = Genome()

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

AG = AfficheGenome(G)
AG.set_posNoeud()

while not done:
    events = pygame.event.get()
    screen.fill((255,255,255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                done = True
            #if event.key == pygame.K_q:
    AG.draw_noeud()
    AG.draw_connec()
    pygame.display.flip()
    mainClock.tick(30)
pygame.quit()
sys.exit()
