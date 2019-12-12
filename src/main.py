from Affichage.affichage import Affichage
from ProgGlobal.progglobal import ProgGlobal
#cd Documents/L3/LifProjet/mathymartinet/

## initialisation d'un main, et lancement de son execution
def main():

    glob = ProgGlobal()
    aff = Affichage()
    aff.boucleAff(glob)


main()
