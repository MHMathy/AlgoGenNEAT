import pygame,sys
from pygame.locals import *

from Voiture.voiture import Voiture
from test.testGenome import AfficheGenome
from IA.genome import Genome
from IA.noeudgene import NoeudGene
from IA.connectiongene import ConnectionGene


class Main:

    def __init__(self):

        pygame.init() #init sdl
        self.mainClock = pygame.time.Clock() #init timer

        #init variables
        self.WHITE = [250,250,250]
        self.WINDOWWIDTH = 1250
        self.WINDOWHEIGHT = 650
        self.gauche = False
        self.droite = False
        self.accel = False
        self.frein = False
        self.v = Voiture(250,150)
        self.police = pygame.font.Font('BradBunR.ttf', 20)

        #load images
        self.ImVoiture = pygame.image.load('images/car.png')
        self.circuit = pygame.image.load('images/course.png')
        self.imageBtn = pygame.image.load('images/BtnVoirNeurones.png')

        #transformations CONSTANTES d'images
        self.circuit = pygame.transform.scale(self.circuit,(int(self.WINDOWWIDTH*4/5),self.WINDOWHEIGHT))
        self.imageBtn = pygame.transform.scale(self.imageBtn,(250,100))


        #init fenetre
        self.screen = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT),0,32)
        pygame.display.set_caption('mathymartinet')


        #definition rect
        self.rectBtn = pygame.Rect((1000,550),(250,100))

    def draw(self): #affichage permanent

        ImVoiture = pygame.transform.rotozoom(self.ImVoiture,self.v.angle,0.05)

        self.screen.blit(self.circuit,(0,0))
        self.screen.blit(ImVoiture, self.v.pos)
        self.screen.blit(self.imageBtn,self.rectBtn)
        pygame.display.update()

    def quitter(self):
        pygame.quit()
        sys.exit()

    def ecrireSurFenetre(self, msg, pos):

        msgSurface = font.renderer(msg, TRUE, self.WHITE)
        self.screen.blit(msgSurface,pos)
        pygame.display.update()

    def gestionEvent(self): #events permanents
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == ord('q'):
                    self.gauche = True
                if event.key == ord('d'):
                    self.droite = True
                if event.key == ord('z'):
                    self.accel = True
                if event.key == ord('s'):
                    self.frein = True
                if event.key == K_ESCAPE:
                    self.quitter()
            elif event.type == KEYUP:
                if event.key == ord('q'):
                    self.gauche = False
                if event.key == ord('d'):
                    self.droite = False
                if event.key == ord('z'):
                    self.accel = False
                if event.key == ord('s'):
                    self.frein = False  
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if self.rectBtn.collidepoint(event.pos):
                    done = False
                    surf = pygame.Surface((self.WINDOWWIDTH - 250, self.WINDOWHEIGHT))
                    surf.fill(self.WHITE)
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
                    AG.draw_noeud(surf)
                    AG.draw_connec(surf)
                    surf.set_alpha(5)
                    while not done:
                        self.screen.blit(surf,(0,0))
                        pygame.display.flip()
                        
                        for event in pygame.event.get():
                            if event.type == KEYDOWN:
                                if event.key == K_ESCAPE:
                                    done = True
                            if event.type == QUIT:
                                self.quitter()


    def actionsVoiture(self):
        if self.gauche == True:
            self.v.tourne_gauche()
        if self.droite == True:
            self.v.tourne_droite()
        if self.accel == True:
            self.v.accelerer()
        if self.frein == True:
            self.v.freiner()      

    def boucle(self):
        while True:
            self.actionsVoiture()
            self.gestionEvent()
            self.v.update()
            self.draw()
            self.mainClock.tick(30)
        
    def execution(self):
        self.__init__()
        self.boucle()
        self.quitter()

