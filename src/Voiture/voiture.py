import math
import sys
import time
from Capteur.capteur import Capteur
from IA.genome import Genome
from IA.calculneurone import CalculNeurone



## documentation de la classe voiture:
# gere tous les evenements lies a une voiture, ainsi que tous ses parametres
class Voiture:
    ## variable commune a toutes les voitures, qui est une liste de capteurs "checkpoints" presents sur
    # le circuit
    listeCapteursCircuit = [(182,130), (525,197), (715, 295), (795,447), (525, 510), (282, 490),(395,346),(235,280)]

    ## constructeur de la classe qui initialise toutes les variables d'une voiture
    def __init__(self, genome, posx=0,posy=0,angle=0,volant=0,vitesse=0): #initialisation de la voiture
        ## position de la voiture
        self.pos = [posx,posy]

        ## angle de la voiture
        self.angle = angle

        ## volant de la voiture
        self.volant = volant

        ## vitesse de la voiture
        self.vitesse = vitesse

        ## liste des capteurs de la voiture
        self.listCapt = []

        ## instant auquel la voiture a ete cree
        self.debutTemps = time.time()

        ## temps de vie de la voiture
        self.dureeVie = 0

        ## capteur circuit auquel est actuellement la voiture
        self.capteurCourant = 0

        ## prochain capteur circuit que doit atteindre la voiture
        self.capteurSuivant = 1

        ## score de la voiture
        self.scoreVoiture = 0

        ## distance par rapport au capteur circuit courant
        self.distCapteurCourant = 0

        ## distance par rapport au prochain capteur circuit
        self.distCapteurSuivant = 0

        self.genome = genome

        self.calcNeuro = CalculNeurone(self.genome)

        angleCapt = 0
        for i in range(0,8): #disposition des capteurs dans une liste selon le sens trigonometrique
            self.listCapt.append(Capteur(angleCapt))
            angleCapt += 45

    ## fonction qui gere l'acceleration de la voiture
    def accelerer(self): #augmente la vitesse
        self.vitesse += 1.5

    ## fonction qui gere la deceleration de la voiture
    def freiner(self): #reduit la vitesse
        self.vitesse -= 1.2

    ## fonction qui permet de faire tourner a gauche la voiture
    def tourne_gauche(self): #permet d'actionner le volant de la voiture pour donner l'ordre de tourner à gauche
        if self.volant<10:
            self.volant += 1

    ## fonction qui permet de faire tourner a gauche la voiture
    def tourne_droite(self): #permet d'actionner le volant de la voiture pour donner l'ordre de tourner à droite
        if self.volant>-10:
            self.volant -= 1

    ## fonction qui permet a la voiture d'arreter de tourner/avancer progressivement
    def retour_neutre(self):
        if self.vitesse > -1 and self.vitesse < 1:
            self.vitesse = 0
        else:
            self.vitesse += (-1*self.vitesse)/abs(self.vitesse)

        if self.volant!=0:
                self.volant += (-0.5*self.volant)/abs(self.volant)

    ## fonction qui met a jour les parametres de la voiture et ses capteurs
    def update(self): #met à jour les paramètres de la voiture (et ses capteurs)
        self.angle += self.volant
        dx = math.cos(math.radians(self.angle))
        dy = math.sin(math.radians(self.angle))
        self.pos = (self.pos[0] + dx*self.vitesse, self.pos[1] - dy*self.vitesse)
        self.retour_neutre()

        Capteur.PosActuVoiture = self.pos
        Capteur.AngleVoiture = self.angle
        for i in range(0,8):
            self.listCapt[i].checkMur()

        self.dureeVie = int((time.time() - self.debutTemps)*1000)


        if self.capteurCourant != 7:
            self.capteurSuivant = self.capteurCourant + 1
        else: capteurSuivant = 0

        self.distCapteurCourant = self.calculDistance(self.pos, self.listeCapteursCircuit[self.capteurCourant])
        self.distCapteurSuivant = self.calculDistance(self.pos, self.listeCapteursCircuit[self.capteurSuivant])

        if self.distCapteurCourant > 50 and self.distCapteurSuivant < 50:
            if self.capteurCourant == 7:
                self.capteurCourant = 0

            else: self.capteurCourant += 1

        self.calcNeuro.setlistLien()
        self.calcNeuro.calcValeurNoeud(self.getValeursPourReseau())


    ## fonction qui retourne la position de la voiture
    def getPos(self): #renvoie la position de la voiture
        return self.pos

    ## fonction qui retourne l'angle de la voiture
    def getAngle(self): #renvoie l'angle d'inclinaison de la voiture
        return self.angle

    ## fonction qui retourne une liste comportant toutes les distances auxquelles les capteurs detetectent un mur
    def getDistRetourCapt(self): #renvoie une liste comportant la distance de chaque capteurs par rapport au mur le plus proche
        listTmp = [0,0,0,0,0,0,0,0]
        for i in range(0,8):
            listTmp[i] = self.listCapt[i].getDistCapteur()
        return listTmp

    ## fonction qui calcul le score de la voiture en fonction de la distance qu'elle a parcouru et du temps qu'elle a survecu
    def calculScore(self): #calcul et retourne le score atteint par la voiture au terme de sa vie

        for i in range(0, self.capteurCourant):
            self.scoreVoiture += self.calculDistance(self.listeCapteursCircuit[i], self.listeCapteursCircuit[i+1])

        self.scoreVoiture += self.calculDistance(self.listeCapteursCircuit[self.capteurCourant],self.listeCapteursCircuit[self.capteurSuivant])- self.calculDistance(self.pos, self.listeCapteursCircuit[self.capteurSuivant])

        scoreDebug = self.scoreVoiture
        self.scoreVoiture *= self.dureeVie
        self.scoreVoiture /= 10

        return int(self.scoreVoiture)

    ## fonction qui calcul la distance entre deux points
    # @param ptA  premier point
    # @param ptB un second point
    def calculDistance(self, ptA, ptB):
        return math.sqrt(math.pow(ptA[0]-ptB[0],2)+math.pow(ptA[1]-ptB[1],2))

    ## fonction qui retourne un dictionnaire comportant toutes les valeurs de la voiture a evaluer par le reseau de neuronnes
    def getValeursPourReseau(self):
        return { "vitesse":self.vitesse,
                 "angle":self.angle,
                 "capteur0":self.listCapt[0].getDistCapteur(),
                 "capteur45":self.listCapt[1].getDistCapteur(),
                 "capteur315":self.listCapt[7].getDistCapteur(),
                 "capteur90":self.listCapt[2].getDistCapteur(),
                 "capteur270":self.listCapt[6].getDistCapteur(),
                 "capteur135":self.listCapt[3].getDistCapteur(),
                 "capteur225":self.listCapt[5].getDistCapteur(),
                 "capteur180":self.listCapt[4].getDistCapteur() }
