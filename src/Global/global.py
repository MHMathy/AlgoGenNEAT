class Global:
    def __init__(self):
        self.listeConstantes = {"proba_mut": Genome.PROBA_MUTATION,
                           "proba_mut_coef": Genome.PROBA_MUTATION_COEF,
                           "C1": Genome.DISTANCE_C1,
                           "C2": Genome.DISTANCE_C2,
                           "C3": Genome.DISTANCE_C3,
                           "default_connec": Genome.DEFAULT_N_CONNEC}
        self.population
        self.debutCycle
        self.dureeCycle
        self.generateurGenome
        self.listeVoiture = []
        self.dictGenScore = {}
        self.dict

    def demarreProgramme(self,population):

        self.population = population
        self.listeVoiture = [voiture(Genome.default_mini(),190,110)]*population
        self.generateurGenome = Generation()
        self.debutCycle = time.time()


    def demarreCycle(self):
        self.debutCycle = time.time()
        #generateurGenome créer new Gen
        #init les voitures avec
        #recommence le cycle


    #plus tard update avec un while et affichge en thread
    def update_once(self):
        self.dureeCycle = int((time.time() - self.debutCycle)*1000)

        for v in self.listeVoiture:
            v.update(self.dureeCycle)


    def fin_cycle(self):
        self.dictGenScore = {}
        for v in self.listeVoiture:
            dictGenScore.update({v.genome : v.calculscore()})

    #fontion pour distribuer les variables globales
