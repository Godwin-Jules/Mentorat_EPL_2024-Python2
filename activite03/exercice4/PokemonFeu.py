"""
    PokemonFeu extends Pokemon:
        * atk*0.5 -> PokemonEau/PokemonFeu
        * atk*1   -> Pokemon
        * atk*2   -> PokemonPlante
"""
from PokemonEau import PokemonEau
from PokemonPlante import PokemonPlante
from Pokemon import Pokemon


class PokemonFeu(Pokemon):
    def attaquer(self, p:Pokemon):
        if p.isDead():
            print(f"{p.getNom()} est déjà mort")
        else:
            if isinstance(p, PokemonPlante):
                p.setHp(p.getHp() - self.getAtk() * 2)
            elif isinstance(p, (PokemonFeu, PokemonEau)):
                p.setHp(int(p.getHp() - self.getAtk() * 0.5))
            else:
                p.setHp(p.getHp() - self.getAtk())

            if p.getHp() < 0:
                p.setHp(0)

