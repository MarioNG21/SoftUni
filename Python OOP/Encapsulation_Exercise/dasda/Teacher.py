from dasda.employee import Employee
from dasda.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'



pesho = Teacher()
print(pesho.get_fired())
print(pesho.sleep())
print(pesho.teach())
