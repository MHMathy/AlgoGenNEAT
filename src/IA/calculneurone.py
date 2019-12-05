from .genome import Genome
from .noeudgene import NoeudGene
from .innovation import Innovation
from ProgGlobal.ProgGlobal import ProgGlobal
from collections import OrderedDict
import operator
import math



class CalculNeurone:

    def __init__(self,genome):
        self.genome = genome
        self.listLien = {}
        self.listValeur = {}
        self.setlistLien()


    def setlistLien(self):
        for noeud in self.genome.get_listNoeuds():
            self.listLien.update({str(noeud.get_id()):[]})


        for connec in self.genome.get_listConnections():
            if not(str(connec.get_noeudout()) in self.listLien):
                self.listLien.update({str(connec.get_noeudout()):[]})
            self.listLien[str(connec.get_noeudout())].append([str(connec.get_noeudin()),connec.get_poids()])

       # print (self.listLien)
        tmp = dict(self.listLien)
        for key in tmp:
            tmp[key] = self.calcCoucheNoeud(key,self.listLien)

        tmp = sorted(tmp.items(), key=operator.itemgetter(1))
        for k in OrderedDict(tmp):
            self.listValeur.update({str(k):False})


    def calcValeurNoeud(self,inputVal):
        """
        self.listValeur['5'] = inputVal["vitesse"]
        self.listValeur['6'] = inputVal["angle"]
        self.listValeur['7'] = inputVal["capteur0"]
        self.listValeur['8'] = inputVal["capteur45"]
        self.listValeur['9'] = inputVal["capteur315"]
        self.listValeur['10'] = inputVal["capteur90"]
        self.listValeur['11'] = inputVal["capteur270"]
        self.listValeur['12'] = inputVal["capteur135"]
        self.listValeur['13'] = inputVal["capteur225"]
        self.listValeur['14'] = inputVal["capteur180"]
        """

        self.listValeur['5'] = inputVal["vitesse"]
        self.listValeur['6'] = inputVal["angle"]
        self.listValeur['7'] = inputVal["capteur0"]
        self.listValeur['8'] = inputVal["capteur45"]
        self.listValeur['9'] = inputVal["capteur315"]

        tmp = 0
        for k in OrderedDict(self.listValeur):
            tmp = 0
            if self.listValeur[k] == False:
                for connec in self.listLien[k]:
                    tmp+= (self.listValeur[connec[0]]*connec[1])
                #tmp += 1 #bias
                self.listValeur[k] = CalculNeurone.sigmoid(tmp)
                #print(k,":",self.listValeur[k])
            else:
                continue

        return {"accelerer":self.listValeur['1'],"freiner":self.listValeur['2'],"tourneG":self.listValeur['3'],"tourneD":self.listValeur['4']}


    @staticmethod
    def calcCoucheNoeud(index,liste):
        if liste[index]==[]:
            return 1
        else:
            tmp = []
            for pair in liste[index]:
                #print(pair)
                tmp.append(CalculNeurone.calcCoucheNoeud(pair[0],liste))
            return 1+max(tmp)

    @staticmethod
    def sigmoid(x):
      return 1/(1 + ProgGlobal.Cons.get("COEF_EXPO")*math.exp(-round(x,5)))

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

        val = {"vitesse":10,"angle": 10,"c_0": 100}

        cn.setlistLien()
        cn.calcValeurNoeud(val)
#CalculNeurone.testRegression()
