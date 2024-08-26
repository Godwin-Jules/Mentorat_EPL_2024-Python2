from Personne import Personne
from Homme import Homme
from Animal import Animal
from Chien import Chien
from Chat import Chat


# Manipulation des objets `Personne`
tom = Personne()        # Création d'un objet de la classe Personne ou instanciation
jules = Personne()
daniel = Personne()
illane = Personne()
abdoul = Personne()

print(tom.sePresenter())
print(tom.getAge())

tom = Homme()
tom.setAge(25)
print(tom.getAge())
print(tom.getActivites())


# Manimpulation des objets `Animal` `Chien` `Chat`
animal = Animal()
chat = Chat("Miwou")
chien = Chien("Qui c'est", 2, 5)

print(animal.emettreSon())        # Animal(emettreSon) - Chat(emettreSon)
print(chien.emettreSon())
print(chat.emettreSon())
