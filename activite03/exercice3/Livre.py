"""
    Livre:
        * id_livre
        * titre
        * auteur
        * isbn
        * disponible
        * +disponible():boolean
        * +retourner():boolean
"""


class Livre:
    _increment:int = 0

    def __init__(self, titre:str, auteur:str, isbn:str, disponible:bool = True):
        Livre._increment += 1
        self.__id_livre = Livre._increment
        self.__titre:str = titre
        self.__auteur:str = auteur
        self.__isbn:str = isbn
        self.__disponible:bool = disponible

    def __str__(self):
        return f"Nom du livre : {self.getTitre()}\n\tAuteur : {self.getAuteur()}\n\tISBN : {self.getIsbn()}\n\tDisponible : {"Oui" if self.isDisponible() else "Non"}"

    def getIdLivre(self):
        return self.__id_livre

    def getTitre(self):
        return self.__titre

    def setTitre(self, titre:str):
        self.__titre = titre

    def getAuteur(self):
        return self.__auteur

    def setAuteur(self, auteur:str):
        self.__auteur = auteur

    def getIsbn(self):
        return self.__isbn

    def setIsbn(self, isbn:str):
        self.__isbn = isbn

    def isDisponible(self):
        return self.__disponible

    def emprunter(self):
        self.__disponible = False

    def retourner(self):
        self.__disponible = True
