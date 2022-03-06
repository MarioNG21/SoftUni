from abc import abstractmethod
from typing import List

from project.appliances.appliance import Appliance
from project.appliances.laptop import Laptop
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.people.child import Child


class Room:
    __INVALID_EXPENSES_MESSAGE = "Expenses cannot be negative"

    def __init__(self, name, budget, members_count):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children: List[Child] = []
        self.expenses = 0

    @classmethod
    def __expenses_validator(cls, value):
        if value < 0:
            raise ValueError(cls.__INVALID_EXPENSES_MESSAGE)
        pass

    @property
    def expenses(self):
        return self.__expenses

    @expenses.setter
    def expenses(self, value):
        if value < 0:
            raise ValueError("Expenses cannot be negative")
        self.__expenses = value

    def calculate_expenses(self, *args):
        result = 0
        for el in args:
            sum_of_one_el = 0
            for obj in el:
                if obj.__class__.__name__ == "Child":
                    sum_of_one_el += obj.cost * 30
                else:
                    sum_of_one_el += obj.get_monthly_expense()
            result += sum_of_one_el

        self.expenses = result
        return self.expenses

    @abstractmethod
    def calculate_total_consumption(self):
        pass

    @abstractmethod
    def return_appliance(self):
        pass
