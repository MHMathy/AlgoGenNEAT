## classe qui gere une connexion
class ConnexionGene:
    ## constructeur de la classe qui initialise les variables de la classe
    def __init__(self,noeudin,noeudout,poids,actif,innovation):
        ## noeud d'entree de la connexion
        self.__noeudin = noeudin

        ## noeud de sortie de la connexion
        self.__noeudout = noeudout

        ## poids de la connexion
        self.__poids = poids

        ## booleen qui defini si la connexion est active ou non
        self.__actif = actif

        ## numero d'innovation de la connexion
        self.__innovation = innovation

    ## retourne le noeud d'entree de la connexion
    def get_noeudin(self):
        return self.__noeudin

    ## retourne le noeud de sortie de la connexion
    def get_noeudout(self):
        return self.__noeudout

    ## retourne le poids de la connexion
    def get_poids(self):
        return self.__poids

    ## retourne l'etat de la connexion
    def get_actif(self):
        return self.__actif

    ## retourne le numero d'innovation de la connexion
    def get_innovation(self):
        return self.__innovation

    ## permet de mettre a jour le poids de la connexion
    # @param value nouvelle valeur du poids de la connexion
    def set_poids(self,value):
        self.__poids = min(2,max(-2,value))

    ## desactive une connexione
    def desactive(self):
        self.__actif = False

    ## renvoie la copie d'une connexion
    def copy_connec(self):
        return ConnexionGene(self.__noeudin,self.__noeudout,self.__poids,self.__actif,self.__innovation)
