class Mammal:
    _kingdom = 'animals'

    def __init__(self, name, type, sound):
        self.name = name
        self.type = type
        self.sound = sound

    def make_sound(self):
        return  f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return self._kingdom.capitalize()

    def info(self):
        return f"{self.name} is of type {self.type}"

class Tiger(Mammal):
    _kingdom = 'putki'
    def __init__(self, name, type, sound):
        super().__init__(name, type, sound)

mammal = Tiger("Dog", "Domestic", "Bark")
print(mammal.make_sound())
print(mammal.get_kingdom())
print(mammal.info())
