from new_project.project.employee import Employee
from new_project.project.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return 'teaching...'