class Person:
    def __init__(self, name):
        self.name = name

    def __iter__(self):
        return PersonIterator(self)


class PersonIterator:
    def __init__(self, person: Person):
        self.person = person
        self.index = 0

    def __next__(self):
        if self.index == len(self.person.name):
            raise StopIteration
        value = self.person.name[self.index]
        self.index += 1
        return value


gosho = Person('Gosho')
for x in gosho:
    print(x)
