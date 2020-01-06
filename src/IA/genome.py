from .noeudgene import NoeudGene
from .connexiongene import ConnexionGene
from Outil.outil import Innovation
from Outil.outil import Constantes
import random

## classe qui gere les neurones sous forme de liste de noeuds et liste de connexions
class Genome:

    ## constructeur qui initialise les deux listes de la classe comme etant des listes vides
    def __init__(self):
        self.__listConnexions = []
        self.__listNoeuds = []

    ## fonction qui initialise un genome avec des connexions definies
    @staticmethod
    def default(type="normal"):
        l = []
        g = Genome()
        l.append(NoeudGene("output",Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("output",Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        l.append(NoeudGene("input", Innovation.get_new_innovation_noeud()))
        for n in l:
            g.ajout_noeud(n)

        g.ajout_connec(ConnexionGene(3,1,1,True,Innovation.get_new_innovation_connec(3,1)))
        g.ajout_connec(ConnexionGene(4,1,1,True,Innovation.get_new_innovation_connec(4,1)))

        g.ajout_connec(ConnexionGene(5,2,1,True,Innovation.get_new_innovation_connec(5,2)))
        g.ajout_connec(ConnexionGene(6,2,1,True,Innovation.get_new_innovation_connec(6,2)))
        #g.ajout_connec(ConnexionGene(7,2,1,True,Innovation.get_new_innovation_connec(7,2)))
        #g.ajout_connec(ConnexionGene(8,2,1,True,Innovation.get_new_innovation_connec(8,2)))
        #g.ajout_connec(ConnexionGene(9,2,1,True,Innovation.get_new_innovation_connec(9,2)))
        #g.ajout_connec(ConnexionGene(10,2,1,True,Innovation.get_new_innovation_connec(10,2)))
        #g.ajout_connec(ConnexionGene(11,1,1,True,Innovation.get_new_innovation_connec(11,1)))

        return g

    ## fonction qui ajoute une connexion aleatoire
    def random_connexion(self,nbCo=Constantes.Cons.get("DEFAULT_N_CONNEC")):
        for i in range(nbCo):
            self.ajout_connec_mutation()

    # ajouter une connexion à la liste de connexion
    ## fonction qui ajoute une connexion dans la liste
    # @param connexion Connexion a ajoute dans la liste
    def ajout_connec(self,connexion):
        self.__listConnexions.append(connexion)

    # ajouter un noeud à la liste de noeud
    ## fonction qui ajoute un noeud dans la liste
    # @param noeud Noeud a ajoute dans la liste
    def ajout_noeud(self,noeud):
        self.__listNoeuds.append(noeud)

    # retourne la liste de noeud
    ## fonction qui retourne la liste des noeuds du genome
    def get_listNoeuds(self):
        return self.__listNoeuds

    # retourne la liste de connexions
    ## fonction qui retourne la liste des connexions du genome
    def get_listConnexions(self):
        return self.__listConnexions

    # retourne un noeud à partir de son numero id
    ## fonction qui retourne un noeud en fonction de son ID
    # @param id ID du noeud a chercher
    def get_noeud(self,id):
        for noeud in self.__listNoeuds:
            if noeud.get_id() == id:
                return noeud

    # retourne le type d'un noeud à partir de son numero id
    ## fonction qui retourne le type d'un noeud en fonction de son ID
    # @param id ID du noeud a chercher
    def get_type_noeud(self,id):
        return self.get_noeud(id).get_type()

    ## fonction qui retourne une connexion en fonction de son ID
    # @param id ID de la connexion a chercher
    def get_connexion(self,id):
        for connec in self.__listConnexions:
            if connec.get_innovation() == id:
                return connec

    # retourne le numero d'innovation max de la liste de connexion
    ## fonction qui retourne le numero d'innovation le plus elever dans la liste
    def get_maxNumInnovation(self):
        maxinno = 0
        for connec in self.__listConnexions:
            if connec.get_innovation()>maxinno:
                maxinno=connec.get_innovation()
        return maxinno

    def aff_genome(self):
        vG = [[],[]]
        for noeud in self.get_listNoeuds():
            vG[0].append(noeud.get_id())
        for connec in self.get_listConnexions():
            vG[1].append([connec.get_noeudin(),connec.get_noeudout(), connec.get_actif()])
        print("liste noeud du genome:", vG[0])
        print("liste connexion du genome:", vG[1])

    ## fonction qui remplace une connexion dans la liste
    # @param newConnec Connexion qui remplacera la precedente dans la liste
    def remplace_connec(self,newConnec):
        for connec in self.__listConnexions:
            if connec.get_innovation() == newConnec.get_innovation():
                connec = newConnec

    # modifie la valeur
    ## fonction qui gere la mutation d'une connexion
    def connec_mutation(self):
        for connec in self.__listConnexions:
            if random.randint(1,100)<Constantes.Cons.get("PROBA_MUTATION"):
                if random.randint(1,100)<Constantes.Cons.get("PROBA_MUTATION_COEF"):
                    connec.set_poids(connec.get_poids()*random.uniform(-2,2))
                else:
                    connec.set_poids(random.uniform(-2,2))

    ## fonction qui ajoute une connexion a une mutation
    def ajout_connec_mutation(self):
        noeud = []
        connecExist = True
        essai = 0
        maxEssai = 100
        succes = False
        while essai<=maxEssai and succes==False:

            essai += 1
            while True:
                noeud = random.sample(self.__listNoeuds,2) #noeud tire au hazard
                if not(noeud[0].get_type() == noeud[1].get_type() and (noeud[0].get_type() == "input" or noeud[0].get_type() == "output")):
                    break


            if noeud[0].get_type() == "hidden" and noeud[1].get_type() == "input":
                noeud.reverse()
            elif noeud[0].get_type() == "output" and noeud[1].get_type() == "hidden":
                noeud.reverse()
            elif noeud[0].get_type() == "output" and noeud[1].get_type() == "input":
                noeud.reverse()

            if [noeud[1].get_id(),noeud[0].get_id()] in Innovation.listC:
                continue #Si la connexion exist deja


            prochain = False
            for connec in self.__listConnexions:
                if connec.get_noeudin() == noeud[0].get_id() and connec.get_noeudout() == noeud[1].get_id():
                    prochain = True #Si la connexion exist deja dans le genome

            if prochain:
                continue

            newConnec = ConnexionGene(noeud[0].get_id(),noeud[1].get_id(),1,True,Innovation.get_new_innovation_connec(noeud[0].get_id(),noeud[1].get_id()))
            self.ajout_connec(newConnec)
            succes = True

        if succes == False:
            print("Ajout de connexion impossible")



    ## fonction qui ajoute un noeud a une mutation
    def ajout_noeud_mutation(self):
        connec = random.choice(self.__listConnexions)
        noeudin = self.get_noeud(connec.get_noeudin())
        noeudout = self.get_noeud(connec.get_noeudout())

        connec.desactive()

        newNoeud = NoeudGene("hidden",Innovation.get_new_innovation_noeud())

        coInNew = ConnexionGene(noeudin.get_id(),newNoeud.get_id(),1,True,Innovation.get_new_innovation_connec(noeudin.get_id(),newNoeud.get_id()))
        coNewOut = ConnexionGene(newNoeud.get_id(),noeudout.get_id(),connec.get_poids(),True,Innovation.get_new_innovation_connec(newNoeud.get_id(),noeudout.get_id()))

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


        for noeudp1 in genParent1.get_listNoeuds():
            noeudtemp.append(noeudp1.get_id())
            newGenome.ajout_noeud(noeudp1.copy_noeud())

        for noeudp2 in genParent2.get_listNoeuds():
            if noeudp2.get_id() in noeudtemp:
                continue
            newGenome.ajout_noeud(noeudp2.copy_noeud())



        for connecp1 in genParent1.get_listConnexions():
            connectemp.append(connecp1.get_innovation())
            newGenome.ajout_connec(connecp1.copy_connec())


        for connecp2 in genParent2.get_listConnexions():
            if connecp2.get_innovation() in connectemp:
                if random.choice([True,False]) == True:
                    newGenome.remplace_connec(connecp2.copy_connec())
            else:
                newGenome.ajout_connec(connecp2.copy_connec())

        return newGenome

    #fonction qui renvoie le poids moyen des connexions, le nombre d'exces et le nombre de disjoints
    ## fonction qui renvoie le poids moyen des connexions, le nombres de noeuds en exces et le nombres de noeuds "decaler" dans la liste entre les deux parents
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
        #en cas d'absence de connexion
        for connec in genParent1.get_listConnexions():
            ListeGenParent1[connec.get_innovation() - 1] = connec

        for connec in genParent2.get_listConnexions() :
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
        return (Constantes.Cons.get("DISTANCE_C1")*e/1)+ (Constantes.Cons.get("DISTANCE_C2")*d/1) + Constantes.Cons.get("DISTANCE_C3")*m
