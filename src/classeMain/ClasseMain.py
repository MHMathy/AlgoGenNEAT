import pygame,sys
from pygame.locals import *

#from afficheGenome.afficheGenome import AfficheGenome
from IA.genome import Genome
from IA.noeudgene import NoeudGene
from IA.connectiongene import ConnectionGene
from Voiture.voiture import Voiture

## classe qui permet la creation d'un rectangle permettant la modification de la valeur d'une variable
class rectModifierVariables:

    ## constructeur de la classe
    def __init__(self, pos, texte, valeur, police):
        self.pos = pos
        self.police = police
        self.__valeur = str(valeur)
        self.txtInit = texte
        self.__etat = False
        self.__rect = pygame.Rect(self.pos, (245, 55))

    ## retourne le texte a afficher selon l'action en cours
    def getTexte(self):
        return  self.police.render(self.txtInit + str(self.__valeur) , True, (255,255,255))

    ## permet la modification de la valeur tampon
    # @param valeur : valeur a concatener a la valeur tampon
    def setValeur(self, val):
        self.__valeur += str(val)

    ## fonction qui met a jour la valeur courante et de la variable en question
    # @param ind : valeur permettant d'identifier la variable a modifer
    def ValiderNouvelleValeur(self, ind):

        if ind == 5: self.__valeur = int(self.__valeur)
        else : self.__valeur = float(self.__valeur)

        if ind == 0:
            Genome.PROBA_MUTATION = self.getValeur()
            Main.listeConstantes["proba_mut"] = self.getValeur()

        elif ind == 1:
            Genome.PROBA_MUTATION_COEF = self.getValeur()
            Main.listeConstantes["proba_mut_coef"] = self.getValeur()

        elif ind == 2:
            Genome.DISTANCE_C1 = self.getValeur()
            Main.listeConstantes["C1"] = self.getValeur()
        elif ind == 3:
            Genome.DISTANCE_C2 = self.getValeur()
            Main.listeConstantes["C2"] = self.getValeur()

        elif ind == 4:
            Genome.DISTANCE_C3 = self.getValeur()
            Main.listeConstantes["C3"] = self.getValeur()

        elif ind == 5:
            Genome.DEFAULT_N_CONNEC = int(self.getValeur())
            Main.listeConstantes["default_connec"] = self.getValeur()

    ## renvoie l'etat du rectant
    def getEtat(self):
        return self.__etat

    ## passe l'etat courant dans son etat oppose
    def setEtat(self):
        self.__etat = not self.__etat

    ## renvoie le rectangle de l'instance
    def getRect(self):
        return self.__rect

    ## permet de supprimer le dernier caractere contenu dans la chaine de caractere de la valeur tampon
    def supprCarac(self):
        self.__valeur = self.__valeur[0:-1]

    ## renvoie la valeur courante de l'instance
    def getValeur(self):
        return self.__valeur

