from abc import ABC, abstractmethod

#Classe abstraite
class Personne(ABC):

    @abstractmethod
    def afficherGenre(self):
        pass