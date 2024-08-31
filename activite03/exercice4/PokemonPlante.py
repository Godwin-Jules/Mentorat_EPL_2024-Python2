"""
    PokemonPlante extends Pokemon:
        * atk*0.5 -> PokemonPlante/PokemonFeu
        * atk*1   -> Pokemon
        * atk*2   -> PokemonEau
"""
from PokemonEau import PokemonEau
from PokemonFeu import PokemonFeu
from Pokemon import Pokemon


class PokemonPlante(Pokemon):
    def attaquer(self, p:Pokemon):
        if p.isDead():
            print(f"{p.getNom()} est déjà mort")
        else:
            if isinstance(p, PokemonEau):
                p.setHp(p.getHp() - self.getAtk() * 2)
            elif isinstance(p, (PokemonPlante, PokemonFeu,)):
                p.setHp(int(p.getHp() - self.getAtk() * 0.5))
            else:
                p.setHp(p.getHp() - self.getAtk())

            if p.getHp() < 0:
                p.setHp(0)
