class Innovation:
    nbNoeud = 0
    listC = []

    @classmethod
    def get_new_innovation_noeud(cls):
        Innovation.nbNoeud+=1
        return Innovation.nbNoeud

    @classmethod
    def get_new_innovation_connec(cls,nIn,nOut):
        for c in Innovation.listC:
            if c==[nIn,nOut]:
                return Innovation.listC.index([nIn,nOut])+1

        Innovation.listC.append([nIn,nOut])
        return len(Innovation.listC)
