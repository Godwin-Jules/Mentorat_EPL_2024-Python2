import time
import asyncio


async def prepareCafe():
    print("Début - Préparation du café")
    await asyncio.sleep(3)
    print("Fin - Préparation du café")
    return "Le café est prêt"

async def toasterPain():
    print("Début - Toast du pain")
    await asyncio.sleep(2)
    print("Fin - Toast du pain")
    return "Le pain est toasté"


async def main():
    start_time = time.time()

    batch = asyncio.gather(prepareCafe(), toasterPain())

    resultat_cafe, resultat_pain = await batch

    end_time = time.time()
    duration = end_time - start_time

    print(f"Résultat de prépareCafe() : {resultat_cafe}")
    print(f"Résultat de toasterPain() : {resultat_pain}")
    print(f"Temps total d'éxecution : {duration:.2f} secondes")


if __name__ == "__main__":
    asyncio.run(main())