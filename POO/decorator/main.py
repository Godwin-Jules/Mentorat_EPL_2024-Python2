from Rectangle import Rectangle


# """
# Essai avec les décorateurs
# def my_decorator(func):
#     print("Beginning of the decorator")
#     func()
#     print("Completed")

def deco(func):
    def wrapper():
        print("Starting of the decoration")
        func()
        print("End of the decoration")
    return wrapper


def my_decorator(func):
    @deco
    @deco
    @deco
    def wrapper():
        print("Beginning of the decorator")
        func()
        print("Completed")
    return wrapper

@my_decorator
def base_function():
    print("This is the base function")

base_function()
# """


""""
def deco_of_deco(func):
    def wrapper(*args, **kwargs):
        print("Decorating \"add_meat\" function!")
        func(*args, **kwargs)
        print("End of the decoration")
    return wrapper

@deco_of_deco
def add_meat(func):
    def wrapper(*args, **kwargs):
        print("On t'ajoute de la viande")
        func(*args, **kwargs)
    return wrapper

def add_drink(func):
    def wrapper(*args, **kwargs):
        print("On t'ajoute une boisson bien fraîche")
        func(*args, **kwargs)
    return wrapper

def add_dessert(func):
    def wrapper(*args, **kwargs):
        print("On t'ajoute un un bon dessert 🍨")
        func(*args, **kwargs)
    return wrapper


@add_meat
@add_drink
@add_dessert
def bouillie(repas):
    print(f"Voici ton plat de {repas} 😎. Bon appétit !")


print(bouillie("riz"))
"""


"""
# Le décorateur @property
rectangle = Rectangle(15, 12)

print(rectangle.longueur)
print(rectangle.largeur)

rectangle.longueur = -1
rectangle.largeur = 0

rectangle._longueur = 7
rectangle._largeur = 5

print(rectangle.longueur)
print(rectangle.largeur)

print("\n\nAvant la suppression\n\n")
print(dir(rectangle), "\n")

del rectangle.longueur
del rectangle.largeur

print("\nAprès la suppression\n\n")
print(dir(rectangle), "\n")

print(rectangle.longueur)
print(rectangle.largeur)
"""