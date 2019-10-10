class ConnectionGene:
    def __init__(self,noeudin,noeudout,poids,actif,innovation):
        self.__noeudin = noeudin
        self.__noeudout = noeudout
        self.__poids = poids
        self.__actif = actif
        self.__innovation = innovation

    def deactive():
        self.__actif = False

    def get_noeudin():
        return self.__noeudin

    def get_noeudout():
        return self.__noeudout

    def get_poids():
        return self.__poids

    def get_actif(self):
        return self.__actif

    def get_innovation():
        return self.__innovation

    def copy_connec(self):
        return ConnectionGene(self.__noeudin,self.__noeudout,self.__poids,self.__actif,self.__innovation)
