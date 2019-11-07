from .noeudgene import NoeudGene
from .connectiongene import ConnectionGene
import random

class Genome:
    def __init__(self):
        self.__listConnections = []
        self.__listNoeuds = []

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

    def get_numInnovation(self):
        if not self.__listConnections:
            return 0
        else:
            return self.__listConnections[-1].get_innovation()

    def get_idNoeudFin(self):
        if not self.__listNoeuds:
            return 0
        else:
            return self.__listNoeuds[-1].get_id()


    def ajout_connec_mutation(self):
        noeud = []
        while True:
            noeud = random.sample(self.__listNoeuds,2) #noeud tire au hazard
            if not(noeud[0].get_type() == noeud[1].get_type() and (noeud[0].get_type() == "input" or noeud[0].get_type() == "output")):
                break

        inverse = False

        #if (noeud[0].get_type() == 'hidden' and noeud[1].get_type() == 'input') or (noeud[0].get_type() == 'output' and noeud[1].get_type() == 'hidden') or (noeud[0].get_type() == 'output' and noeud[1].get_type() == 'input'):

        if noeud[0].get_type() == "hidden" and noeud[1].get_type() == "input":
            inverse = True
        elif noeud[0].get_type() == "output" and noeud[1].get_type() == "hidden":
            inverse = True
        elif noeud[0].get_type() == "output" and noeud[1].get_type() == "input":
            inverse = True

        if inverse:
            noeud.reverse()

        connecExist = False
        for connec in self.__listConnections:
            if connec.get_noeudin() == noeud[0].get_id() and connec.get_noeudout() == noeud[1].get_id():
                connecExist = True
                break

        if connecExist == True:
            return

        #break

        newConnec = ConnectionGene(noeud[0].get_id(),noeud[1].get_id(),1,True,self.get_numInnovation()+1) #incrementer de 1 l'innovatino et garder la trace

        #if inverse == False:
            #new_connec = ConnectionGene(noeud[0],noeud[1],poids,True,innovation) #incrementer de 1 l'innovatino et garder la trace

        #if inverse == True:
            #new_connec = ConnectionGene(noeud[1],noeud[0],poids,True,innovation)

        self.ajout_connec(newConnec)

    def ajout_noeud_mutation(self):
        connec = random.choice(self.__listConnections)
        noeudin = self.get_noeud(connec.get_noeudin())
        noeudout = self.get_noeud(connec.get_noeudout())

        connec.deactive()

        newNoeud = NoeudGene("hidden",self.get_idNoeudFin()+1)

        coInNew = ConnectionGene(noeudin.get_id(),newNoeud.get_id(),1,True,self.get_numInnovation()+1)
        coNewOut = ConnectionGene(newNoeud.get_id(),noeudout.get_id(),connec.get_poids(),True,self.get_numInnovation()+2)

        self.ajout_noeud(newNoeud)

        self.ajout_connec(coInNew)
        self.ajout_connec(coNewOut)

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

    @staticmethod
    def testRegression():
    
        print("initialisation du genome")
        G = Genome()
        if G.get_listNoeuds() != [] or G.get_listConnections() != []:
            print("echec de l'initialisation du genome") 
            return -1
        print("initialisation reussie")

        l = []

        l.append(NoeudGene("input", 1))
        l.append(NoeudGene("output",2))

        for ind in l:
            G.ajout_noeud(ind)
        
        if len(G.get_listNoeuds()) != 2: 
            print("probleme lors de l'ajout d'un noeud")
            return -1
        print("tous les noeuds ont ete ajoute")

        for i in range(0,1):
            G.ajout_connec_mutation()

        if len(G.get_listConnections()) != 1:
            print("probleme lors de la creation de la connection entre les deux noeuds")
            return -1
        print("la connection a ete ajoute")

        G.ajout_noeud_mutation()

        if len(G.get_listConnections()) != 3 or len(G.get_listNoeuds()) != 3:
            print("erreur lors de l'ajout d'un noeud de mutation")
            print("taille listConnections:", len(G.get_listConnections()), " devrait etre egale a 3")
            print("taille listNoeuds: ", len(G.get_listNoeuds()), "devrait etre egale a 3")
            return -1
        print("le noeud de mutation a ete ajoute")
        print("fin du test de regression, passe avec succes")

Genome.testRegression()

        





        
