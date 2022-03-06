class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def get_age(self):
        return self._age

    @property
    def get_name(self):
        return self._name

    def is_adult(self):
        return self._age >= 18


    @get_age.setter
    def get_age(self, new_age):

        if not new_age:
            raise ValueError("Age cannot be None")

        self._age = new_age


    @get_name.setter
    def get_name(self, new_name):
        if not new_name:
            raise ValueError

        if any([not x.isalpha() for x in new_name]):
            raise ValueError("Cannot contain digit")

        self._name = new_name


class Kid(Person):
    def __init__(self, name, age):
        super().__init__(name, age)


x = Person("pesho", 12)
x.get_age = 18
print(x.get_age)
x.get_name = "Tigara12"
print(x.name)