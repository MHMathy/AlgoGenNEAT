from .genome import Genome
from Outil.outil import Constantes
import random

## classe Generation qui va permettre de derouler une generation
class Generation:

    ##constructeur de la classe
    def __init__ (self,genDef):
        self.taillePopulation = Constantes.Cons.get("TAILLE_POPULATION")

        self.lienGenomeEspece = {}
        self.lienGenomeAptitude = {}

        self.listEspeces = []
        self.listGenomes = []
        self.listGenomes = [genDef]*self.taillePopulation
        self.nextGenGenome = []

        self.maxAptitude = 0

    ## fonction evaluer, qui va gerer le classement entre especes des differents genomes
    def evaluer(self,dictScore):

        #Reinitialiser les dictionnaires
        for e in self.listEspeces:
            e.reset()

        self.lienGenomeEspece.clear()
        self.lienGenomeAptitude.clear()
        self.nextGenGenome.clear()

        if len(dictScore.keys())!=1:
            self.listGenomes.clear()

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

        #Evaluer les genomes et assigner les aptitudes
        for g in self.listGenomes:
            e = self.lienGenomeEspece.get(g)

            score = abs(dictScore.get(g))

            scoreAjuster = score
            scoreAjuster=score/len(e.membres)

            e.ajout_aptitude_ajuster(scoreAjuster)
            e.aptitudePopulation.append(AptitudeGenome(g,scoreAjuster))
            self.lienGenomeAptitude.update({g:scoreAjuster})
            if score>self.maxAptitude:
                self.maxAptitude = score

        #Enlève les espèces avec uniquement la mascotte
        for e in self.listEspeces[:]:
            if len(e.membres)==1:
                self.listEspeces.remove(e)

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

        #Le prochaine generation devient la generation actuelle
        self.listGenomes = list(self.nextGenGenome)
        self.nextGenGenome.clear()
        print("  Nombre especes: ",len(self.listEspeces))
        m = max(self.lienGenomeAptitude.values())
        gmax = [key  for (key, value) in self.lienGenomeAptitude.items() if value == m]
        print("max score: ",m)
        gmax[0].aff_genome()


    ## fonction qui renvoie la liste de genomes
    def get_listGenomes(self):
        return self.listGenomes

    ## fonction qui retourne une espece aleatoire, en favorisant les espèces avec un meilleur score
    def get_random_espece(self):
        maxApt = max(esp.aptitudeTotalAjuster for esp in self.listEspeces)
        r = random.random()*maxApt
        conteApt = 0
        for e in sorted(self.listEspeces, key = lambda esp: esp.aptitudeTotalAjuster):
            conteApt+=e.aptitudeTotalAjuster
            if conteApt >=r:
                return e

    ## fonction qui retourne un genome aleatoire, favorisant les genomes avec un meilleur score
    def get_random_genome(self,esp):
        maxApt = max(gen.aptitude for gen in esp.aptitudePopulation)
        r = random.random()*maxApt
        conteApt = 0
        for aptGen in sorted(esp.aptitudePopulation, key = lambda aptGen: aptGen.aptitude):
            conteApt+=aptGen.aptitude

            if conteApt>=r:
                return aptGen.genome


## classe qui gere l'aptitude des genomes
class AptitudeGenome:

    ## constructeur de la classe
    # @param scoreAptitude score obtenu par le genome
    def __init__(self,genome, scoreAptitude):
        self.genome = genome
        self.aptitude = scoreAptitude

    ## fonction qui regarde si le genome 1 a un meilleur score que le genome 2
    @staticmethod
    def comparer(aptG1,aptG2):
        if aptG1.aptitude > aptG2.aptitude :
            return 1
        elif aptG1.aptitude < aptG2.aptitude :
            return -1
        else:
            return 0

## classe qui gere les especes
class Espece:

    ## constructeur de la classe
    # @param mascotte genome de reference
    def __init__(self,mascotte):
        self.mascotte = mascotte
        self.membres = []
        self.membres.append(self.mascotte)
        self.aptitudePopulation = []
        self.aptitudeTotalAjuster = 0

    ## fonction qui incremente l'aptitude totale
    def ajout_aptitude_ajuster(self,aptAjuster):
        self.aptitudeTotalAjuster += aptAjuster

    ## fonction qui vide les différents objets pour la generation suivante
    def reset(self):
        self.mascotte = random.choice(self.membres)
        self.membres.clear()
        self.membres.append(self.mascotte)
        self.aptitudePopulation.clear()
        self.aptitudeTotalAjuster = 0
