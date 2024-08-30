"""
    Membre:
        * id_membre
        * nom
        * prenom
        * livres_empruntes
        * +emprunter_livre(livre:Livre):boolean
        * +retourner_livre(livre:Livre):boolean
"""

from Livre import Livre

class Membre:
    _increment = 0

    def __init__(self, nom:str, prenom:str, livres_empruntes:list[Livre] = []):
        Membre._increment += 1
        self.__id_membre = Membre._increment
        self.__nom:str = nom
        self.__prenom:str = prenom
        self.__livres_empruntes:list = livres_empruntes

    def __str__(self):
        return f"Membre : {self.getNom()} {self.getPrenom()}"

    def getIdMembre(self):
        return self.__id_membre

    def getNom(self):
        return self.__nom

    def setNom(self, nom:str):
        self.__nom = nom

    def getPrenom(self):
        return self.__prenom

    def setPrenom(self, prenom:str):
        self.__prenom = prenom

    def getLivresEmpruntes(self):
        return self.__livres_empruntes

    def setLivresEmpruntes(self, livres_empruntes:list[Livre]):
        self.__livres_empruntes = livres_empruntes

    def emprunter_livre(self, livre:Livre):
        if livre.isDisponible():
            livres_empruntes = self.getLivresEmpruntes()
            livre.emprunter()
            livres_empruntes.append(livre)
            self.setLivresEmpruntes(livres_empruntes)
            return True
        else:
            return False

    def retourner_livre(self, livre:Livre):
        livres_empruntes = self.getLivresEmpruntes()
        if livre in livres_empruntes:
            livres_empruntes.remove(livre)
            self.setLivresEmpruntes(livres_empruntes)
            return True
        else:
            return False
