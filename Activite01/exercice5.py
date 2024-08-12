"""Dernière partie du jeu de Devinette"""

from random import randint as rd_int
from math import sqrt
import os

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

# Message de félicitations
CONGRATULATIONS = {
    1: "Super Voyant",          #   [1 - 3] tentatives
    2: "Sage Voyant",           #   [4 - 6] tentatives
    3: "Apprenti Voyant",       #   [7 - 9] tentatives
    4: "Pusillanime"            #   [10 et +] tentatives
}

# Une liste qui repertorie toutes les tentatives de chaque niveau de jeu joué si le joueur a finalement trouvé le nombre mystère
TENTATIVES = []

# Une liste qui repertorie l'historique de toutes les tentatives
HISTORY = {
    "facile": [],
    "moyen": [],
    "difficile": []
}

# Nombre maximal d'essaie autorisé
MAX_TRY = 15

# La fonction qui détermine le message de félicitation
def get_congrats(attempt, mystery_number, found=False):

    print("\t\t - Nombre de tentatives :", attempt)
    if attempt in [1, 2, 3]:
        print("\t\t - Appréciation : ", CONGRATULATIONS[1])
        print("\t\t - Trouvé :", ("Oui" if found else "Non"))
        print("\t\t - Nombre mystère :", mystery_number)
    elif attempt in [4, 5, 6]:
        print("\t\t - Appréciation : ", CONGRATULATIONS[2])
        print("\t\t - Trouvé :", ("Oui" if found else "Non"))
        print("\t\t - Nombre mystère :", mystery_number)
    elif attempt in [7, 8, 9]:
        print("\t\t - Appréciation : ", CONGRATULATIONS[3])
        print("\t\t - Nombre mystère trouvé :", ("Oui" if found else "Non"))
        print("\t\t - Nombre mystère :", mystery_number)
    else:
        print("\t\t - Appréciation : ", CONGRATULATIONS[4])
        print("\t\t - Trouvé :", ("Oui" if found else "Non"))
        print("\t\t - Nombre mystère :", mystery_number)

    print("\t\t - Score final :", get_score(attempt), "%")

# Une fonction qui repertorie l'historique
def append_history(level, mystery_number, nb_attempts, found=False):
    history_data = {
        'mystery_number': mystery_number,   # Le nombre mystère de la partie
        'attempt': nb_attempts,         # Le nombre de tentatives de la partie
        'score': get_score(nb_attempts),    # Le score de la partie
        'found': found,                     # Si le joueur a finalement trouvé le nombre mystère
    }
    HISTORY[level].append(history_data)

# La fonction qui calcule la moyenne
def average(tentatives = TENTATIVES):
    return round(sum(tentatives) / len(tentatives), 2) if len(tentatives) > 0 else None

# La fonction qui calcule l'écart-type (standard deviation)
def deviation(tentatives = TENTATIVES):
    avg = average(tentatives)
    variance = sum((x - avg)**2 for x in tentatives) / len(tentatives) if len(tentatives) > 0 else None
    """Equivalence du code de la ligne précédente
        somme = 0
        for x in tentatives:
            somme += (x - avg)**2
        variance = somme / len(tentatives)
    """
    return round(sqrt(variance), 2) if variance != None else 0

# La fonction qui calcule la moyenne olympique
def olympic_avg(tentatives = TENTATIVES):
    tentatives = sorted(tentatives) # Classement des éléments par ordre croissant
    if len(tentatives) <= 2:
        return None
    return average(tentatives[1:-1])    # Prendre tous les éléments de la liste sauf la première et et la dernière

# La fonction qui calcule le score
def get_score(nb_attempts):
    return round( ((1 - nb_attempts / MAX_TRY) * 100), 2)

# La fonction qui exécute la logique du jeu
def game(mystery_number, level):

    found = False
    attempt = 0
    levels = list(HISTORY.keys())

    while attempt < MAX_TRY:
        print(f"\nIl vous reste {MAX_TRY - attempt} tentative(s)")
        attempt += 1
        try:
            user_value = int(input("Quel est le nombre mystère ? "))
        except:
            print("Saisie incorrecte")
            continue
        if user_value < mystery_number:
            if attempt == 15:
                append_history(levels[level - 1], mystery_number, attempt)
                continue
            print(f"Le nombre mystère est plus grand que {user_value}")
        elif user_value > mystery_number:
            if attempt == 15:
                append_history(levels[level - 1], mystery_number, attempt)
                continue
            print(f"Le nombre mystère est plus petit que {user_value}")
        else:
            found = True
            TENTATIVES.append(attempt)
            append_history(levels[level - 1], mystery_number, attempt, found)
            break

    print("\n\tFin de la partie")
    get_congrats(attempt, mystery_number, found)

# La fonction qui affiche l'historique
def show_history():
    if os.name == 'nt':     # Pour les systèmes Windows
        os.system('cls')
    else:                   # Pour les systèmes Linux et MacOS
        os.system('clear')

    avg_olympic = olympic_avg()
    total_trial = sum(len(HISTORY[x]) for x in HISTORY)
    total_trial_success = len(TENTATIVES)
    list_score_success = [trial for level in HISTORY for trial in HISTORY[level] if trial['found']]
    # Equivalence du code de la ligne précédente
    # list_score_success = []
    # for level in HISTORY:
    #     for trial in HISTORY[level]:
    #         if trial['found']:
    #             list_score_success.append(trial)
    global_score = average([trial['score'] for trial in list_score_success ])
    # Equivalence du code de la ligne précédente
    # list_scores = []
    # for trial in list_score_success:
    #     list_scores.append(trial['score'])

    print("\n\t--- Historique du Jeu ---\n")
    print("> Nombre de parties jouées :", total_trial)
    print("\t + Facile :", len(HISTORY["facile"]))
    print("\t + Moyen :", len(HISTORY["moyen"]))
    print("\t + Difficile :", len(HISTORY["difficile"]))
    print("> Nombre de parties réussies :", total_trial_success)

    print("\t + Facile")
    if HISTORY['facile']:
        for id, trial in enumerate(HISTORY['facile']):
            print("\t\tPartie", id+1, ":")
            get_congrats(trial['attempt'], trial['mystery_number'], trial['found'])

    print("\t + Moyen")
    if HISTORY['moyen']:
        for id, trial in enumerate(HISTORY['moyen']):
            print("\t\tPartie", id+1, ":")
            get_congrats(trial['attempt'], trial['mystery_number'], trial['found'])

    print("\t + Difficile")
    if HISTORY['difficile']:
        for id, trial in enumerate(HISTORY['difficile']):
            print("\t\tPartie", id+1, ":")
            get_congrats(trial['attempt'], trial['mystery_number'], trial['found'])

    print("> Score global :", ("Aucune réussite enregistrée" if global_score == None else global_score), "%")
    print("> Ecart-type :", deviation())
    print("> Moyenne Olympique :", ("Données insuffisantes pour une moyenne olympique" if avg_olympic == None else avg_olympic))

# La fonction principale du programme
def main():
    """Première partie du jeu de Devinette"""

    while True:
        if os.name == 'nt':     # Pour les systèmes Windows
            os.system('cls')
        else:                   # Pour les systèmes Linux et MacOS
            os.system('clear')

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

        game(mystery_number, user_level)
        try:
            replay = input("Voulez-vous rejouer ? ([O, o, Y, y] = oui) ")
            if replay in ['O', 'o', 'Y', 'y']:
                continue
            else:
                break
        except Exception as e:
            break

    show_history()


# Appel de la fonction principale du programme
main()
