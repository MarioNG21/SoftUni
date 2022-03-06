from typing import List

from project.people.child import Child
from project.rooms.room import Room
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV


class LaptopFactory:
    @staticmethod
    def create_laptop(num_of_children):
        result = []
        for num in range(num_of_children):
            result.append(Laptop())
            result.append(TV())
            result.append(Fridge())
        return result


class YoungCoupleWithChildren(Room):
    def __init__(self, family_name, salary_one, salary_two, *children):
        super().__init__(family_name, salary_one + salary_two, 2 + len(children))
        self.room_cost = 30
        self.children: List[Child] = [child for child in children]
        self.child_appliances = LaptopFactory().create_laptop(len(self.children))
        self.appliances = [TV(), TV(), Fridge(), Fridge(), Laptop(), Laptop(), *self.child_appliances]
        self.expenses = self.calculate_expenses(self.appliances, self.children)

    def calculate_total_consumption(self):
        return self.expenses + self.room_cost

    def return_appliance(self):
        return sum([app.get_monthly_expense() for app in self.appliances])
