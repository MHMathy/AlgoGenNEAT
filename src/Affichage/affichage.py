import pygame,sys
from pygame.locals import *
from Outil.outil import Constantes
from Outil.outil import Map
from ProgGlobal.progglobal import ProgGlobal
import random
import copy

## classe qui permet la creation d'un rectangle permettant la modification de la valeur d'une variable
class rectModifierVariables:

    ## constructeur de la classe
    def __init__(self, pos, texte, valeur, police):
        self.pos = pos
        self.police = police
        self.__valeur = str(valeur)
        self.txtInit = texte
        self.nom = self.txtInit[0:-1]
        self.__etat = False
        self.__rect = pygame.Rect(self.pos, (245, 40))

    ## retourne le texte a afficher selon l'action en cours
    def getTexte(self):
        return  self.police.render(self.txtInit + " : " + str(self.__valeur) , True, (255,255,255))

    ## permet la modification de la valeur tampon
    # @param valeur : valeur a concatener a la valeur tampon
    def setValeur(self, val):
        self.__valeur += str(val)

    ## fonction qui met a jour la valeur courante et de la variable en question
    # @param -1 : valeur permettant d'identifier la variable a modifer
    def ValiderNouvelleValeur(self):
        tmp = 0
        if "." in self.__valeur:
            tmp = float(self.__valeur)

        else:
            tmp = int(self.__valeur)

        Constantes.set_listConstantes(self.txtInit, tmp)

    ## renvoie l'etat du rectangle
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

