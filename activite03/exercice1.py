from math import sqrt


class Complexe:

    # Le constructeur
    def __init__(self, a=0, b=0):
        self.__a = a
        self.__b = b

    # Les accesseurs
    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def setA(self, a):
        self.__a = a

    def setB(self, b):
        self.__b = b

    # La méthode qui permet de faire afficher un nombre complexe
    def __str__(self):
        b = self.getB()
        return f"{self.getA()} {"+" if b > 0 else ""}{b if b not in {-1, 0, 1} else ""}{"i" if b != 0 else ""}"

    # La méthode qui retourne la somme de deux nombre complexes
    def ajouter(self, complex):
        return Complexe(self.getA() + complex.getA(), self.getB() + complex.getB())

    # La méthode qui retourne le produit de deux nombres complexes
    def produit(self, complex):
        a = self.getA()*complex.getA() - self.getB()*complex.getB()
        b = self.getA()*complex.getB() + self.getB()*complex.getA()
        return Complexe(a, b)

    # La méthode qui retourne le conjugué d'un nombre complexe
    def conjugue(self):
        return Complexe(self.getA(), - self.getB())

    # La méthode qui calcule le module d'un nombre complexe
    def module(self):
        return sqrt(self.getA()**2 + self.getB()**2)

    # La méthode qui retourne le carré d'un nombre complexe
    def carre(self):
        a = self.getA()**2 - self.getB()**2
        b = 2 * self.getA() * self.getB()
        return Complexe(a, b)

    # La méthode qui compare deux nombre complexes
    def comparer(self, complex):
        return True if self.getA() == complex.getA() and self.getB() == complex.getB() else False