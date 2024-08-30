"""
    Responsable extends Employee:
        * attr as for Employe(__matricule, __nom, __prenom, __indiceSalarial)
        * __infHierarchique (liste des inférieurs hiérarchique directs)
        * +addInfHierarchique(employee)
        * +removeInfHierarchique(employee)
        * +afficherInfHierarchique()
"""

from Employee import Employee


def sort_id(instance):
    return instance.getMatricule()

def sort_nom(instance):
    return instance.getNom()

def sort_prenom(instance):
    return instance.getPrenom()

def sort_salary(instance):
    return instance.calculSalaire()



class Responsable(Employee):
    def __init__(self, nom:str, prenom:str, indice_salarial, inf_hierarchique:list):
        super().__init__(nom, prenom, indice_salarial)
        self.__infHierarchique = inf_hierarchique

    def getInfHierarchique(self):
        return self.__infHierarchique

    def setInfHierarchique(self, inf_hierarchique:list):
        self.__infHierarchique = inf_hierarchique

    def addInfHierarchique(self, employe:Employee):
        inferieurs:list = self.getInfHierarchique()
        inferieurs.append(employe)
        self.setInfHierarchique(inferieurs)

    def addInfHierarchiqueList(self, employes:list):
        for employe in employes:
            self.addInfHierarchique(employe)

    def removeInfHierarchique(self, employe_id:int):
        inferieurs:list = self.getInfHierarchique()
        for employe in inferieurs:
            if employe.getMatricule() == employe_id:
                inferieurs.remove(employe)
                break

    def afficherInferieurs(self):
        inferieurs:list = self.getInfHierarchique()
        inferieurs.sort(key=sort_nom)
        print(f"Les inférieurs hiérarchiques directs de {self.getNom()} {self.getPrenom()} sont :")
        for employe in inferieurs:
            print("\t=> ", employe)

