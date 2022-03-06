class Person:
    def __init__(self, first_name, last_name, age = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


me = Person("Peter", "John", 25)
me_2 = Person("John", "Doe")


me.age += 1

print(me.age)