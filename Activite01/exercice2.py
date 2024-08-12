"""Programme de calcul de la distance entre deux points A(xa, ya) et B(xb, yb)"""

from math import sqrt

# La fontion qui permet de récupérer les coordonnées d'un point
def point_entry(name):
    while True:
        try:
            x = float(input(f"\nAbscisse du point {name} : "))
            y = float(input(f"Ordonnée du point {name} : "))
            return x, y     # les coordonnées du point
        except Exception as e:
            print("Saisie incorrecte. Veuillez reprendre !")
            print(e)

# La fonction principale
def main():
    """Un programme qui fait le calcul de la distance entre deux points A et B"""
    print("\n\tCalcul de la distance entre deux points A(xa, ya) et B(xb, yb)")
    xa, ya = point_entry('A')
    xb, yb = point_entry('B')
    distance = sqrt((xa - xb)**2 + (ya - yb)**2)
    print(f"Calcul effectué : d(A,B) = {distance}")

# Appel de la fonction principale du programme
main()