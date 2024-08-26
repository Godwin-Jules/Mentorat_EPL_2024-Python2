from exercice1 import Complexe

# Application de l'exercice 1
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