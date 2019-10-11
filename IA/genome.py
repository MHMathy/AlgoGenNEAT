from noeudgene import NoeudGene
from connectiongene import ConnectionGene
import random

class Genome:
    def __init__(self):
        self.__listConnections = []
        self.__listNoeuds = []
        self.__numInnovation = 0

    def init_Innovation(self):
        tmp = self.__listConnections.copy()
        tmp.reverse()
        self.__numInnovation = tmp[0].__numInnovation

    def new_numInnovation(self):
        self.__numInnovation += 1
        return self.__numInnovation

    def ajout_connec(self,connection):
        self.__listConnections.append(connection)

    def ajout_noeud(self,noeud):
        self.__listNoeuds.append(noeud)

    def get_listNoeuds(self):
        return self.__listNoeuds

    def get_listConnections(self):
        return self.__listConnections

    def get_noeud(self,id):
        for noeud in self.__listNoeuds:
            if noeud.get_id() == id:
                return noeud

    def get_numInnovation():
        return self.__numInnovation


    def ajout_connec_mutation(self):
        noeud = []
        while True:
            noeud = random.sample(self.__listNoeuds,2) #noeud tire au hazard
            if noeud[0].get_type() != noeud[1].get_type():
                break

        inverse = False

        #if (noeud[0].get_type() == 'hidden' and noeud[1].get_type() == 'input') or (noeud[0].get_type() == 'output' and noeud[1].get_type() == 'hidden') or (noeud[0].get_type() == 'output' and noeud[1].get_type() == 'input'):

        if noeud[0].get_type() == 'hidden' and noeud[1].get_type() == 'input':
            inverse = True
        elif noeud[0].get_type() == 'output' and noeud[1].get_type() == 'hidden':
            inverse = True
        elif noeud[0].get_type() == 'output' and noeud[1].get_type() == 'input':
            inverse = True

        noeud.sort(reverse=inverse)

        connecExist = False
        for connec in self.__listConnections:
            if connec.get_noeudin() == noeud[0].get_id() and connec.get_noeudout() == noeud[1].get_id():
                connecExist = True
                break

        if connecExist == True:
            return

        #break

        newConnec = ConnectionGene(noeud[0].get_id(),noeud[1].get_id(),1,True,self.new_numInnovation()) #incrementer de 1 l'innovatino et garder la trace

        #if inverse == False:
            #new_connec = ConnectionGene(noeud[0],noeud[1],poids,True,innovation) #incrementer de 1 l'innovatino et garder la trace

        #if inverse == True:
            #new_connec = ConnectionGene(noeud[1],noeud[0],poids,True,innovation)

        self.ajout_connec(newConnec)

    def ajout_noeud_mutation(self):
        connec = random.choice(self.__listConnections)
        noeudin = get_noeud(connec.__noeudin)
        noeudout = get_noeud(connec.__noeudout)

        connec.deactive()

        newNoeud = NoeudGene("hidden",len(__listNoeuds))

        coInNew = ConnectionGene(noeudin.get_id(),newnoeud.get_id(),1,True,self.new_numInnovation())
        coNewOut = ConnectionGene(newnoeud.get_id(),noeudout.get_id(),connec.get_poids(),True,self.new_numInnovation())

        self.ajout_noeud(newnoeud)

        self.ajout_connec(c)
        self.ajout_connec(co_new_out)

    def melange_genome(self,genParent1,genParent2):

        newGenome = Genome()

        for noeudp1 in genParent1.get_listNoeuds():
            newGenome.ajout_noeud(noeudp1.copy_noeud())

        for i in range(0,genParent1.get_numInnovation()):
            connectemp = []
            for connecp1 in genParent1.get_listConnections():
                if connecp1.get_innovation()==i:
                    connectemp.append(connecp1.copy_connec())
            for connecp2 in genParent2.get_listConnections():
                if connecp2.get_innovation()==i:
                    connectemp.append(connecp2.copy_connec())
            if len(connectemp)==0:
                continue
            else:
                newGenome.ajout_connec(random.choice(connectemp))

        return newGenome
