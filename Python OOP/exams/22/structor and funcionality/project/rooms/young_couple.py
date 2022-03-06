from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    def __init__(self, family_name, salary_one, salary_two):
        super().__init__(family_name, salary_one + salary_two, 2)
        self.room_cost = 20
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop()]
        self.expenses = self.calculate_expenses(self.appliances)

    def calculate_total_consumption(self):
        return self.expenses + self.room_cost

    def return_appliance(self):
        return sum([app.get_monthly_expense() for app in self.appliances])