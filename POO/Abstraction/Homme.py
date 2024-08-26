from Personne import Personne

class Homme(Personne):
    def __init__(self, nom, prenom):
        self.__nom = nom
        self.__prenom = prenom

    # def afficherGenre(self):
    #     print("Je suis un homme !")