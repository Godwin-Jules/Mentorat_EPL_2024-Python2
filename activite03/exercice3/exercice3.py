"""
    Livre:
        * id_livre
        * titre
        * auteur
        * isbn
        * disponible
        * +disponible():boolean
        * +retourner():boolean
    Membre:
        * id_membre
        * nom
        * prenom
        * livres_empruntes
        * +emprunter_livre(livre:Livre):boolean
        * +retourner_livre(livre:Livre):boolean
    Bibliotheque:
        * nom
        * livres
        * membres
        * +ajouter_livre(livre:Livre)
        * +inscrire_membre(membre:Membre)
        * +lister_livres_disponibles()
        * +lister_livres_empruntes()
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