## classe Affichage qui gere tous les evenements d'affichage, la boucle du programme et les events
class Affichage:

    ## constructeur de la classe Affichage
    def __init__(self):

        pygame.init()
        pygame.font.init()

        self.WHITE = [255,255,255]
        self.WINDOWWIDTH = 1250
        self.WINDOWHEIGHT = 650
        self.boolAffProgression = False
        self.reset = False
        self.boolAffGenome = False
        self.pause = True
        self.demarrer = False
        self.mainClock = pygame.time.Clock()

        self.listRect = []

        #init fenetre
        self.screen = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT),0,32)
        pygame.display.set_caption('mathymartinet')

        #charger images
        self.ImVoiture = pygame.image.load('../data/car.png')
        self.circuit = pygame.image.load('../data/course.png')
        self.imageBtn = pygame.image.load('../data/BtnVoirProgression.png')

        self.police = pygame.font.Font('../data/arial_narrow_7.ttf', 17)

        #transformations CONSTANTES d'images
        self.circuit = pygame.transform.scale(self.circuit,(int(self.WINDOWWIDTH*4/5),self.WINDOWHEIGHT))
        self.imageBtn = pygame.transform.scale(self.imageBtn,(250,100))



        #definition rect
        self.rectBtn = pygame.Rect((1000,550),(250,100))
        self.rectReset = pygame.Rect((1000,510), (125,30))
        self.rectPause = pygame.Rect((1125,510), (125,30))

        constantesModifiables = Constantes.get_listConstantes()

        self.listRect.append(rectModifierVariables((1005,0), "TAILLE_POPULATION", constantesModifiables["TAILLE_POPULATION"], self.police))
        self.listRect.append(rectModifierVariables((1005, 40), "DURREE_CYCLE_EN_S", constantesModifiables["DURREE_CYCLE_EN_S"], self.police))
        self.listRect.append(rectModifierVariables((1005, 80), "DISTANCE_MIN_ESPECE", constantesModifiables["DISTANCE_MIN_ESPECE"], self.police))
        self.listRect.append(rectModifierVariables((1005, 120), "PROBA_MUTATION_GENOME", constantesModifiables["PROBA_MUTATION_GENOME"], self.police))
        self.listRect.append(rectModifierVariables((1005, 160), "PROBA_AJOUT_CONNEC_GENOME", constantesModifiables["PROBA_AJOUT_CONNEC_GENOME"], self.police))
        self.listRect.append(rectModifierVariables((1005, 200), "PROBA_AJOUT_NOEUD_GENOME", constantesModifiables["PROBA_AJOUT_NOEUD_GENOME"], self.police))
        self.listRect.append(rectModifierVariables((1005, 240), "PROBA_MUTATION", constantesModifiables["PROBA_MUTATION"], self.police))
        self.listRect.append(rectModifierVariables((1005, 280), "PROBA_MUTATION_COEF", constantesModifiables["PROBA_MUTATION_COEF"], self.police))
        self.listRect.append(rectModifierVariables((1005, 320), "DISTANCE_C1", constantesModifiables["DISTANCE_C1"], self.police))
        self.listRect.append(rectModifierVariables((1005, 360), "DISTANCE_C2", constantesModifiables["DISTANCE_C2"], self.police))
        self.listRect.append(rectModifierVariables((1005, 400), "DISTANCE_C3", constantesModifiables["DISTANCE_C3"], self.police))
        self.listRect.append(rectModifierVariables((1005, 440), "DEFAULT_N_CONNEC", constantesModifiables["DEFAULT_N_CONNEC"], self.police))
        self.listRect.append(rectModifierVariables((1005, 480), "COEF_EXPO", constantesModifiables["COEF_EXPO"], self.police))

        #init du reseau neuronne test
        self.surf = pygame.Surface((self.WINDOWWIDTH - 250, self.WINDOWHEIGHT))
        self.surf.fill(self.WHITE)

        self.surf2 = pygame.Surface((self.WINDOWWIDTH - 250, self.WINDOWHEIGHT))
        self.surf2.fill(self.WHITE)

        for i in range(self.WINDOWHEIGHT):
            Map.map.append([0]*(self.WINDOWWIDTH - 250))

        for i in range(self.WINDOWHEIGHT):
            for j in range(self.WINDOWWIDTH-250):
                Map.map[i][j] = self.circuit.get_at([j,i])

    ## fonction qui gere l'affichage des differents elements du programme
    def draw(self,glob):



        listPosVoiture = []
        self.screen.blit(self.circuit,(0,0))
        self.screen.blit(self.imageBtn,self.rectBtn)

        if glob.listVoiture != []:

            for i in range(len(glob.listVoiture)):

                if glob.listVoiture[i].vivant:
                    ImVoiture = pygame.transform.rotozoom(self.ImVoiture,glob.listVoiture[i].angle,0.05)

                    [x,y]=ImVoiture.get_rect().center

                    listPosVoiture.append([glob.listVoiture[i].pos[0]-x,glob.listVoiture[i].pos[1]-y])

                    self.screen.blit(ImVoiture, listPosVoiture[i])

                    """
                    pygame.draw.circle(self.screen,(255,0,0),glob.listVoiture[i].pos,3)
                    for capt in glob.listVoiture[i].listCapt:
                        if capt.angleCapteur == 0:
                            pygame.draw.line(self.screen,(255,0,0),glob.listVoiture[i].pos,capt.posCapteur)
                        else:
                            pygame.draw.line(self.screen,(0,0,0),glob.listVoiture[i].pos,capt.posCapteur)
                    """
                else:
                    listPosVoiture.append(False)





        for i in range(len(self.listRect)):
            if self.listRect[i].getEtat() == True: pygame.draw.rect(self.screen,(255,127,0), self.listRect[i].getRect())
            else: pygame.draw.rect(self.screen,(0,0,0), self.listRect[i].getRect())

            self.screen.blit(self.listRect[i].getTexte(), self.listRect[i].getRect())

        ########## AFFICHE GENOME ##########################################################

        if self.boolAffGenome == True:
            self.screen.blit(self.surf2,(0,0))

        # Affiche la courbe de progression du score
        if self.boolAffProgression == True:
            pygame.draw.line(self.surf, (0,0,0), (50, self.WINDOWHEIGHT),(50,0), 5)
            pygame.draw.line(self.surf, (0,0,0), (0, self.WINDOWHEIGHT - 20),(self.WINDOWWIDTH - 250, self.WINDOWHEIGHT - 20), 5)

            rectScore = pygame.Rect((70, 20), (100,20))
            rectGen = pygame.Rect((self.WINDOWWIDTH - 350, self.WINDOWHEIGHT - 50), (100,20))

            pygame.draw.rect(self.surf, (255,255,255), rectScore)
            pygame.draw.rect(self.surf, (255,255,255), rectGen)

            self.surf.blit(self.police.render("score" , True, (0,0,0)), rectScore)
            self.surf.blit(self.police.render("generation" , True, (0,0,0)), rectGen)
            absGen = 70
            for i in range(len(glob.listMeilleurScore)):
                pygame.draw.circle(self.surf,(255,0,0),(absGen,int(self.WINDOWHEIGHT - 60 - glob.listMeilleurScore[i] / 5000)),5)
                absGen += 5

            self.screen.blit(self.surf,(0,0))

        self.screen.blit(self.police.render("Reset", True, (255,255,255)),self.rectReset)

        if self.pause == True:
            pygame.draw.rect(self.screen,(0,0,0), self.rectPause)
            self.screen.blit(self.police.render("Play", True, (255,255,255)),self.rectPause)
        else:
            pygame.draw.rect(self.screen,(0,0,0), self.rectPause)
            self.screen.blit(self.police.render("Pause", True, (255,255,255)),self.rectPause)

        pygame.display.update()

        listPosVoiture.clear()

    ## fonction qui quitte la SDL et ferme la fenetre python
    def quitter(self):
        pygame.quit()
        sys.exit()

    ## fonction qui gere les differents evenements SDL: appuie sur une touche, appuie sur un bouton..
    def gestionEvent(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.quitter()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE and self.boolAffProgression == False:
                    self.quitter()
                if event.key == K_ESCAPE and self.boolAffProgression == True:
                        self.boolAffProgression = False

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
                        self.listRect[i].ValiderNouvelleValeur()
                        self.listRect[i].setEtat()

            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if self.rectBtn.collidepoint(event.pos):
                    self.boolAffProgression = True

                for i in range(len(self.listRect)):
                    if self.listRect[i].getEtat() == True: self.listRect[i].setEtat()

                    if self.listRect[i].getRect().collidepoint(event.pos):
                        self.listRect[i].setEtat()

                if self.rectReset.collidepoint(event.pos):
                    self.boolAffGenome = not (self.boolAffGenome)

                if self.rectPause.collidepoint(event.pos) and self.pause == False:
                    self.pause = True

                elif self.rectPause.collidepoint(event.pos) and self.pause == True:
                    for rect in self.listRect:
                        rect.ValiderNouvelleValeur()

                    self.pause = False
                    self.demarrer = True
                    return True

    def text(self,surface,text, x, y,police,size=1, couleur=(0,0,0)):
        text = police.render(text, size,couleur)
        rect = text.get_rect()
        rect.center =(x,y)
        surface.blit(text,rect)


    def drawGenome(self,glob):



        pos = []
        posN = {}
        colc = [0,0,255]
        for connec in glob.gmax.get_listConnexions():
            cin = connec.get_noeudin()
            cout = connec.get_noeudout()

            for n in [cin,cout]:
                if posN.get(n)==None:

                    coln = [100,100,255]
                    if glob.gmax.get_type_noeud(n) == "output":
                        pos = [random.randint(100,900),random.randint(50,100)]

                        coln = [100,255,100]
                    elif glob.gmax.get_type_noeud(n) == "input":
                        pos = [random.randint(100,900),random.randint(550,600)]
                        coln = [255,100,100]
                    elif glob.gmax.get_type_noeud(n) == "bias":
                        pos = [random.randint(700,900),random.randint(400,450)]
                        coln = [100,100,100]
                    else:
                        pos = [random.randint(100,900),random.randint(200,450)]

                    posN.update({n:pos})
                    pygame.draw.circle(self.surf2,coln, pos, 30)
                    self.text(self.surf2,str(n),pos[0],pos[1]+20,self.police)
            if connec.get_poids()<0:
                colc = [255,0,0]
            if connec.get_actif() == False:
                colc = [50,50,50]
            print("cin",cin,"    ",posN.get(cin)," cout",cout,"    ",posN.get(cout))
            colc = [50,50,50]
            pygame.draw.line(self.surf2,(0,0,0),posN.get(cin),posN.get(cout),int(connec.get_poids()*2)+1)
            colc = [50,50,50]
            pygame.draw.line(self.surf2,(0,0,0),posN.get(cout),posN.get(cin),int(connec.get_poids()*2)+1)



    def boucleAff(self, glob):

        while True:
            if self.demarrer == False:
                self.draw(glob)
                demar = self.gestionEvent()
                if demar == True:
                    glob.demarreProgramme()

            else :
                glob.demarreCycle()
                self.drawGenome(glob)
                while glob.arreterCourse() == False:
                    self.draw(glob)
                    self.gestionEvent()
                    if self.pause == False:
                        glob.update_once()
                        self.mainClock.tick(30)


                self.surf2.fill((255,255,255))
                glob.fin_cycle()

        self.quitter()
