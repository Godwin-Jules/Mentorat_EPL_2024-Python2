"""
    Employee:
        * _taux (attr de classe)
        * __nom
        * __matricule (unique)
        * __indiceSalarial (indice salarial)
        * +calculSalaire()
            Salaire: __indiceSalarial * _taux

    Responsable extends Employee:
        * attr as for Employe(__matricule, __nom, __prenom, __indiceSalarial)
        * __infHierarchique (liste des inférieurs hiérarchique directs)
        * +addInfHierarchique(employee)
        * +removeInfHierarchique(employee)
        * +afficherInfHierarchique()

    Commercial extends Employee:
        * _proportion (attr de classe)
        * __salaireFixe
        * __ventes
        * +addVentes()
        * +calculSalaire() => @Override

    Personnel:
        * __employes
        * __commerciaux
        * __nom
        * +sommeDesSalaires()
"""

def sort_id(instance):
    return instance.getMatricule()

def sort_nom(instance):
    return instance.getNom()

def sort_prenom(instance):
    return instance.getPrenom()

def sort_salary(instance):
    return instance.calculSalaire()

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
