from Animal import Animal

class Chat(Animal):
    def __init__(self, nom="Unknown", age=0, poids=0):
        super().__init__(nom, "Chat", age, poids)

    def emettreSon(self):
        return "Miyaou"
