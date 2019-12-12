from IA.generation import Generation
from IA.genome import Genome
from Outil.outil import Constantes
from Voiture.voiture import Voiture
import time

class ProgGlobal:

    def __init__(self):

        self.debutCycle = 0
        self.dureeCycle = 0
        self.generateurGenome = None
        self.listVoiture = []
        self.dictGenScore = {}

        self.listMeilleurScore = []

    def demarreProgramme(self):
        self.listMeilleurScore.clear()
        self.listVoiture.clear()
        self.dictGenScore.clear()
        genDef = Genome.default_mini()
        self.generateurGenome = Generation(genDef)
        for i in range(Constantes.Cons.get("TAILLE_POPULATION")):
            self.dictGenScore.update({genDef :0})



    def demarreCycle(self):
        print("GEN N°",len(self.listMeilleurScore))
        self.generateurGenome.evaluer(self.dictGenScore)
        if len(self.generateurGenome.get_listGenomes())!= Constantes.Cons.get("TAILLE_POPULATION"):
            print("MEGA GROSSE ERREUR")
        for gen in self.generateurGenome.get_listGenomes():
            self.listVoiture.append(Voiture(gen,190,110))

        self.dictGenScore.clear()

        self.debutCycle = time.time()


    #plus tard update avec un while et affichge en thread
    def update_once(self):
        self.dureeCycle = int((time.time() - self.debutCycle)*1000)

        for v in self.listVoiture:
            if v.vivant == True:
                v.update(self.dureeCycle)


    def fin_cycle(self):

        for v in self.listVoiture:
            self.dictGenScore.update({v.genome : v.calculScore()})

        self.listMeilleurScore.append(max(self.dictGenScore.values()))
        self.listVoiture.clear()

    def arreterCourse(self):
        arret = True
        for v in self.listVoiture:
            if v.vivant == True:
                arret = False

        if self.dureeCycle > Constantes.Cons.get("DURREE_CYCLE_EN_S"):
            arret = True
