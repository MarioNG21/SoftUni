class Person:
    def __init__(self, name, age):
        self.set_age(age)
        self.set_name(name)

    def set_age(self, new_age):
        self.__age = new_age

    def get_age(self):
        return self.__age

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name


person = Person("George", 32)
print(person.get_name())
print(person.get_age())
