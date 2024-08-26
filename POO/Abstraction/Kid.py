from Homme import Homme

# Pour que cette classe fonctionne bien (cad si l'on veut créer des objets à partir de cette classe) il faut implémenter la méthode afficherGenre() qui est une méthode abstraite.
class Kid(Homme):

    def afficherGenre(self):
        print("Je suis un petit garçon !")