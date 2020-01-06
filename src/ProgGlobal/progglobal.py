from IA.generation import Generation
from IA.genome import Genome
from Outil.outil import Constantes
from Voiture.voiture import Voiture
import random
import time

class ProgGlobal:

    def __init__(self):

        self.debutCycle = 0
        self.dureeCycle = 0
        self.generateurGenome = None
        self.listVoiture = []
        self.dictGenScore = {}
        self.gmax = None
        self.listMeilleurScore = []

    def demarreProgramme(self):
        self.listMeilleurScore.clear()
        self.listVoiture.clear()
        self.dictGenScore.clear()

        genDef = Genome.default()

        self.dictGenScore.update({genDef:0})

        self.generateurGenome = Generation(genDef)

        self.listMeilleurScore = [0]



    def demarreCycle(self):
        print()
        print("GEN N°",len(self.listMeilleurScore)," Meilleur Score: ",self.listMeilleurScore[-1])

        self.generateurGenome.evaluer(self.dictGenScore)

        for gen in self.generateurGenome.get_listGenomes():
            x = random.randint(190,210)
            y = random.randint(140,160)
            self.listVoiture.append(Voiture(gen,200,150))


        m = max(self.dictGenScore.values())

        tmp = [key  for (key, value) in self.dictGenScore.items() if value == m]
        self.gmax = tmp[0]

        self.dictGenScore.clear()

        self.debutCycle = time.time()
        self.dureeCycle = 0


    #plus tard update avec un while et affichge en thread
    def update_once(self):

        self.dureeCycle = int(time.time() - self.debutCycle)
        for v in self.listVoiture:

            if v.vivant == True:
                v.update(self.dureeCycle)


    def fin_cycle(self):

        for v in self.listVoiture:

            score = v.calculScore()

            self.dictGenScore.update({v.genome : score})

        self.listMeilleurScore.append(max(self.dictGenScore.values()))
        self.listVoiture.clear()

    def arreterCourse(self):
        arret = True
        for v in self.listVoiture:
            if v.vivant == True:
                arret = False

        
        if self.dureeCycle > Constantes.Cons.get("DURREE_CYCLE_EN_S"):
            print(self.dureeCycle)
            arret = True

        return arret
