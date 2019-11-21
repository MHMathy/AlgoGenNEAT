from .noeudgene import NoeudGene
from .connectiongene import ConnectionGene
from .innovation import Innovation
import random


# classe contenant une liste de noeuronnes sous le nom de noeud et une liste de connection entre les noeuds
## classe qui gere les noeuronnes sous forme de liste de noeuds et liste de connections
class Genome:

    PROBA_MUTATION = 80
    PROBA_MUTATION_COEF = 90
    DISTANCE_C1 = 0.3
    DISTANCE_C2 = 0.3
    DISTANCE_C3 = 0.3

    ## constructeur qui initialise les deux listes de la classe comme etant des listes vides
    def __init__(self):
        self.__listConnections = []
        self.__listNoeuds = []

    # ajouter une connection à la liste de connection
    ## fonction qui ajoute une connection dans la liste
    # @param connection Connection a ajoute dans la liste
    def ajout_connec(self,connection):
        self.__listConnections.append(connection)

    # ajouter un noeud à la liste de noeud
    ## fonction qui ajoute un noeud dans la liste
    # @param noeud Noeud a ajoute dans la liste
    def ajout_noeud(self,noeud):
        self.__listNoeuds.append(noeud)

    # retourne la liste de noeud
    ## fonction qui retourne la liste des noeuds du genome
    def get_listNoeuds(self):
        return self.__listNoeuds

    # retourne la liste de connections
    ## fonction qui retourne la liste des connections du genome
    def get_listConnections(self):
        return self.__listConnections

    # retourne un noeud à partir de son numero id
    ## fonction qui retourne un noeud en fonction de son ID
    # @param id ID du noeud a chercher
    def get_noeud(self,id):
        for noeud in self.__listNoeuds:
            if noeud.get_id() == id:
                return noeud

    ## fonction qui retourne une connection en fonction de son ID
    # @param id ID de la connection a chercher    
    def get_connection(self,id):
        for connec in self.__listConnections:
            if connec.get_innovation() == id:
                return connec

    # retourne le numero d'innovation max de la liste de connection
    ## fonction qui retourne le numero d'innovation le plus elever dans la liste
    def get_maxNumInnovation(self):
        maxinno = 0
        for connec in self.__listConnections:
            if connec.get_innovation()>maxinno:
                maxinno=connec.get_innovation()
        return maxinno

    ## fonction qui remplace une connection dans la liste
    # @param newConnec Connection qui remplacera la precedente dans la liste
    def remplace_connec(self,newConnec):
        for connec in self.__listConnections:
            if connec.get_innovation() == newConnec.get_innovation():
                connec = newConnec

    # modifie la valeur
    ## fonction qui gere la mutation d'une connection
    def connec_mutation(self):
        for connec in self.__listConnections:
            if (random.randint(1,100)<Genome.PROBA_MUTATION):
                if(random.randint(1,100)<Genome.PROBA_MUTATION_COEF):
                    connec.set_poids(connec.get_poids()*random.uniform(-2,2))
                else:
                    connec.set_poids(random.uniform(-2,2))

    ## fonction qui ajoute une connection a une mutation
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

        #incrementer de 1 l'innovation et garder la trace
        newConnec = ConnectionGene(noeud[0].get_id(),noeud[1].get_id(),1,True,Innovation.get_new_innovation_connec(noeud[0].get_id(),noeud[1].get_id()))

        self.ajout_connec(newConnec)

    ## fonction qui ajoute un noeud a une mutation
    def ajout_noeud_mutation(self):
        connec = random.choice(self.__listConnections)
        noeudin = self.get_noeud(connec.get_noeudin())
        noeudout = self.get_noeud(connec.get_noeudout())

        connec.deactive()

        newNoeud = NoeudGene("hidden",Innovation.get_new_innovation_noeud())

        coInNew = ConnectionGene(noeudin.get_id(),newNoeud.get_id(),1,True,Innovation.get_new_innovation_connec(noeudin.get_id(),newNoeud.get_id()))
        coNewOut = ConnectionGene(newNoeud.get_id(),noeudout.get_id(),connec.get_poids(),True,Innovation.get_new_innovation_connec(newNoeud.get_id(),noeudout.get_id()))

        self.ajout_noeud(newNoeud)

        self.ajout_connec(coInNew)
        self.ajout_connec(coNewOut)

    ## fonction qui renvoie une genome qui est le melange de deux autres genomes
    # @param genParent1 1er parent du genome qui sera retourne
    # @param genParent2 2eme parent du genome qui sera retourne
    @staticmethod
    def melange_genome(genParent1,genParent2):
        #+vite si copie et pop
        newGenome = Genome()
        noeudtemp = []
        connectemp = []

        # ce sera pas dans l'ordre donc bouge toi le cul si ça te trigger
        for noeudp1 in genParent1.get_listNoeuds():
            noeudtemp.append(noeudp1.get_id())
            newGenome.ajout_noeud(noeudp1.copy_noeud())

        for noeudp2 in genParent2.get_listNoeuds():
            if noeudp2.get_id() in noeudtemp:
                continue
            newGenome.ajout_noeud(noeudp2.copy_noeud())



        for connecp1 in genParent1.get_listConnections():
            connectemp.append(connecp1.get_innovation())
            newGenome.ajout_connec(connecp1.copy_connec())


        for connecp2 in genParent2.get_listConnections():
            if connecp2.get_innovation() in connectemp:
                if random.choice([True,False]) == True:
                    newGenome.remplace_connec(connecp2.copy_connec())
            else:
                newGenome.ajout_connec(connecp2.copy_connec())

        return newGenome

    #fonction qui renvoie le poids moyen des connections, le nombre d'exces et le nombre de disjoints
    ## fonction qui renvoie le poids moyen des connections, le nombres de noeuds en exces et le nombres de noeuds "decaler" dans la liste entre les deux parents
    # @param genParent1 1er genome a evaluer
    # @param genParent2 2eme genome a evaluer
    @staticmethod
    def count_moyenne_exces_disjoint(genParent1, genParent2):
        matchParents = 0
        exces = 0
        disjoint = 0
        moyennePoids = 0

        #on trouve le numero d'innovation max de chaque parent
        MaxInnovationParent1 = genParent1.get_maxNumInnovation()
        MaxInnovationParent2 = genParent2.get_maxNumInnovation()

        #on recupere le numero d'innovation max entre les deux precedents
        MaxInno = max(MaxInnovationParent1, MaxInnovationParent2)

        #on initialise deux listes contenant que des 0
        ListeGenParent1 = [0] * MaxInno
        ListeGenParent2 = [0] * MaxInno

        #on trie les numeros d'innovation dans la liste par ordre croissant, en laissant la valeur 0
        #en cas d'absence de connection
        for connec in genParent1.get_listConnections():
            ListeGenParent1[connec.get_innovation() - 1] = connec

        for connec in genParent2.get_listConnections() :
            ListeGenParent2[connec.get_innovation() - 1] = connec

        #on incremente les differentes variables selon les places des numeros d'innovation dans les listes
        for i in range (0, MaxInno):
            if ListeGenParent1[i] != 0 and ListeGenParent2[i] != 0 and ListeGenParent1[i].get_innovation() == ListeGenParent2[i].get_innovation():
                matchParents += 1
                moyennePoids += abs(ListeGenParent1[i].get_poids() - ListeGenParent2[i].get_poids())

            elif ListeGenParent1[i] == 0 and ListeGenParent2[i] != 0 and i < MaxInnovationParent1:
                disjoint += 1

            elif ListeGenParent1[i] != 0 and ListeGenParent2[i] == 0:
                disjoint += 1

            elif ListeGenParent2[i] != 0 and ListeGenParent2[i].get_innovation() == i and i > MaxInnovationParent1 :
                exces += 1

        moyennePoids /= matchParents
        return moyennePoids,exces,disjoint

    ## fonction qui calcule la compatibilite entre deux genomes
    # @param genome1 premier genome a evaluer
    # @param genome2 deuxieme genome a evaluer
    @staticmethod
    def calc_distance_compatibilite(genome1,genome2):
        (m,e,d) = Genome.count_moyenne_exces_disjoint(genome1,genome2)
        return (Genome.DISTANCE_C1*e/1)+ (Genome.DISTANCE_C2*d/1) + Genome.DISTANCE_C3*m

    ## fonction qui teste les differentes fonctions de la classe
    @staticmethod
    def testRegression():

        print("initialisation du genome")
        G1 = Genome()
        G2 = Genome()
        if G1.get_listNoeuds() != [] or G1.get_listConnections() != []:
            print("echec de l'initialisation du genome")
            return -1
        print("initialisation reussie")

        l = []

        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("output",Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("output",Innovation.get_new_innovation_noeud()))

        print("id 1:",l[0].get_id())
        print("id 2:",l[1].get_id())

        for n in l:
            G1.ajout_noeud(n)
            G2.ajout_noeud(n)

        if len(G1.get_listNoeuds()) != 5:
            print("probleme lors de l'ajout d'un noeud")
            return -1
        print("tous les noeuds ont ete ajoute")

        while len(G1.get_listConnections())<3:
            G1.ajout_connec_mutation()
        while len(G2.get_listConnections())<5:
            G2.ajout_connec_mutation()


        if len(G1.get_listConnections()) != 3:
            print("probleme lors de la creation de la connection entre les noeuds")
            return -1
        print("la connection a ete ajoute")

        for i in range(0,3):
            G1.ajout_noeud_mutation()
            G2.ajout_noeud_mutation()

        #Trouver le bon nombre de connection
        """
        if len(G1.get_listConnections()) != 3 or len(G1.get_listNoeuds()) != 3:
            print("erreur lors de l'ajout d'un noeud de mutation")
            print("taille listConnections:", len(G1.get_listConnections()), " devrait etre egale a 3")
            print("taille listNoeuds: ", len(G1.get_listNoeuds()), "devrait etre egale a 3")
            return -1
        print("le noeud de mutation a ete ajoute")
        """
        tmppoids = []
        change = False
        for connec in G1.get_listConnections():
            tmppoids.append(connec.get_poids())

        #print(tmppoids)
        G1.connec_mutation()
        i = 0
        for connec in G1.get_listConnections():
            if connec.get_poids() != tmppoids:
                change = True
            i +=1
        if change == True:
            print("Les valeurs des connections ont changé")
        else:
            print("Aucun changement, connec mutaion ne marche pas")

        vG1 = [[],[]]
        vG2 = [[],[]]
        for noeud in G1.get_listNoeuds():
            vG1[0].append(noeud.get_id())
        for connec in G1.get_listConnections():
            vG1[1].append([connec.get_noeudin(),connec.get_noeudout()])
        print("liste noeud de G1:", vG1[0])
        print("liste connection de G1:", vG1[1])

        for noeud in G2.get_listNoeuds():
            vG2[0].append(noeud.get_id())
        for connec in G2.get_listConnections():
            vG2[1].append([connec.get_noeudin(),connec.get_noeudout()])
        print("liste noeud de G2:", vG2[0])
        print("liste connection de G2:", vG2[1])

        G3 = Genome.melange_genome(G1,G2)
        vG3 = [[],[]]
        for noeud in G3.get_listNoeuds():
            vG3[0].append(noeud.get_id())
        for connec in G3.get_listConnections():
            vG3[1].append([connec.get_noeudin(),connec.get_noeudout()])
        print("liste noeud de G3:", vG3[0])
        print("liste connection de G3:", vG3[1])

        print("compatibilité: ",Genome.calc_distance_compatibilite(G1,G3))
        print("fin du test de regression, passe avec succes")



#Genome.testRegression()
