from .noeudgene import NoeudGene
from .connectiongene import ConnectionGene
from .innovation import Innovation
import random



class Genome:

    PROBA_MUTATION = 80
    PROBA_MUTATION_COEF = 90
    DISTANCE_C1 = 1
    DISTANCE_C2 = 1
    DISTANCE_C3 = 1
    ino = Innovation()

    def __init__(self,innovationG):
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

    def connec_mutation(self):
        for connec in self.__listConnections:
            if (random.randint(1,100)<PROBA_MUTATION):
                if(random.randint(1,100)<PROBA_MUTATION_COEF):
                    connec.set_poids(connec.get_poids()*random.uniform(-2,2))
                else:
                    connec.set_poids(random.uniform(-2,2))

    def ajout_connec_mutation(self):
        noeud = []
        while True:
            noeud = random.sample(self.__listNoeuds,2) #noeud tire au hazard
            if not(noeud[0].get_type() == noeud[1].get_type() and (noeud[0].get_type() == "input" or noeud[0].get_type() == "output")):
                break

        inverse = False

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

        newConnec = ConnectionGene(noeud[0].get_id(),noeud[1].get_id(),1,True,Innovation.get_new_innovation_connec(noeud[0].get_id(),noeud[1].get_id())) #incrementer de 1 l'innovatino et garder la trace

        self.ajout_connec(newConnec)

    def ajout_noeud_mutation(self):
        connec = random.choice(self.__listConnections)
        noeudin = self.get_noeud(connec.get_noeudin())
        noeudout = self.get_noeud(connec.get_noeudout())

        connec.deactive()

        newNoeud = NoeudGene("hidden",ino.get_new_innovation_noeud())

        coInNew = ConnectionGene(noeudin.get_id(),newNoeud.get_id(),1,True,Innovation.get_new_innovation_connec(noeudin.get_id(),newNoeud.get_id()))
        coNewOut = ConnectionGene(newNoeud.get_id(),noeudout.get_id(),connec.get_poids(),True,Innovation.get_new_innovation_connec(newNoeud.get_id(),noeudout.get_id()))

        self.ajout_noeud(newNoeud)

        self.ajout_connec(coInNew)
        self.ajout_connec(coNewOut)

    @staticmethod
    def melange_genome(genParent1,genParent2):
        #+vite si copie et pop
        newGenome = Genome()
        noeudtemp = []
        connectemp = []
        fini = False
        while not fini:
            for noeudp1 in genParent1.get_listNoeuds():
                newGenome.ajout_noeud(noeudp1.copy_noeud())

        while not fini:

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

        @staticmethod
        def calc_distance_compatibilite(genome1,genome2):

        @staticmethod
        def count_match_exces_disjoint(genome1,genome2):

        @staticmethod
        def calc_distance_compatibilite(genome1,genome2):