## class Main qui gere les evenements SDL et l'execution globale du programme
class Main:
    listeConstantes = {"proba_mut": Genome.PROBA_MUTATION,
                       "proba_mut_coef": Genome.PROBA_MUTATION_COEF,
                       "C1": Genome.DISTANCE_C1,
                       "C2": Genome.DISTANCE_C2,
                       "C3": Genome.DISTANCE_C3,
                       "default_connec": Genome.DEFAULT_N_CONNEC}

    ## constructeur qui initialise les differentes variables de la classe
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
        self.G = Genome.default()
        self.v = Voiture(self.G,195,145)
        self.BoolAffResNeuro = False
        self.__reset = False
        self.pause = True

        self.listRect = []

        #load images
        self.ImVoiture = pygame.image.load('../data/car.png')
        self.circuit = pygame.image.load('../data/course.png')
        self.imageBtn = pygame.image.load('../data/BtnVoirNeurones.png')

        self.police = pygame.font.Font('../data/arial_narrow_7.ttf', 23)

        #transformations CONSTANTES d'images
        self.circuit = pygame.transform.scale(self.circuit,(int(self.WINDOWWIDTH*4/5),self.WINDOWHEIGHT))
        self.imageBtn = pygame.transform.scale(self.imageBtn,(250,100))


        #init fenetre
        self.screen = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT),0,32)
        pygame.display.set_caption('mathymartinet')


        #definition rect
        self.rectBtn = pygame.Rect((1000,550),(250,100))
        self.rectReset = pygame.Rect((1100,530), (250,20))
        self.rectPause = pygame.Rect((1100,480), (250,20))

        self.listRect.append(rectModifierVariables((1005,0), "Proba_mutation : ", Genome.PROBA_MUTATION, self.police))
        self.listRect.append(rectModifierVariables((1005, 40), "Proba_mutation_coef : ", Genome.PROBA_MUTATION_COEF, self.police))
        self.listRect.append(rectModifierVariables((1005, 80), "Distance_c1 : ", Genome.DISTANCE_C1, self.police))
        self.listRect.append(rectModifierVariables((1005, 120), "Distance_c2 : ", Genome.DISTANCE_C2, self.police))
        self.listRect.append(rectModifierVariables((1005, 160), "Distance_c3 : ", Genome.DISTANCE_C1, self.police))
        self.listRect.append(rectModifierVariables((1005, 200), "default_n_connec : ", Genome.DEFAULT_N_CONNEC, self.police))
        self.listRect.append(rectModifierVariables((1005, 240), "default_n_connec : ", Genome.DEFAULT_N_CONNEC, self.police))
        self.listRect.append(rectModifierVariables((1005, 280), "default_n_connec : ", Genome.DEFAULT_N_CONNEC, self.police))        
        self.listRect.append(rectModifierVariables((1005, 320), "default_n_connec : ", Genome.DEFAULT_N_CONNEC, self.police))        
        self.listRect.append(rectModifierVariables((1005, 360), "default_n_connec : ", Genome.DEFAULT_N_CONNEC, self.police))
        self.listRect.append(rectModifierVariables((1005,400), "default_n_connec : ", Genome.DEFAULT_N_CONNEC, self.police))
        self.listRect.append(rectModifierVariables((1005,440), "default_n_connec : ", Genome.DEFAULT_N_CONNEC, self.police))
        #init du reseau neuronne test
        self.surf = pygame.Surface((self.WINDOWWIDTH - 250, self.WINDOWHEIGHT))
        self.surf.fill(self.WHITE)

    def getReset(self):
        return self.__reset()

    # fonction qui gere les affichages permanents (circuit, voiture, boutons,..)
    def draw(self): #affichage permanent

        ImVoiture = pygame.transform.rotozoom(self.ImVoiture,self.v.angle,0.05)
        posRectImVoiture = ImVoiture.get_rect().center

        listeCapteursCircuit = [(182,130), (525,197), (715, 295), (795,447), (525, 510), (282, 490),(395,346),(235,280)]

        self.screen.blit(self.circuit,(0,0))
        self.screen.blit(self.imageBtn,self.rectBtn)

        for i in range(len(self.listRect)):
            if self.listRect[i].getEtat() == True: pygame.draw.rect(self.screen,(255,127,0), self.listRect[i].getRect())
            else: pygame.draw.rect(self.screen,(0,0,0), self.listRect[i].getRect())
            self.screen.blit(self.listRect[i].getTexte(), self.listRect[i].getRect())

        x = self.v.pos[0]-posRectImVoiture[0]
        y = self.v.pos[1]-posRectImVoiture[1]

        self.screen.blit(ImVoiture, (x,y))

        for capt in listeCapteursCircuit:
            pygame.draw.circle(self.screen, (255,0,0), capt, 3)

        if self.BoolAffResNeuro == True:
            self.screen.blit(self.surf,(0,0))

        self.screen.blit(self.police.render("Reset", True, (255,255,255)),self.rectReset)

        if self.pause == True:
            pygame.draw.rect(self.screen,(0,0,0), self.rectPause)
            self.screen.blit(self.police.render("Play", True, (255,255,255)),self.rectPause)
        else:
            pygame.draw.rect(self.screen,(0,0,0), self.rectPause)
            self.screen.blit(self.police.render("Pause", True, (255,255,255)),self.rectPause)

        pygame.display.update()

    ## fonction qui quitte la SDL et ferme la fenetre python
    def quitter(self): #quitte la sdl et ferme la fenetre python
        pygame.quit()
        sys.exit()

    ## fonction qui gere les differents evenements SDL: appuie sur une touche, appuie sur un bouton..
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
                if event.key == ord('t'):
                    print(self.v.calculScore())
                if event.key == K_ESCAPE and self.BoolAffResNeuro == False:
                    self.quitter()
                if event.key == K_ESCAPE and self.BoolAffResNeuro == True:
                        self.BoolAffResNeuro = False

                for i in range(len(self.listRect)):
                    if self.listRect[i].getEtat() == True and (event.key == K_KP0 or event.key == K_0):
                        self.listRect[i].setValeur(0)
                
                    if self.listRect[i].getEtat() == True and (event.key == K_KP1 or event.key == K_1):
                        self.listRect[i].setValeur(1)

                    if self.listRect[i].getEtat() == True and (event.key == K_KP2 or event.key == K_2):
                        self.listRect[i].setValeur(2)

                    if self.listRect[i].getEtat() == True and (event.key == K_KP3 or event.key == K_3):
                        self.listRect[i].setValeur(3)

                    if self.listRect[i].getEtat() == True and (event.key == K_KP4 or event.key == K_4):
                        self.listRect[i].setValeur(4)

                    if self.listRect[i].getEtat() == True and (event.key == K_KP5 or event.key == K_5):
                        self.listRect[i].setValeur(5)

                    if self.listRect[i].getEtat() == True and (event.key == K_KP6 or event.key == K_6):
                        self.listRect[i].setValeur(6)

                    if self.listRect[i].getEtat() == True and (event.key == K_KP7 or event.key == K_7):
                        self.listRect[i].setValeur(7)
                    
                    if self.listRect[i].getEtat() == True and (event.key == K_KP8 or event.key == K_8):
                        self.listRect[i].setValeur(8)

                    if self.listRect[i].getEtat() == True and (event.key == K_KP9 or event.key == K_9):
                        self.listRect[i].setValeur(9)

                    if self.listRect[i].getEtat() == True and (event.key == K_KP_PERIOD or event.key == K_PERIOD):
                        self.listRect[i].setValeur('.')

                    if self.listRect[i].getEtat() == True and event.key == K_BACKSPACE:
                        self.listRect[i].supprCarac()
                    
                    if self.listRect[i].getEtat() == True and event.key == K_RETURN:
                        self.listRect[i].ValiderNouvelleValeur(i)
                        self.listRect[i].setEtat()

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

                for i in range(len(self.listRect)):
                    if self.listRect[i].getEtat() == True: self.listRect[i].setEtat()

                    if self.listRect[i].getRect().collidepoint(event.pos):                    
                        self.listRect[i].setEtat()
                    
                if self.rectReset.collidepoint(event.pos):
                    self.__reset = True

                if self.rectPause.collidepoint(event.pos) and self.pause == False:
                    self.pause = True

                elif self.rectPause.collidepoint(event.pos) and self.pause == True:
                    self.pause = False
                
    ## fonction qui actionnent la voiture en fonction des evenements
    def actionsVoiture(self):
        if self.gauche == True:
            self.v.tourne_gauche()
        if self.droite == True:
            self.v.tourne_droite()
        if self.accel == True:
            self.v.accelerer()
        if self.frein == True:
            self.v.freiner()

    ## boucle qui gere en permanence les fonctions principales du programme
    def boucle(self):
        while True:
            
            self.draw()
            self.gestionEvent()

            if self.pause == False:
                self.actionsVoiture()
                self.v.update()               
                self.mainClock.tick(30)

            if self.__reset == True:
                Main.resetAvecNewConst()
                Main.__init__(self)

    ## fonction qui permet l'execution globale du programme
    def execution(self):
        self.boucle()
        self.quitter()

    @classmethod
    def resetAvecNewConst(cls):
        Genome.PROBA_MUTATION = Main.listeConstantes["proba_mut"]
        Genome.PROBA_MUTATION_COEF = Main.listeConstantes["proba_mut_coef"]
        Genome.DISTANCE_C1 = Main.listeConstantes["C1"]
        Genome.DISTANCE_C1 = Main.listeConstantes["C2"]
        Genome.DISTANCE_C1 = Main.listeConstantes["C3"]
        Genome.DEFAULT_N_CONNEC = Main.listeConstantes["default_connec"]