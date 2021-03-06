import math
import time
from Capteur.capteur import Capteur
from IA.genome import Genome
from IA.calculneurone import CalculNeurone



## documentation de la classe voiture:
# gere tous les evenements lies a une voiture, ainsi que tous ses parametres
class Voiture:
    ## variable commune a toutes les voitures, qui est une liste de capteurs "checkpoints" presents sur
    # le circuit
    listeCapteursCircuit = [(182,130), (525,197), (715, 295), (795,447), (525, 540), (265, 520),(330,360),(220,280)]

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

        self.nbTour = 0

        ## temps de vie de la voiture
        self.dureeVie = 0

        ## etat vivant
        self.vivant = True

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
        if self.vitesse < 8:
            self.vitesse += 1.5
        else:
            self.vitesse = 5

    ## fonction qui gere la deceleration de la voiture
    def freiner(self): #reduit la vitesse
        if self.vitesse> -3:
            self.vitesse -= 1.2
        else:
            self.vitesse = -3

    ## fonction qui permet de faire tourner a gauche la voiture
    def tourne_gauche(self): #permet d'actionner le volant de la voiture pour donner l'ordre de tourner à gauche
        if self.volant<3:
            self.volant += 1 #* (self.vitesse**(1/2) - self.vitesse*0.25)


    ## fonction qui permet de faire tourner a gauche la voiture
    def tourne_droite(self): #permet d'actionner le volant de la voiture pour donner l'ordre de tourner à droite
        if self.volant>(-3):
            self.volant -=  1

    ## fonction qui met a jour les parametres de la voiture et ses capteurs
    def update(self,duree): #met à jour les paramètres de la voiture (et ses capteurs)
       for capt in self.listCapt:
           capt.setPosActuVoiture(self.pos)
           capt.checkMur()
       self.checkCollisionMur()
       if self.vivant == True:
           self.dureeVie = duree

           valSortie = self.calcNeuro.calcValeurNoeud(self.get_valeurs_pour_reseau())

           if valSortie.get("acc/fre")>0.8:
               self.accelerer()

           elif valSortie.get("acc/fre")<0.6:
               self.freiner()

           if valSortie.get("D/G")>0.8 and self.vitesse != 0:
               self.tourne_droite()
           elif valSortie.get("D/G")<0.2 and self.vitesse != 0:
               self.tourne_gauche()


           self.angle += self.volant
           dx = math.cos(math.radians(self.angle))
           dy = math.sin(math.radians(self.angle))
           self.pos = (self.pos[0] + dx*self.vitesse, self.pos[1] - dy*self.vitesse)
           self.pos = [int(self.pos[0]),int(self.pos[1])]

           for capt in self.listCapt:
               capt.posActuVoiture = self.pos
               capt.angleVoiture = self.angle


           if self.capteurCourant != 7:
               self.capteurSuivant = self.capteurCourant + 1

           else:
               self.capteurSuivant = 0

           self.distCapteurCourant = self.calculDistance(self.pos, self.listeCapteursCircuit[self.capteurCourant])
           self.distCapteurSuivant = self.calculDistance(self.pos, self.listeCapteursCircuit[self.capteurSuivant])

           if self.distCapteurSuivant < 75:
               if self.capteurCourant == 7:
                   self.nbTour += 1
                   self.capteurCourant = 0

               else: self.capteurCourant += 1

           if self.dureeVie > 1.5 and self.pos == [200,150]:
               self.meurt()



    def meurt(self):
        self.vivant = False

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

        if self.vivant == False:
            self.scoreVoiture /=2

        self.scoreVoiture #*= self.dureeVie

        if self.nbTour > 0:
            self.scoreVoiture += (self.scoreTourComplet() * self.nbTour)
        print(self.nbTour)
        return int(self.scoreVoiture)

    ## fonction qui calcul la distance entre deux points
    # @param ptA  premier point
    # @param ptB un second point
    def calculDistance(self, ptA, ptB):
        return math.sqrt(math.pow(ptA[0]-ptB[0],2)+math.pow(ptA[1]-ptB[1],2))

    ## fonction qui retourne un dictionnaire comportant toutes les valeurs de la voiture a evaluer par le reseau de neuronnes
    def get_valeurs_pour_reseau(self):

        return { "vitesse":self.vitesse,
                 #"volant":self.volant,
                 "capteur0":self.listCapt[0].getDistCapteur(),
                 "capteur45":self.listCapt[1].getDistCapteur(),
                 "capteur315":self.listCapt[7].getDistCapteur(),
                 "capteur90":self.listCapt[2].getDistCapteur(),
                 "capteur270":self.listCapt[6].getDistCapteur(),
                 "capteur135":self.listCapt[3].getDistCapteur(),
                 "capteur225":self.listCapt[5].getDistCapteur(),
                 "capteur180":self.listCapt[4].getDistCapteur() }


    def checkCollisionMur(self):
        listeTmp = self.getDistRetourCapt()

        if ((listeTmp.index(min(listeTmp)) in [1,2,3,5,6,7]) and min(listeTmp) < 11) or ((listeTmp.index(min(listeTmp)) in [0,4]) and min(listeTmp) < 20):
            self.meurt()

    def scoreTourComplet(self):
        res = 0
        for i in range(len(self.listeCapteursCircuit) - 1):
            res += self.calculDistance(self.listeCapteursCircuit[i], self.listeCapteursCircuit[i+1])

        res += self.calculDistance(self.listeCapteursCircuit[6], self.listeCapteursCircuit[0])

        return res
