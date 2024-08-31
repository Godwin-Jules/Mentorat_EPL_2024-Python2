"""
    Pokemon:
        * nom:str
        * hp:int
        * atk:int
        * +isDead():boolean
        * +attaquer(p:Pokemon)
        * +afficher()
"""

class Pokemon:
    def __init__(self, nom:str, hp:int=100, atk:int=10):
        self.__nom:str = nom
        self.__hp:int = hp
        self.__atk:int = atk

    def __str__(self):
        return self.getNom()

    def getNom(self):
        return self.__nom

    def setNom(self, nom:str):
        self.__nom = nom

    def getHp(self):
        return self.__hp

    def setHp(self, hp:int):
        self.__hp = hp

    def getAtk(self):
        return self.__atk

    def setAtk(self, atk:int):
        self.__atk = atk

    def isDead(self):
        return self.__hp == 0

    def attaquer(self, p:Pokemon):      #type:ignore
        if p.getHp() - self.getAtk() > 0:
            p.setHp(p.getHp() - self.getAtk())
        else:
            p.setHp(0)

    def afficher(self):
        print(f"Pokemon : {self.getNom()} (HP = {self.getHp()}; ATK = {self.getAtk()})")

