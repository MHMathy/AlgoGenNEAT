from .genome import Genome
from .noeudgene import NoeudGene
from Outil.outil import Innovation
from Outil.outil import Constantes
from collections import OrderedDict
import operator
import math
import numpy as np



## classe CalculNeuronne qui va se charger de calculer la valeur de sortie de chaque neurone pour obtenir les valeurs de sortie
#
class CalculNeurone:

    ## contructeur qui assigne un genome et établie un lien entre chaque neurone
    def __init__(self,genome):
        self.genome = genome
        self.listLien = {}
        self.listValeur = {}
        self.setlistLien()

    ## fonction qui va retourner une liste indiquant tout les dépandances entre les neurones
    # pour toutes connections vers un neurone, on retient qu'il aura besoin de chaque neurone en entrée
    def setlistLien(self):
        for noeud in self.genome.get_listNoeuds():
            self.listLien.update({str(noeud.get_id()):[]})


        for connec in self.genome.get_listConnexions():
            if not(str(connec.get_noeudout()) in self.listLien):
                self.listLien.update({str(connec.get_noeudout()):[]})
            if connec.get_actif():
                self.listLien[str(connec.get_noeudout())].append([str(connec.get_noeudin()),connec.get_poids()])


        tmp = dict(self.listLien)
        for key in tmp:
            tmp[key] = self.calcCoucheNoeud(key,self.listLien)

        tmp = sorted(tmp.items(), key=operator.itemgetter(1))
        for k in OrderedDict(tmp):
            self.listValeur.update({str(k):False})


    ## fonction qui va calculer la valeur de chaques neurones on fonction des neurones dont il dépend
    # @param prend en entrée les valeurs fournie par la voiture
    def calcValeurNoeud(self,inputVal):
        for k in OrderedDict(self.listValeur):
            self.listValeur[k] = False

        # les valeurs d'entrée sont assigné
        self.listValeur['3'] = inputVal["vitesse"]
        self.listValeur['4'] = inputVal["capteur0"]
        self.listValeur['5'] = inputVal["capteur45"]
        self.listValeur['6'] = inputVal["capteur315"]
        self.listValeur['7'] = inputVal["capteur90"]
        self.listValeur['8'] = inputVal["capteur270"]
        self.listValeur['9'] = inputVal["capteur135"]
        self.listValeur['10'] = inputVal["capteur225"]
        self.listValeur['11'] = inputVal["capteur180"]

        tmp = 0
        for k in OrderedDict(self.listValeur):
            tmp = 0
            if self.listValeur[k] == False:
                # pour chaques neurones sans valeur on cherche les valeurs dont il dépend grace lisrLien
                # et
                for connec in self.listLien[k]:
                    tmp+= (self.listValeur[connec[0]]*connec[1])
                #tmp += 1 #bias  ###########################################################################################
                self.listValeur[k] = CalculNeurone.sigmoid(tmp)

            else:
                continue


        return {"acc/fre":self.listValeur['1'],"D/G":self.listValeur['2']}

    ## cherche à déterminer les dépendances d'un seul neurone
    @staticmethod
    def calcCoucheNoeud(index, liste):
        if liste[index] == []:
            return 1
        else:
          tmp = 0
          for pair in liste[index]:
              ind = 0
              while ind < int(index):
                  if 1 + int(max(liste)) > tmp:
                     tmp = 1 + int(max(liste))
                  ind += 1
          return tmp

    ## fonciton sigmoid pour calculer la sortie à partir de la somme des valeurs
    @staticmethod
    def sigmoid(x):

        if x < 0:
             return 1 - 1/(1 + np.exp(x))

        else :
            return 1/(1 + np.exp(-x))

    @staticmethod
    def testRegression():

        G1 = Genome()
        l = []
        """
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("output",Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("output",Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("output",Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("output",Innovation.get_new_innovation_noeud()))
        """

        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("output",Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("output",Innovation.get_new_innovation_noeud()))
        for n in l:
            G1.ajout_noeud(n)

        for i in range(0,6):
            G1.ajout_connec_mutation()

        for i in range(0,2):
            G1.ajout_noeud_mutation()
        for i in range(0,6):
            G1.ajout_connec_mutation()
        G1.connec_mutation()
        cn = CalculNeurone(G1)

        val = {"vitesse":7,"capteurDif": 150,"capteur0": 100}

        cn.setlistLien()
        cn.calcValeurNoeud(val)
#CalculNeurone.testRegression()
