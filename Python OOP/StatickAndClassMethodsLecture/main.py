class Person:
    def __init__(self, age, name):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @staticmethod
    def validate_name(value):
        if len(value) < 4:
            raise ValueError("Name was to short")


class Student(Person):
    def __init__(self, age, name):
        super().__init__(age, name)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @staticmethod
    def validate_name(value):
        Person.validate_name(value)
        if len(value) < 5:
            raise ValueError("Name must be at least 5-characters long")


st = Student(12, 'aa')
st.validate_name('aaaa')
