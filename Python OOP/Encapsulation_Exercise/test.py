class Person:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_value):
        if not isinstance(new_value, str):
            raise TypeError("Expected string")
        self._name = new_value


class SubPerson(Person):
    @property
    def name(self):
        print("Getting name")
        return super().name

    @name.setter
    def name(self, value):
        print('Setting name to ', value)
        super(SubPerson).name.__set__(self, value)




s = SubPerson("Guido")
print(s.name)
s.name = "Mario"