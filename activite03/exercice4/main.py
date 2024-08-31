from Pokemon import Pokemon
from PokemonEau import PokemonEau
from PokemonFeu import PokemonFeu
from PokemonPlante import PokemonPlante


# Application de l'exercice 4
pk1 = Pokemon("pokemon 1")
pk2 = PokemonFeu("PokemonFeu 1")
pk3 = PokemonFeu("PokemonFeu 2")
pk4 = PokemonEau("PokemonEau 1")
pk5 = PokemonPlante("PokemonPlante 1")

# Affichage avant attaques
print("Etat des pokémons avant les attaques")
pk1.afficher()
pk2.afficher()
pk3.afficher()
pk4.afficher()
pk5.afficher()

pk2.attaquer(pk1)   # pk1 = 90, pk2 = 100
pk3.attaquer(pk1)   # pk1 = 80, pk3 = 100
pk4.attaquer(pk1)   # pk1 = 70, pk4 = 100
pk5.attaquer(pk1)   # pk1 = 60, pk5 = 100

pk1.attaquer(pk2)   # pk1 = 60, pk2 =  90
pk1.attaquer(pk3)   # pk1 = 60, pk3 =  90
pk1.attaquer(pk4)   # pk1 = 60, pk4 =  90
pk1.attaquer(pk5)   # pk1 = 60, pk5 =  90

pk2.attaquer(pk5)   # pk2 = 90, pk5 = 70
pk2.attaquer(pk3)   # pk2 = 90, pk3 = 85
pk5.attaquer(pk2)   # pk2 = 85, pk5 = 70
pk4.attaquer(pk3)   # pk3 = 65, pk4 = 90

# Afffichage après attaques
print("\nEtat des pokémons après les attaques")
pk1.afficher()
pk2.afficher()
pk3.afficher()
pk4.afficher()
pk5.afficher()