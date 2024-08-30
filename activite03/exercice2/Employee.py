"""
    Employee:
        * _taux (attr de classe)
        * __nom
        * __matricule (unique)
        * __indiceSalarial (indice salarial)
        * +calculSalaire()
            Salaire: __indiceSalarial * _taux
"""

class Employee:
    _increment:int = 0
    _taux:int = 1300

    def __init__(self, nom:str, prenom:str, indice_salarial:int):
        Employee._increment += 1
        self.__matricule = Employee._increment
        self.__nom = nom
        self.__prenom = prenom
        self.__indiceSalarial = indice_salarial

    def __str__(self):
        return f"N° Matricule : {self.getMatricule():3d} => Employé : {self.getNom():15s} {self.getPrenom()}"

    def getMatricule(self):
        return self.__matricule

    def getNom(self):
        return self.__nom

    def setNom(self, nom:str):
        self.__nom = nom

    def getPrenom(self):
        return self.__prenom

    def setPrenom(self, prenom:str):
        self.__prenom = prenom

    def getIndiceSalarial(self):
        return self.__indiceSalarial

    def setIndiceSalarial(self, indice_salarial:int):
        self.__indiceSalarial = indice_salarial

    @classmethod
    def getTaux(cls):
        return cls._taux

    @classmethod
    def setTaux(cls, taux:int):
        cls._taux = taux

    def calculSalaire(self):
        return self.getIndiceSalarial() * Employee.getTaux()
