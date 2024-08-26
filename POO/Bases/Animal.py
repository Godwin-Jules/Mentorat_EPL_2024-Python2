class Animal:

    def __init__(self, nom="Unknown", espece="Animal", age=0, poids=0):
        self.nom = nom
        self.espece = espece
        self.age = age
        self.poids = poids

    def emettreSon(self):
        return "Criant"
