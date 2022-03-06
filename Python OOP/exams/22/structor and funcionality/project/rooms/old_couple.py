from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    def __init__(self, family_name, pension_one, pension_two):
        super().__init__(family_name, pension_one + pension_two, 2)
        self.room_cost = 15
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Stove(), Stove()]
        self.expenses = self.calculate_expenses(self.appliances)

    def calculate_total_consumption(self):
        return self.expenses + self.room_cost

    def return_appliance(self):
        return sum([app.get_monthly_expense() for app in self.appliances])
