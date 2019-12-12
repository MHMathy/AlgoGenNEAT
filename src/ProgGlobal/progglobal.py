from IA.generation import Generation
from IA.genome import Genome
from Outil.outil import Constantes
from Voiture.voiture import Voiture

class ProgGlobal:

    def __init__(self):

        self.debutCycle = 0
        self.dureeCycle = 0
        self.generateurGenome = None
        self.listeVoiture = []
        self.dictGenScore = {}

        self.listMeilleurScore = []

    def demarreProgramme(self):
        self.listMeilleurScore.clear()
        self.generateurGenome = Generation(Genome.default_mini())
        self.listeVoiture = [Voiture(Genome.default_mini(),190,110)]*Constantes.Cons["TAILLE_POPULATION"]
        for v in self.listeVoiture:
            self.dictGenScore.update({v.genome :0})



    def demarreCycle(self):
        print("GEN N°",len(self.listMeilleurScore))
        self.generateurGenome.evaluer(self.dictGenScore)
        if len(self.generateurGenome.get_listGenomes())!= Constantes.Cons.get("TAILLE_POPULATION"):
            print("MEGA GROSSE ERREUR")
        for gen in self.generateurGenome.get_listGenomes():
            self.listeVoiture.append(voiture(gen,190,110))

        self.dictGenScore.clear()

        self.debutCycle = time.time()


    #plus tard update avec un while et affichge en thread
    def update_once(self):
        self.dureeCycle = int((time.time() - self.debutCycle)*1000)

        for v in self.listeVoiture:
            if v.vivant == True:
                v.update(self.dureeCycle)


    def fin_cycle(self):

        for v in self.listeVoiture:
            dictGenScore.update({v.genome : v.calculscore()})

        self.listMeilleurScore.append(max(self.dictGenScore.values()))
        self.listeVoiture.clear()

    def arreterCourse(self):
        arret = True
        for v in self.listeVoiture:
            if v.vivant == True:
                arret = False

        if self.dureeCycle > Constantes.Cons.get("DURREE_CYCLE_EN_S"):
            arret = True
