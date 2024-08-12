"""Première partie du jeu de Devinette"""

from random import randint as rd_int

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
    while True:
        try:
            max_value = int(input("Quelle sera la valeur maximale : "))
            break
        except Exception as e:
            print("Saisie incorrecte")
            print(e, "\n")
    mystery_number = rd_int(0, max_value)
    game(mystery_number)


# Appel de la fonction principale du programme
main()