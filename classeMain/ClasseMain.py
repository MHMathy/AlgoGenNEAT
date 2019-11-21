import pygame,sys
from pygame.locals import *

sys.path.append('./')

from afficheGenome.afficheGenome import AfficheGenome
from IA.genome import Genome
from IA.noeudgene import NoeudGene
from IA.connectiongene import ConnectionGene
from Voiture.voiture import Voiture


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
        self.BoolAffResNeuro = False

        self.G = Genome()
        self.l = []
        self.AG = AfficheGenome(self.G)
        

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

        #init du reseau neuronne test
        self.surf = pygame.Surface((self.WINDOWWIDTH - 250, self.WINDOWHEIGHT))
        self.surf.fill(self.WHITE)

        self.l.append(NoeudGene("input", 1))
        self.l.append(NoeudGene("input", 2))
        self.l.append(NoeudGene("output", 3))
        self.l.append(NoeudGene("output", 4))
        self.l.append(NoeudGene("input", 5))
                
        for n in self.l:
            self.G.ajout_noeud(n)

        for i in range(0,4):
            self.G.ajout_connec_mutation()
        self.AG = AfficheGenome(self.G)
        self.AG.set_posNoeud()
        self.AG.draw_noeud(self.surf)
        self.AG.draw_connec(self.surf)
        self.surf.set_alpha(200)



    def draw(self): #affichage permanent

        ImVoiture = pygame.transform.rotozoom(self.ImVoiture,self.v.angle,0.05)

        self.screen.blit(self.circuit,(0,0))
        self.screen.blit(self.imageBtn,self.rectBtn)
        self.screen.blit(ImVoiture, self.v.pos)

        if self.BoolAffResNeuro == True:
            self.screen.blit(self.surf,(0,0))
            

        pygame.display.update()

    def quitter(self): #quitte la sdl et ferme la fenetre python
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
                if event.key == K_ESCAPE and self.BoolAffResNeuro == False:
                    self.quitter()                
                if event.key == K_ESCAPE and self.BoolAffResNeuro == True:
                        self.BoolAffResNeuro = False
             #   if event.key == K_m:
              #      self.surf.fill((255,255,255))
               #     self.G.ajout_noeud_mutation()
                #    self.AG.set_posNoeud()
                 #   self.AG.draw_noeud(self.surf)
                   #  self.AG.draw_connec(self.surf)
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
                    self.BoolAffResNeuro = True

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
            self.v.update()
            self.draw()
            self.gestionEvent()
            self.mainClock.tick(30)
        
    def execution(self):
        self.__init__()
        self.boucle()
        self.quitter()

