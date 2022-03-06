from abc import ABC, abstractmethod
from typing import List

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink


class Table(ABC):
    __INVALID_CAPACITY_MESSAGE = "Capacity has to be greater than 0!"

    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders: List[BakedFood] = []
        self.drink_orders: List[Drink] = []
        self.number_of_people = 0
        self.is_reserved = False

    @classmethod
    def __validate_capacity(cls, value):
        if value <= 0:
            raise ValueError(cls.__INVALID_CAPACITY_MESSAGE)

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__validate_capacity(value)
        self.__capacity = value

    def reserve(self, number_of_people):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        return sum([d.price for d in self.drink_orders]) + sum([f.price for f in self.food_orders])

    def clear(self):
        self.food_orders: List[BakedFood] = []
        self.drink_orders: List[Drink] = []
        self.number_of_people = 0
        self.is_reserved = False

    @abstractmethod
    def get_type(self):
        pass

    def free_table_info(self):
        if not self.is_reserved:
            return f'''Table: {self.table_number}
Type: {self.get_type()}
Capacity: {self.capacity}
'''.rstrip()