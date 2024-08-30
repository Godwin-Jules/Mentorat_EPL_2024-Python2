"""
    Bibliotheque:
        * nom
        * livres
        * membres
        * +ajouter_livre(livre:Livre)
        * +inscrire_membre(membre:Membre)
        * +lister_livres_disponibles()
        * +lister_livres_empruntes()
"""

from Livre import Livre
from Membre import Membre

class Bibliotheque:
    def __init__(self, nom:str, livres:list[Livre] = [], membres:list[Membre] = []):
        self.__nom:str = nom
        self.__livres:list[Livre] = livres
        self.__membres:list[Membre] = membres

    def __str__(self):
        return f"Bibliothèque : {self.getNom()}\n\tNombre de livres : {len(self.getLivres())}\n\tNombre de membres : {len(self.getMembres())}"

    def getNom(self):
        return self.__nom

    def setNom(self, nom:str):
        self.__nom = nom

    def getLivres(self):
        return self.__livres

    def setLivres(self, livres:list[Livre]):
        self.__livres = livres

    def getMembres(self):
        return self.__membres

    def setMembres(self, membres:list[Membre]):
        self.__membres = membres

    def ajouter_livre(self, livre:Livre):
        livres = self.getLivres()
        livres.append(livre)
        self.setLivres(livres)

    def ajouter_livres(self, livres:list[Livre]):
        books = self.getLivres()
        for livre in livres:
            books.append(livre)
        self.setLivres(books)

    def inscrire_membre(self, membre:Membre):
        membres = self.getMembres()
        membres.append(membre)
        self.setMembres(membres)

    def inscrire_membres(self, membres:list[Membre]):
        members = self.getMembres()
        for membre in membres:
            members.append(membre)
        self.setMembres(members)

    def lister_livres_disponibles(self):
        livres_disponibles = [livre for livre in self.getLivres() if livre.isDisponible()]
        return livres_disponibles

    def lister_livres_empruntes(self):
        livres_empruntes = [livre for livre in self.getLivres() if not livre.isDisponible()]
        return livres_empruntes