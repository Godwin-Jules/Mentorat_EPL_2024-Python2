"""
    Commercial extends Employee:
        * _proportion (attr de classe)
        * __salaireFixe
        * __ventes
        * +addVentes()
        * +calculSalaire() => @Override
"""

from Employee import Employee


class Commercial(Employee):
    _salaireFixe = 30_000
    _proportion = 0.18

    def __init__(self, nom:str, prenom:str, ventes:int = 0):
        super().__init__(nom, prenom, 0)
        self.__ventes = ventes

    def getVentes(self):
        return self.__ventes

    def setVentes(self, ventes):
        self.__ventes = ventes

    @classmethod
    def getSalaireFixe(cls):
        return cls._salaireFixe

    @classmethod
    def setSalaireFixe(cls, salaire_fixe):
        cls._salaireFixe = salaire_fixe

    @classmethod
    def getProportion(cls):
        return cls._proportion

    @classmethod
    def setProportion(cls, proportion):
        cls._proportion = proportion

    def calculSalaire(self):
        interessement = self.getVentes() * Commercial.getProportion()
        return self.getSalaireFixe() + interessement

