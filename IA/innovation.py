class Innovation:
    nbNoeud = 0
    listC = []

    @classmethod
    def get_new_innovation_noeud(cls):
        Innovation.nbNoeud+=1
        return nbNoeud

    @classmethod
    def get_new_innovation_connec(cls,nIn,nOut):
        for c in listC:
            if c==[nIn,nOut]:
                return listC.index([nIn,nOut])+1

        Innovation.listC.append([nIn,nOut])
        return len(listC)
