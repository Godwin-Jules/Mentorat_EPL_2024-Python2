"""
    Pokemon:
        * nom:str
        * hp:int
        * atk:int
        * +isDead():boolean
        * +attaquer(p:Pokemon)
        * +afficher()
        * +getClasse()
        * +getName()
        * +getSimpleName()
    PokemonFeu extends Pokemon:
        * atk*0.5 -> PokemonEau/PokemonFeu
        * atk*1   -> Pokemon
        * atk*2   -> PokemonPlante
        * +getClasse()
        * +getName()
        * +getSimpleName()
    PokemonEau extends Pokemon:
        * atk*0.5 -> PokemonEau/PokemonPlante
        * atk*1   -> Pokemon
        * atk*2   -> PokemonFeu
        * +getClasse()
        * +getName()
        * +getSimpleName()
    PokemonPlante extends Pokemon:
        * atk*0.5 -> PokemonPlante/PokemonFeu
        * atk*1   -> Pokemon
        * atk*2   -> PokemonEau
        * +getClasse()
        * +getName()
        * +getSimpleName()
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

    def getClasse(self):
        return Pokemon

    def getName(self):
        return type(self)

    def getSimpleName(self):
       return "Pokemon"

    def attaquer(self, p):      #type:ignore
        if p.getHp() - self.getAtk() > 0:
            p.setHp(p.getHp() - self.getAtk())
        else:
            p.setHp(0)

    def afficher(self):
        print(f"Pokemon : {self.getNom()} (HP = {self.getHp()}; ATK = {self.getAtk()})")



class PokemonFeu(Pokemon):
    def getClasse(self):
        return PokemonFeu

    def getName(self):
        return type(self)

    def getSimpleName(self):
        return "PokemonFeu"

    def attaquer(self, p:Pokemon):
        if p.isDead():
            print(f"{p.getNom()} est déjà mort")
        else:
            if p.getSimpleName() == "Pokemon":
                p.setHp(p.getHp() - self.getAtk())
            elif p.getSimpleName() == "PokemonPlante":
                p.setHp(p.getHp() - self.getAtk() * 2)
            else:
                p.setHp(int(p.getHp() - self.getAtk() * 0.5))

            if p.getHp() < 0:
                p.setHp(0)



class PokemonEau(Pokemon):
    def getClasse(self):
        return PokemonEau

    def getName(self):
        return type(self)

    def getSimpleName(self):
        return "PokemonEau"

    def attaquer(self, p:Pokemon):
        if p.isDead():
            print(f"{p.getNom()} est déjà mort")
        else:
            if p.getSimpleName() == "Pokemon":
                p.setHp(p.getHp() - self.getAtk())
            elif p.getSimpleName() == "PokemonFeu":
                p.setHp(p.getHp() - self.getAtk() * 2)
            else:
                p.setHp(int(p.getHp() - self.getAtk() * 0.5))

            if p.getHp() < 0:
                p.setHp(0)



class PokemonPlante(Pokemon):
    def getClasse(self):
        return PokemonPlante

    def getName(self):
        return type(self)

    def getSimpleName(self):
        return "PokemonPlante"

    def attaquer(self, p:Pokemon):
        if p.isDead():
            print(f"{p.getNom()} est déjà mort")
        else:
            if p.getSimpleName() == "Pokemon":
                p.setHp(p.getHp() - self.getAtk())
            elif p.getSimpleName() == "PokemonEau":
                p.setHp(p.getHp() - self.getAtk() * 2)
            else:
                p.setHp(int(p.getHp() - self.getAtk() * 0.5))

            if p.getHp() < 0:
                p.setHp(0)
