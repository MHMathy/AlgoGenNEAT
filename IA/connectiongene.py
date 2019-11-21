## classe qui gere une connection
class ConnectionGene:
    ## constructeur de la classe qui initialise les variables de la classe
    def __init__(self,noeudin,noeudout,poids,actif,innovation):
        ## noeud d'entree de la connection
        self.__noeudin = noeudin

        ## noeud de sortie de la connection
        self.__noeudout = noeudout

        ## poids de la connection
        self.__poids = poids

        ## booleen qui defini si la connection est active ou non
        self.__actif = actif

        ## numero d'innovation de la connection
        self.__innovation = innovation

    ## retourne le noeud d'entree de la connection
    def get_noeudin(self):
        return self.__noeudin

    ## retourne le noeud de sortie de la connection
    def get_noeudout(self):
        return self.__noeudout

    ## retourne le poids de la connection
    def get_poids(self):
        return self.__poids

    ## retourne l'etat de la connection
    def get_actif(self):
        return self.__actif

    ## retourne le numero d'innovation de la connection
    def get_innovation(self):
        return self.__innovation

    ## permet de mettre a jour le poids de la connection
    # @param value nouvelle valeur du poids de la connection
    def set_poids(self,value):
        self.__poids = min(2,max(-2,value))

    ## desactive une connectione
    def deactive(self):
        self.__actif = False

    ## renvoie la copie d'une connection
    def copy_connec(self):
        return ConnectionGene(self.__noeudin,self.__noeudout,self.__poids,self.__actif,self.__innovation)
