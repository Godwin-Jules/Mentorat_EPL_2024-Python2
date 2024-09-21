class Rectangle:

    def __init__(self, longueur, largeur):
        if longueur < 0:
            longueur = 0
        if largeur < 0:
            largeur = 0
        self._longueur = longueur
        self._largeur = largeur

    @property
    def longueur(self):
        return f"{self._longueur}cm"

    @property
    def largeur(self):
        return f"{self._largeur}cm"

    @longueur.setter
    def longueur(self, nv_longueur):
        if nv_longueur > 0:
            self._longueur = nv_longueur
        else:
            print("La longueur doit être supérieure à 0")

    @largeur.setter
    def largeur(self, nv_largeur):
        if nv_largeur > 0:
            self._largeur = nv_largeur
        else:
            print("La largeur doit être supérieure à 0")

    @longueur.deleter
    def longueur(self):
        del self._longueur

    @largeur.deleter
    def largeur(self):
        del self._largeur