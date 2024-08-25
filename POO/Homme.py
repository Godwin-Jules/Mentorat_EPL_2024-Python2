from Personne import Personne

class Homme(Personne):
    __activites = {
        "Football",
        "Manga",
        "Tennis",
        "Basketball",
    }

    def __init__(self):
        super().__init__()
        self.__sexe = 'M'

    def getActivites(self):
        return self.__activites

