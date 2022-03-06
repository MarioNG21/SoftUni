class Animal:
    _sound = None
    _species = None

    def make_sound(self):
        return self._sound

    def get_species(self):
        return self._species


class Cat(Animal):
    _sound = "Meow"
    _species = 'cat'


class Dog(Animal):
    _sound = 'Woaf'
    _species = 'dog'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog(), Cat()]
animal_sound(animals)
