class StrDicMixin:
    def __str__(self):
        return ', '.join(f"{key}: {value}" for (key, value) in self.__dict__.items())


class Person(StrDicMixin):
    def __init__(self, name):
        if not name:
            raise ValueError("Person name cannot be None or empty space")
        self.name = name
        self.hobbies = set()

    def add_hobby(self, hobby):
        self.hobbies.add(hobby)

    def __str__(self):
        return super().__str__()

class SoftwareDeveloper(Person):
    def __init__(self, name):
        super().__init__(name)
        self.add_hobby('Lego')
        self.add_hobby('Cats')

    def add_hobby(self, hobby):
        super().add_hobby(hobby)

class Employee(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company

print(Person("Gosho"))