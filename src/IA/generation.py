from .genome import Genome
from Outil.outil import Constantes
import random

class Generation:
    def __init__ (self,genomeDefault):
        self.taillePopulation = Constantes.Cons.get("TAILLE_POPULATION")

        self.lienGenomeEspece = {}
        self.lienGenomeAptitude = {}

        self.listEspeces = []
        self.listGenomes = []
        self.listGenomes = [genomeDefault] * self.taillePopulation

        self.nextGenGenome = []

        self.maxAptitude = 0


    def evaluer(self,dictScore):

        #Reinitialiser les dictionnaires
        for e in self.listEspeces:
            e.reset()

        self.lienGenomeEspece.clear()
        self.lienGenomeAptitude.clear()
        self.nextGenGenome.clear()

        for key in dictScore.keys():
            self.listGenomes.append(key)


        #Place les genomes dans des espèces
        for g in self.listGenomes:

            trouveEspece = False
            for e in self.listEspeces:
                #Si le genome est proche de la mascotte d'une espèce, on l'ajoute à l'espèce

                if Genome.calc_distance_compatibilite(g,e.mascotte)<Constantes.Cons.get("DISTANCE_MIN_ESPECE"):
                    e.membres.append(g)
                    self.lienGenomeEspece.update({g:e})
                    trouveEspece = True
                    break
            #Sinon on crée une nouvelle espèce avec le genome en mascotte
            if trouveEspece == False:
                newEspece = Espece(g)
                self.listEspeces.append(newEspece)
                self.lienGenomeEspece.update({g:newEspece})

        #Enlève les espèces vides
        #Mettre un print voir si ça s'active un jour
        for e in self.listEspeces[:]:

            if len(e.membres)==0:
                self.listEspeces.remove(e)


        #Evaluer les genomes et assigner les aptitudes
        for g in self.listGenomes:
            e = self.lienGenomeEspece.get(g)
            score = dictScore.get(g)
            scoreAjuster = score
            if score!= None:
                print(len(e.membres),"et",score)
                scoreAjuster=score/len(e.membres)
            e.ajout_aptitude_ajuster(scoreAjuster)
            e.aptitudePopulation.append(AptitudeGenome(g,scoreAjuster))
            self.lienGenomeAptitude.update({g:scoreAjuster})
            if score>self.maxAptitude:
                self.maxAptitude = score

        #Mettre les meilleurs genomes de chaque espèce dans la generation suivante
        for e in self.listEspeces:
            e.aptitudePopulation.sort(key=lambda x: x.aptitude,reverse=True)
            self.nextGenGenome.append(e.aptitudePopulation[0].genome)


        #Generer le reste de la prochaine generation par mélange
        while len(self.nextGenGenome)<self.taillePopulation:
            e = self.get_random_espece()

            g1 = self.get_random_genome(e)
            g2 = self.get_random_genome(e)

            if self.lienGenomeAptitude.get(g1)>=self.lienGenomeAptitude.get(g2):
                gfils = Genome.melange_genome(g1,g2)
            else:
                gfils = Genome.melange_genome(g2,g1)

            if random.randint(1,100)<Constantes.Cons.get("PROBA_MUTATION_GENOME"):
                gfils.connec_mutation()

            if random.randint(1,100)<Constantes.Cons.get("PROBA_AJOUT_CONNEC_GENOME"):
                gfils.ajout_connec_mutation()

            if random.randint(1,100)<Constantes.Cons.get("PROBA_AJOUT_NOEUD_GENOME"):
                gfils.ajout_noeud_mutation()

            self.nextGenGenome.append(gfils)

        self.listGenomes = list(self.nextGenGenome)
        self.nextGenGenome.clear()

    def get_listGenomes(self):
        return self.listGenomes


    def get_random_espece(self):
        maxApt = max(esp.aptitudeTotalAjuster for esp in self.listEspeces)
        while True:
            e = random.choice(self.listEspeces)
            if e.aptitudeTotalAjuster>(maxApt*0.7):
                return e

    def get_random_genome(self,esp):
        maxApt = max(gen.aptitude for gen in esp.aptitudePopulation)
        while True:
            gen = random.choice(esp.aptitudePopulation)
            if gen.aptitude>(maxApt*0.7):
                return gen.genome

    @staticmethod
    def evaluer_Genome(g):
        print("n'aurait pas du s'activer")
        pass



class AptitudeGenome:

    def __init__(self,genome, scoreAptitude):
        self.genome = genome
        self.aptitude = scoreAptitude

    @staticmethod
    def comparer(aptG1,aptG2):
        if aptG1.aptitude > aptG2.aptitude :
            return 1
        elif aptG1.aptitude < aptG2.aptitude :
            return -1
        else:
            return 0


class Espece:

    def __init__(self,mascotte):
        self.mascotte = mascotte
        self.membres = []
        self.membres.append(self.mascotte)
        self.aptitudePopulation = []
        self.aptitudeTotalAjuster = 0

    def ajout_aptitude_ajuster(self,aptAjuster):
        self.aptitudeTotalAjuster += aptAjuster

    def reset(self):
        self.mascotte = random.choice(self.membres)
        self.membres.clear()
        self.aptitudePopulation.clear()
        self.aptitudeTotalAjuster = 0


class testGeneration(Generation):
    def __init__(self,pop,genD):
        Generation.__init__(self,pop,genD)

    def get_aptitude_max(self):
        return self.maxAptitude

    def get_nb_espece(self):
        return len(self.listEspeces)


    @staticmethod
    def evaluer_Genome(g):
        return len(g.get_listConnections())

    @staticmethod
    def testRegression():
        gen = testGeneration(10,Genome.default())

        for i in range(100):
            gen.evaluer()
            print("Generation: ", i,"  Aptitude max: ",gen.get_aptitude_max(),"  Nombre especes: ",gen.get_nb_espece())

#testGeneration.testRegression()
