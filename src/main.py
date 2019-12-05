from classeMain.ClasseMain import Main
from Affichage.Affichage import Affichage
from Global.global import Global
#cd Documents/L3/LifProjet/mathymartinet/

## initialisation d'un main, et lancement de son execution
def main():

    glob = Global()
    aff = Affichage()
    aff.boucle(glob)


main()
