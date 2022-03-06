from typing import List

from project.appliances.appliance import Appliance
from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    def __init__(self, family_name, salary):
        super().__init__(family_name, salary, 1)
        self.room_cost = 10
        self.appliances: List[Appliance] = [TV()]
        self.expenses = self.calculate_expenses(self.appliances)

    def calculate_total_consumption(self):
        return self.expenses + self.room_cost

    def return_appliance(self):
        return sum([app.get_monthly_expense() for app in self.appliances])