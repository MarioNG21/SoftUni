class Person:
    _min_length = 2
    _max_name_length = 15

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):

        return self.__name

    @name.setter
    def name(self, value):
        self._validate_name(value)
        self.__name = value

    @classmethod
    def _validate_name(cls, value):
        value_len = len(value)
        if value_len < cls._min_length or cls._max_name_length < value_len:
            raise ValueError(f"The length of the name must be between {cls._min_length} and {cls._max_name_length}")

class Student(Person):
    attr1 = "Student"
    _min_length = 10
    # _max_name_length = 19


st = Student("PESHO KUCIQ", 25)