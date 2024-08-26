from Animal import Animal

class Chien(Animal):
    def __init__(self, nom="Unknown", age=0, poids=0):
        super().__init__(nom, "Chien", age, poids)

    def emettreSon(self):
        return "Wouf"
