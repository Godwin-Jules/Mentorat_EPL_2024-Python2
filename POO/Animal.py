class Animal:

    def __init__(self, nom="", espece="animal", age=0, poids=0):
        self.nom = nom
        self.espece = espece
        self.age = age
        self.poids = poids

    def emettreSon(self):
        return "Criant"

class Chat(Animal):
    def __init__(self, nom="", espece="", age=0, poids=0):
        super().__init__(nom, espece, age, poids)

    def emettreSon(self):
        return "Miyaou"

class Chien(Animal):
    def __init__(self, nom="", espece="", age=0, poids=0):
        super().__init__(nom, espece, age, poids)

    def emettreSon(self):
        return "Ouaf"


animal = Animal() # type:ignore
chat = Chat("Miwou", "chat")
chien = Chien("Qui c'est", "chien", 2, 5)

print(chat.emettreSon())        # Animal(emettreSon) - Chat(emettreSon)
print(chien.emettreSon())
print(animal.emettreSon())