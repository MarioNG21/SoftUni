class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.mail = self.first + ' ' + last + '@abv.bg'

    def fullname(self):
        return f"{self.first} {self.last}"


emp_1 = Employee("Mario", "Georgiev")
emp_1.first = 'Nikolai'
print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname())
print(emp_1.mail)