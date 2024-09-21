import time


def prepareCafe():
    print("Début - Préparation du café")
    time.sleep(3)
    print("Fin - Préparation du café")
    return "Le café est prêt"

def toasterPain():
    print("Début - Toast du pain")
    time.sleep(2)
    print("Fin - Toast du pain")
    return "Le pain est toasté"


def main():
    start_time = time.time()

    resultat_cafe = prepareCafe()
    resultat_pain = toasterPain()

    end_time = time.time()
    duration = end_time - start_time

    print(f"Résultat de prépareCafe() : {resultat_cafe}")
    print(f"Résultat de toasterPain() : {resultat_pain}")
    print(f"Temps total d'éxecution : {duration:.2f} secondes")


if __name__ == "__main__":
    main()