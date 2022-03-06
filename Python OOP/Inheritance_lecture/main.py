class Person:
    def __init__(self, name):
        if not name:
            raise ValueError("Person name ccanot be None or empty space")
        self.name = name
        self.hobbies = set()

    def add_hobby(self, hobby):
        self.hobbies.add(hobby)

    def __str__(self):
        if self.hobbies:
            return f"{self.name} has the following hobbies: {self.hobbies}"
        else:
            return f"{self.name} has no hobbies"

class SoftwareDeveloper(Person):
    def __init__(self, name):
        super().__init__(name)
        self.add_hobby('Lego')
        self.add_hobby('Cats')

    def add_hobby(self, hobby):
        super().add_hobby(hobby)


class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
        self.subjects = []

    def add_subject(self, subject):
        self.subjects.append(subject)
        self.add_hobby(subject)

    def __str__(self):
        super_str = super().__str__()
        # same as Person.__str(self) but not abstract
        if self.subjects:
            subjects = f" and has subject: {self.subjects}"
        else:
            subjects = " and not subjects"
        return super_str + subjects

class Employee(Person):
    def __init__(self, name, company):
        super().__init__(name)
        self.company = company



    # Wrong because we dont use the inheritance
    # def __init__(self, name, company):
    #     self.name = name
    #     self.company = company
    #     self.hobbies = set()
x = Person("Mario")
x.add_hobby('biking')

y = SoftwareDeveloper("Mario")

george = Teacher("Mr.George")
george.add_subject("Math")
george.add_hobby("Tennis")

print(george)
print(Employee("", "SoftUni"))