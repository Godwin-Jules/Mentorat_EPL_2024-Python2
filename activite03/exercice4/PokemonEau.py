"""
    PokemonEau extends Pokemon:
        * atk*0.5 -> PokemonEau/PokemonPlante
        * atk*1   -> Pokemon
        * atk*2   -> PokemonFeu
"""
from PokemonFeu import PokemonFeu
from PokemonPlante import PokemonPlante
from Pokemon import Pokemon


class PokemonEau(Pokemon):
    def attaquer(self, p:Pokemon):
        if p.isDead():
            print(f"{p.getNom()} est déjà mort")
        else:
            if isinstance(p, PokemonFeu):
                p.setHp(p.getHp() - self.getAtk() * 2)
            elif isinstance(p, (PokemonEau, PokemonPlante,)):
                p.setHp(int(p.getHp() - self.getAtk() * 0.5))
            else:
                p.setHp(p.getHp() - self.getAtk())

            if p.getHp() < 0:
                p.setHp(0)

