from .noeudgene import NoeudGene
from .connectiongene import ConnectionGene
from .innovation import Innovation
import random


# classe contenant une liste de noeuronnes sous le nom de noeud et une liste de connection entre les noeuds
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

    # ajouter une connection à la liste de connection
    def ajout_connec(self,connection):
        self.__listConnections.append(connection)

    # ajouter un noeud à la liste de noeud
    def ajout_noeud(self,noeud):
        self.__listNoeuds.append(noeud)

    # retourne la liste de noeud
    def get_listNoeuds(self):
        return self.__listNoeuds

    # retourne la liste de connections
    def get_listConnections(self):
        return self.__listConnections

    # retourne un noeud à partir de son numero id
    def get_noeud(self,id):
        for noeud in self.__listNoeuds:
            if noeud.get_id() == id:
                return noeud

    # retourne le numero d'innovation max de la liste de connection
    def get_maxNumInnovation(self):
        maxinno = 0
        for connec in self.__listConnections:
            if connec.get_innovation>maxinno:
                maxinno=connec.get_innovation()
        return maxinno

    # a supprimer?
    # retourne le numero d'innovation max des noeuds
    def get_idNoeudFin(self):
        if not self.__listNoeuds:
            return 0
        else:
            return self.__listNoeuds[-1].get_id()

    # modifie la valeur
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
    def count_match_exces_disjoint(genParent1, genParent2):
        matchParents = 0
        exces = 0
        disjoint = 0
        moyennePoids = 0

        # on trouve le numero d'innovation max de chaque parent
        MaxInnovationParent1 = genParent1.get_maxNumInnovation()
        MaxInnovationParent2 = genParent2.get_maxNumInnovation()

        #on recupere le numero d'innovation max entre les deux precedents
        MaxInno = max(MaxInnovationParent1, MaxInnovationParent2)

        #on initialise deux listes contenant que des 0
        ListeGenParent1 = [0] * MaxInnovationParent1
        ListeGenParent2 = [0] * MaxInnovationParent2

        #on trie les numeros d'innovation dans la liste par ordre croissant, en laissant la valeur 0
        #en cas d'absence de connection
        for i in genParent1.get_listConnections():
            ListeGenParent1[i.get_innovation() - 1] = i

        for i in genParent2.get_listConnections() :
            ListeGenParent2[i.get_innovation() - 1] = i

        #on incremente les differentes variables selon les places des numeros d'innovation dans les listes
        for i in range (0, MaxInno):
            if ListeGenParent1[i].get_innovation() == ListeGenParent2[i].get_innovation():
                matchParents += 1
                moyennePoids += abs(ListeGenParent1[i].get_poids() - ListeGenParent2[i].get_poids())

            elif ListeGenParent1[i].get_innovation() == 0 and ListeGenParent2[i].get_innovation() != 0 and i < MaxInnovationParent1:
                disjoint += 1

            elif ListeGenParent1[i].get_innovation() =! 0 and ListeGenParent2[i].get_innovation() == 0:
                disjoint += 1

            elif ListeGenParent2[i].get_innovation() == i and i > MaxInnovationParent1 :
                exces += 1

        moyennePoids /= matchParents
        return moyennePoids,exces,disjoint

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


    @staticmethod
    def calc_distance_compatibilite(genome1,genome2):
        (m,e,d) = count_moyen_exces_disjoint(genome1,genome2)
        return (DISTANCE_C1*e/1)+ (DISTANCE_C2*d/1) + DISTANCE_C3*m

Genome.testRegression()
