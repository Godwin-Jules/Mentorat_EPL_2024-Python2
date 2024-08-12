"""Deuxième partie du jeu de Devinette"""

from random import randint as rd_int

# Un dictionnaire qui contient les niveaux et leur information
LEVELS = {
    1: "Facile (0 - 100)",
    2: "Moyen (0 - 500)",
    3: "Difficle (0 - 1000)"
}
# Un dictionnaire qui contient la valeur maximale de chaque niveau
MAX_VALUE = {
    1: 100,
    2: 500,
    3: 1000
}


# La fonction qui exécute la logique du jeu
def game(mystery_number):

    attempt = 0
    while True:
        attempt += 1
        user_value = int(input("Quel est le nombre mystère ? "))
        if user_value < mystery_number:
            print(f"Le nombre mystère est plus grand que {user_value}")
        elif user_value > mystery_number:
            print(f"Le nombre mystère est plus petit que {user_value}")
        else:
            print(f"Bravo, vous avez trouvé le nombre mystère {mystery_number} en {attempt} tentative(s)")
            break


# La fonction principale du programme
def main():
    """Première partie du jeu de Devinette"""
    print("\n\t--- Jeu de Devinette ---\n")
    print("Veuillez choisir un niveau!\n")
    print(f"\t[1] - Niveau {LEVELS[1]}")
    print(f"\t[2] - Niveau {LEVELS[2]}")
    print(f"\t[3] - Niveau {LEVELS[3]}\n")
    user_level = input("Votre choix : ")

    try:
        user_level = int(user_level)
        if user_level not in [1, 2, 3]:
            print(f"Niveau par défaut : {LEVELS[2]}")
            user_level = 2
        else:
            print(f"Niveau {LEVELS[user_level]}")
    except:
        print(f"Niveau par défault : {LEVELS[2]}")
        user_level = 2

    max_value = MAX_VALUE[user_level]
    mystery_number = rd_int(0, max_value)
    game(mystery_number)


# Appel de la fonction principale du programme
main()