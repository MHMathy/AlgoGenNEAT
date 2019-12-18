## classe qui garde en memoire l'etat d'un genome (connections et nombres de neuronnes)
class Innovation:
    nbNoeud = 0
    listC = []

    ## retourne le nombre de noeuds
    @classmethod
    def get_new_innovation_noeud(cls):
        Innovation.nbNoeud+=1
        return Innovation.nbNoeud

    ## retourne le nombre de connections dans la liste
    @classmethod
    def get_new_innovation_connec(cls,nIn,nOut):

        if [nIn,nOut] in cls.listC:
            return cls.listC.index([nIn,nOut])+1
        else:
            cls.listC.append([nIn,nOut])
        return len(Innovation.listC)

class Constantes:

    Cons = {
        "TAILLE_POPULATION": 10,
        "DURREE_CYCLE_EN_S": 10,

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


    @classmethod
    def get_listConstantes(cls):
        return cls.Cons

    @classmethod
    def set_listConstantes(cls,nomConst,valConst):
            cls.Cons[nomConst] = valConst
