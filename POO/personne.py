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

tom = Personne()        # Création d'un objet de la classe Personne ou instanciation
jules = Personne()
daniel = Personne()
illane = Personne()
abdoul = Personne()


print(tom.sePresenter())
print(tom.getAge())