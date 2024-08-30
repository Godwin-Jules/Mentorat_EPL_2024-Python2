from Employee import Employee
from Commercial import Commercial
from Responsable import Responsable
from Personnel import Personnel


# Application de l'exercice 2
com6 = Commercial("TREVOR", "Albertine", 180_000)
emp1 = Employee("KOKOU", "Komi", 245)
emp2 = Employee("AKAKPO", "Komla", 305)
emp3 = Employee("EKLOU", "Justin", 275)
com1 = Commercial("KPODAR", "Ferdinard", 815_000)
emp8 = Employee("KOEWOU", "Albertine", 255)
com7 = Commercial("AKOU", "Kafui", 214_000)
com4 = Commercial("KOKOROKO", "Claire", 745_000)
emp4 = Employee("DEVOR", "Kossi", 291)
emp5 = Employee("VALERE", "Dupont", 315)
com8 = Commercial("SENYO", "Robert", 18_500)
com9 = Commercial("AMEFATO", "Mawussi", 596_200)
emp6 = Employee("KELVIN", "Afiwa", 259)
com3 = Commercial("GANYO", "Liliane", 495_300)
emp7 = Employee("ZILOSTER", "Denzel", 455)
com10 = Commercial("KAFOUM", "Edoudjinam", 745_450)
emp9 = Employee("KLOBER", "Evelyne", 378)
com5 = Commercial("LOPEZ", "deborah", 1_603_450)
com2 = Commercial("KPEVI", "Modeste", 1_009_800)
emp10 = Employee("DEVOR", "Kossi", 401)

resp = Responsable("MILEGNE", "Dieu donné", 984, [])
dev_poo = Personnel("DevPOO")

employes = [emp1, emp2, emp3, emp4, emp5, emp6, emp7, emp8, emp9, emp10]
commerciaux = [com1, com2, com3, com4, com5, com6, com7, com8, com9, com10]

resp.addInfHierarchiqueList(employes)
resp.addInfHierarchiqueList(commerciaux)

dev_poo.addEmploye(resp)
dev_poo.addEmployes(employes)
dev_poo.addCommerciaux(commerciaux)

resp.afficherInferieurs()

dev_poo.afficherSommeDesSalaires()
dev_poo.afficherBeneficeDuMois()
dev_poo.afficherListeDePaye()
