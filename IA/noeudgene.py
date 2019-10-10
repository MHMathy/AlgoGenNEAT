class NoeudGene:
    def __init__(self,type,id):
        self.__type=type
        self.__id=id

    def get_type(self):
        return self.__type

    def get_id(self):
        return self.__id

    def copy_noeud(self):
        return NoeudGene(self.__type,self.__id)
