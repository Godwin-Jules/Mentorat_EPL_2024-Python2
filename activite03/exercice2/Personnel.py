"""
    Personnel:
        * __employes
        * __commerciaux
        * __nom
        * +sommeDesSalaires()
"""

from Commercial import Commercial
from Employee import Employee


def sort_id(instance):
    return instance.getMatricule()

def sort_nom(instance):
    return instance.getNom()

def sort_prenom(instance):
    return instance.getPrenom()

def sort_salary(instance):
    return instance.calculSalaire()



class Personnel():
    def __init__(self, nom_entreprise, employes:list = [], commerciaux:list = []):
        self.__nom:str = nom_entreprise
        self.__employes:list[Employee] = employes
        self.__commerciaux:list[Commercial] = commerciaux

    def __str__(self):
        return f"Entreprise : {self.getNom()}\n\t-> Nombre d'employés : {len(self.getEmployes())}\n\t-> Nombre de commerciaux : {len(self.getCommerciaux())}"

    def getNom(self):
        return self.__nom

    def setNom(self, nom:str):
        self.__nom = nom

    def getEmployes(self):
        return self.__employes

    def setEmployes(self, employes:list):
        self.__employes = employes

    def getCommerciaux(self):
        return self.__commerciaux

    def setCommerciaux(self, commerciaux:list):
        self.__commerciaux = commerciaux

    def addEmploye(self, employe:Employee):
        employes:list = self.getEmployes()
        employes.append(employe)
        self.setEmployes(employes)

    def addEmployes(self, employees:list[Employee]):
        employes:list = self.getEmployes()
        for employe in employees:
            employes.append(employe)
        self.setEmployes(employes)

    def addCommercial(self, commercial:Commercial):
        commerciaux:list = self.getCommerciaux()
        commerciaux.append(commercial)
        self.setCommerciaux(commerciaux)

    def addCommerciaux(self, commerciaux:list[Commercial]):
        commercials:list = self.getCommerciaux()
        for com in commerciaux:
            commercials.append(com)
        self.setCommerciaux(commercials)

    def sommeDesSalaires(self):
        salaire_totale = 0
        for emp in self.getEmployes():
            salaire_totale += emp.calculSalaire()
        for com in self.getCommerciaux():
            salaire_totale += com.calculSalaire()
        return salaire_totale

    def totalDesVentes(self):
        total_ventes = 0
        for com in self.getCommerciaux():
            total_ventes += com.getVentes()
        # return total_ventes
        return sum(com.getVentes() for com in self.getCommerciaux())

    def beneficeDuMois(self):
        return self.totalDesVentes() - self.sommeDesSalaires()

    def afficherSommeDesSalaires(self):
        print(f"\nLa somme totale des salaires pour ce mois-ci est de : {self.sommeDesSalaires():.0f} F cfa")

    def afficherBeneficeDuMois(self):
        print(f"\nLe bénéfice de ce mois-ci est : {self.beneficeDuMois()} F cfa")

    def afficherListeDePaye(self):
        print("\n\t\t\tLISTE DE PAYE\n")
        print("\t* Liste de paye des employés")
        for emp in sorted(self.getEmployes(), key=sort_salary, reverse=True):
            print(f"\t\t> {emp.getNom():10s} {emp.getPrenom():12s} -> {emp.calculSalaire():10.0f} F cfa")
        print("\n\t* Liste de paye des commerciaux")
        for com in sorted(self.getCommerciaux(), key=sort_salary, reverse=True):
            print(f"\t\t> {com.getNom():10s} {com.getPrenom():12s} -> {com.calculSalaire():10.0f} F cfa")
