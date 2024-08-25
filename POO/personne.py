class Personne():

    def __init__(self):
        self.__nom = "Someone"
        self.__prenom = "Nickname"
        self.__age = 1
        self.__profession = "Learner"
        self.__quartier = ""
        self.__ville = ""
        self.__pays = ""
        self.__tel = "+228 99 88 77 66"

    def sePresenter(self):
        return f"Je m'appelle {self.__nom} {self.__prenom}. J'ai {self.__age} an(s) et je suis {self.__profession}. Contactez-moi que le : {self.__tel}"

    def changerProfession(self, nvProfession):
        self.__profession = nvProfession

# setter => est une méthode qui vous permet de modifier la valeur d'un attribut private
# getter => est une méthode qui vous permet de retourner ou de lire la valeur d'un attribut private
# setter & getter sont appelés des accesseurs en POO

    def feterAnniversaire(self):
        self.__age += 1

    def getAge(self):
        return self.__age

    def setAge(self, nvAge):
        self.__age = nvAge

    def getNom(self):
        return self.__nom
