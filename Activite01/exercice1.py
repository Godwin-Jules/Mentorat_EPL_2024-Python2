"""Un programme qui, à partir de la saisie de deux réels et un opérateur affiche le résultat après exécution de l’opération choisie."""

# La fonction principale du programme
def main():
    """Un programme qui fait le calcul à partir de deux valeurs et d'un opérateur"""
    print("\n\t--- Programme de calcul de nombres ---")
    number_one = input("Votre premier nombre : ")   # le premier nombre
    number_two = input("Votre second nombre : ")    # le deuxième nombre
    user_operator = input("Choisissez votre opérateur de calcul [+, -, *, /] : ")   # l'opérateur de l'utilisateur
    try:
        result = eval(number_one+user_operator+number_two)  # eval permet d'évaluer une expression et de l'exécuter comme un code python
        print(f"\n\tOpération réussie : {number_one} {user_operator} {number_two} = {result}")
    except Exception as e:
        print("\n\tOpération impossible")
        print(e)

# Appel de la fonction principale du programme
main()