from exercice1.exercice1 import Complexe
from exercice2.exercice2 import *
from exercice3.exercice3 import *
from exercice4.exercice4 import *



# Application de l'exercice 1
print("\n=================== APPLICATION DE L'EXERCICE 1 ===================\n\n")
nb1 = Complexe(1, -1)
nb2 = Complexe(2, 4)

somme = nb1.ajouter(nb1)
produit = nb1.produit(nb2)
conjugue = nb1.conjugue()
module = nb1.module()
carre = nb1.carre()

print(somme)
print(produit)
print(conjugue)
print(module)
print(carre)
print(nb1.comparer(nb2))
print(Complexe())


# Application de l'exercice 2
print("\n\n\n=================== APPLICATION DE L'EXERCICE 2 ===================\n\n")
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


# Application de l'exercice 3
print("\n\n\n=================== APPLICATION DE L'EXERCICE 3 ===================\n\n")
livre1 = Livre("Automate the Boring Stuff with Python", "Al Sweigart", "978-1-59327-992-9")
livre2 = Livre("L'art de négocier", "Dag Heward-Mills", "978-2-212-54434-3")
livre3 = Livre("English Grammar in Use", "Raymond Murphy", "978-1-108-58662-7")
livre4 = Livre("English Grammar", "Evelyn P. Altenberg & Robert M. Vago", "978-0-511-72945-4")

membre1 = Membre("MILEGNE", "Dieu donné")
membre2 = Membre("TOM", "Jerry")
membre3 = Membre("KOMELI", "Kathy")

biblio = Bibliotheque("LA CONNAISSANCE")
biblio.ajouter_livres([livre1, livre2, livre3, livre4])
biblio.inscrire_membres([membre1, membre2, membre3])
membre1.emprunter_livre(livre1)
print(livre1)
print(membre1)
print(biblio)
print(biblio)
print(membre1.emprunter_livre(livre1))


# Application de l'exercice 4
print("\n\n\n=================== APPLICATION DE L'EXERCICE 4 ===================\n\n")
pk1 = Pokemon("pokemon 1")
pk2 = PokemonFeu("PokemonFeu 1")
pk3 = PokemonFeu("PokemonFeu 2")
pk4 = PokemonEau("PokemonEau 1")
pk5 = PokemonPlante("PokemonPlante 1")

# Affichage avant attaques
print("Etat des pokémons avant les attaques")
pk1.afficher()
pk2.afficher()
pk3.afficher()
pk4.afficher()
pk5.afficher()

pk2.attaquer(pk1)   # pk1 = 90, pk2 = 100
pk3.attaquer(pk1)   # pk1 = 80, pk3 = 100
pk4.attaquer(pk1)   # pk1 = 70, pk4 = 100
pk5.attaquer(pk1)   # pk1 = 60, pk5 = 100

pk1.attaquer(pk2)   # pk1 = 60, pk2 =  90
pk1.attaquer(pk3)   # pk1 = 60, pk3 =  90
pk1.attaquer(pk4)   # pk1 = 60, pk4 =  90
pk1.attaquer(pk5)   # pk1 = 60, pk5 =  90

pk2.attaquer(pk5)   # pk2 = 90, pk5 = 70
pk2.attaquer(pk3)   # pk2 = 90, pk3 = 85
pk5.attaquer(pk2)   # pk2 = 85, pk5 = 70
pk4.attaquer(pk3)   # pk3 = 65, pk4 = 90

# Afffichage après attaques
print("Etat des pokémons après les attaques")
pk1.afficher()
pk2.afficher()
pk3.afficher()
pk4.afficher()
pk5.afficher()