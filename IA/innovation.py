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
        for c in Innovation.listC:
            if c==[nIn,nOut]:
                return Innovation.listC.index([nIn,nOut])+1

        Innovation.listC.append([nIn,nOut])
        return len(Innovation.listC)
