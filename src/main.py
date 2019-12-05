from classeMain.ClasseMain import Main
from Affichage.Affichage import Affichage
from ProgGlobal.ProgGlobal import ProgGlobal
#cd Documents/L3/LifProjet/mathymartinet/

## initialisation d'un main, et lancement de son execution
def main():

    glob = ProgGlobal()
    aff = Affichage()
    aff.boucle(glob)


main()
