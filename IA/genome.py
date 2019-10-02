from noeudgene import NoeudGene
from connectiongene import ConnectionGene
import random

class Genome:
    def ajout_connec(self,connection):
        self.__listConnections.append(connection)

    def ajout_noeud(self,noeud):
        self.__listNoeuds.append(noeud)

    def get_noeud(id):
        for noeud in __listNoeuds:
            if noeud.get_id() == id:
                return noeud


    def ajout_connec_mutation():
        noeud = random.sample(__listNoeuds,k=2) #noeud tiré au hazard

        inverse = False

        #if (noeud[0].get_type() == 'hidden' and noeud[1].get_type() == 'input') or (noeud[0].get_type() == 'output' and noeud[1].get_type() == 'hidden') or (noeud[0].get_type() == 'output' and noeud[1].get_type() == 'input'):

        if noeud[0].get_type() == 'hidden' and noeud[1].get_type() == 'input':
            inverse = True
        elif noeud[0].get_type() == 'output' and noeud[1].get_type() == 'hidden':
            inverse = True
        elif noeud[0].get_type() == 'output' and noeud[1].get_type() == 'input':
            inverse = True

        noeud.sort(reverse=inverse)

        connecExist = False
        for connec in __listConnections:
            if connec.__noeudin == noeud[0].get_id() and connec.__noeudout == noeud[1].get_id():
                connecExist = True
        #break

        new_connec = ConnectionGene(noeud[0].get_id(),noeud[1].get_id(),poids,True,innovation) #incrémenter de 1 l'innovatino et garder la trace

        #if inverse == False:
            #new_connec = ConnectionGene(noeud[0],noeud[1],poids,True,innovation) #incrémenter de 1 l'innovatino et garder la trace

        #if inverse == True:
            #new_connec = ConnectionGene(noeud[1],noeud[0],poids,True,innovation)

        ajout_connec(new_connec)

    def ajout_noeud_mutation():
        connec = random.choice(__listConnections)
        noeudin = get_noeud(connec.__noeudin)
        noeudout = get_noeud(connec.__noeudout)

        connec.deactive()

        newnoeud = NoeudGene("hidden",len(__listNoeuds))

        co_in_new = ConnectionGene(noeudin.get_id(),newnoeud.get_id(),1,True,0)
        co_new_out = ConnectionGene(newnoeud.get_id(),noeudout.get_id(),connec.get_poids(),True,0)

        ajout_noeud(newnoeud)

        ajout_connec(co_in_new)
        ajout_connec(co_new_out)
