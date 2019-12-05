"""
separer calcul affichage
import ProgGlobal dans des sous classes
utilité sigmoid que si on fait varier l'intensité de l'action
utiliser private ou non
qu'est-ce qu'il y a dans le rapport

"""

"""
TAILLE_POPULATION = 10
DUREE_CYCLE_EN_S = 60

DISTANCE_MIN_ESPECE = 5
PROBA_MUTATION_GENOME = 50
PROBA_AJOUT_CONNEC_GENOME = 10
PROBA_AJOUT_NOEUD_GENOME = 10

PROBA_MUTATION = 80
PROBA_MUTATION_COEF = 90
DISTANCE_C1 = 1
DISTANCE_C2 = 1
DISTANCE_C3 = 0.4
DEFAULT_N_CONNEC = 6

COEF_EXPO = 1
"""



class ProgGlobal:

    Cons = {
        "TAILLE_POPULATION": 10,
        "DUREE_CYCLE_EN_S" = 60,

        "DISTANCE_MIN_ESPECE": 5,
        "PROBA_MUTATION_GENOME": 50,
        "PROBA_AJOUT_CONNEC_GENOME": 10,
        "PROBA_AJOUT_NOEUD_GENOME": 10,

        "PROBA_MUTATION": 80,
        "PROBA_MUTATION_COEF": 90,
        "DISTANCE_C1": 1,
        "DISTANCE_C2": 1,
        "DISTANCE_C3": 0.4,
        "DEFAULT_N_CONNEC": 6,

        "COEF_EXPO": 1
       }

    def __init__(self):

        self.debutCycle
        self.dureeCycle
        self.generateurGenome
        self.listeVoiture = []
        self.dictGenScore = {}

        self.listMeilleurScore = []

    def demarreProgramme(self,population,durree):
        self.listMeilleurScore.clear()
        ProgGlobal.Cons["TAILLE_POPULATION"] = population
        ProgGlobal.Cons["durree"] =
        self.generateurGenome = Generation(Genome.default_mini())
        self.listeVoiture = [voiture(Genome.default_mini(),190,110)]*population
        for v in self.listeVoiture:
            dictGenScore.update({v.genome :0})



    def demarreCycle(self):

        self.generateurGenome.evaluer(self.dictGenScore)
        if len(self.generateurGenome.get_listGenomes())!= ProgGlobal.Cons.get("TAILLE_POPULATION"):
            print("MEGA GROSSE ERREUR")
        for gen in self.generateurGenome.get_listGenomes():
            self.listeVoiture.append(voiture(gen,190,110))

        self.dictGenScore.clear()

        self.debutCycle = time.time()


    #plus tard update avec un while et affichge en thread
    def update_once(self):
        self.dureeCycle = int((time.time() - self.debutCycle)*1000)

        for v in self.listeVoiture:
            if v.vivant == True
                v.update(self.dureeCycle)


    def fin_cycle(self):

        for v in self.listeVoiture:
            dictGenScore.update({v.genome : v.calculscore()})

        self.listMeilleurScore.append(max(self.dictGenScore;values()))
        self.listeVoiture.clear()

    def arreterCourse(self):
        arret = True
        for v in self.listeVoiture:
            if v.vivant == True:
                arret = False

        if self.dureeCycle > ProgGlobal.Cons.get("DUREE_CYCLE_EN_S"):
            arret = True


    @classmethod
    def get_listConstantes(cls):
        return cls.Cons

    @classmethod
    def set_listConstantes(cls,nomConst,valConst):
            cls.Cons[nomConst] = valConst
