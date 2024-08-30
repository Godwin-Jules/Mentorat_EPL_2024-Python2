from Livre import Livre
from Membre import Membre
from Bibliotheque import Bibliotheque


# Application de l'exercice 3
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