class ConnectionGene:
    def __init__(self,noeudin,noeudout,poids,actif,innovation):
        self.__noeudin = noeudin
        self.__noeudout = noeudout
        self.__poids = poids
        self.__actif = actif
        self.__innovation = innovation



    def get_noeudin(self):
        return self.__noeudin

    def get_noeudout(self):
        return self.__noeudout

    def get_poids(self):
        return self.__poids

    def get_actif(self):
        return self.__actif

    def get_innovation(self):
        return self.__innovation

    def set_poids(self,value):
        self.__poids = min(2,max(-2,value))

    def deactive(self):
        self.__actif = False

    def copy_connec(self):
        return ConnectionGene(self.__noeudin,self.__noeudout,self.__poids,self.__actif,self.__innovation)
