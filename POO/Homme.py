class Personne():

    def __init__(self):
        self.__nom = ""
        self.__prenom = ""
        self.__age = 0
        self.__profession = ""
        self.__quartier = ""
        self.__ville = ""
        self.__pays = ""
        self.__tel = 0

    def sePresenter(self):
        return f"Je m'appelle {self.__nom} {self.__prenom}. J'ai {self.__age} ans et je suis {self.__profession}."

    def changerProfession(self, nvProfession):
        self.__profession = nvProfession

    def feterAnniversaire(self):
        self.__age += 1

    def getAge(self):
        return self.__age

    def setAge(self, nvAge):
        self.__age = nvAge

    def getNom(self):
        return self.__nom


    

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

tom = Homme()

tom.setAge(25)
print(tom.getAge())
print(tom.getActivites())