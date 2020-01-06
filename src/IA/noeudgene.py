## classe qui gere les informations ProgGlobales d'un noeud
class NoeudGene:
    ## constructeur de la classe
    # @param type defini le type du noeud (input, output, hidden)
    # @param id identifiant du noeud
    def __init__(self,type,id):
        self.__type=type
        self.__id=id

    ## retourne le type du noeud
    def get_type(self):
        return self.__type

    ## retourne l'id du noeud
    def get_id(self):
        return self.__id

    ## renvoie une copie du noeud
    def copy_noeud(self):
        return NoeudGene(self.__type,self.__id)
