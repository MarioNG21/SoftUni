from typing import List

from project.baked_food.baked_food import BakedFood
from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.drink import Drink
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.table.table import Table


class FoodFactory:
    @staticmethod
    def creating_food(food_type, name, price):
        if food_type == 'Bread':
            return Bread(name, price)
        elif food_type == "Cake":
            return Cake(name, price)
        return None


class DrinkFactory:
    @staticmethod
    def creating_drink(drink_type, name, portion, brand):
        if drink_type == "Tea":
            return Tea(name, portion, brand)
        elif drink_type == "Water":
            return Water(name, portion, brand)

        return


class TableFactory:
    @staticmethod
    def creating_table(table_type, table_number, capacity):
        if table_type == "OutsideTable":
            return OutsideTable(table_number, capacity)
        elif table_type == "InsideTable":
            return InsideTable(table_number, capacity)
        return


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu: List[BakedFood] = []
        self.drinks_menu: List[Drink] = []
        self.tables_repository: List[Table] = []
        self.total_income = 0

    def __getting_names_of_food_in_food_menu(self):
        return (f.name for f in self.food_menu)

    def __getting_names_of_drink_in_drinks_menu(self):
        return (d.name for d in self.drinks_menu)

    def __getting_food_from_name(self, name):
        for food in self.food_menu:
            if food.name == name:
                return food

    def __getting_drink_from_name(self, name):
        for drink in self.drinks_menu:
            if drink.name == name:
                return drink

    def __finding_food(self, food):
        for f in self.food_menu:
            if f.name == food.name:
                return True

        return False

    def __finding_drink(self, drink):
        for d in self.drinks_menu:
            if d.name == drink.name:
                return True

        return False

    def __finding_table(self, table):
        for t in self.tables_repository:
            if t.table_number == table.table_number:
                return True

        return False

    def __getting_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

        return None

    def add_food(self, food_type, name, price):
        food = FoodFactory().creating_food(food_type, name, price)
        if not self.__finding_food(food):
            self.food_menu.append(food)
            return f"Added {food.name} ({food.__class__.__name__}) to the food menu"
        raise Exception(f"{food_type} {name} is already in the menu!")

    def add_drink(self, drink_type, name, portion, brand):
        drink = DrinkFactory().creating_drink(drink_type, name, portion, brand)
        if not self.__finding_drink(drink):
            self.drinks_menu.append(drink)
            return f"Added {drink.name} ({drink.brand}) to the drink menu"

        raise Exception(f"{drink_type} {name} is already in the menu!")

    def add_table(self, table_type, table_number, capacity):
        table = TableFactory().creating_table(table_type, table_number, capacity)
        if not self.__finding_table(table):
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

        raise Exception(f"Table {table_number} is already in the bakery!")

    def reserve_table(self, number_of_people):
        table = [t for t in self.tables_repository if not t.is_reserved]
        if table:
            current_table = table[0]
            if current_table.capacity >= number_of_people:
                current_table.reserve(number_of_people)
                return f"Table {current_table.table_number} has been reserved for {number_of_people} people"

            return f"No available table for {number_of_people} people"

    def order_food(self, table_number, *args):
        table = self.__getting_table(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        food_in_menu_names = [self.__getting_food_from_name(name) for name in args
                              if name in self.__getting_names_of_food_in_food_menu()]

        [table.order_food(food) for food in food_in_menu_names]

        food_not_in_menu_str = [name for name in args if name not in self.__getting_names_of_food_in_food_menu()]

        food_names_in_menu_str = '\n'.join(repr(f) for f in food_in_menu_names)
        food_names_not_in_menu = '\n'.join(food_not_in_menu_str)
        return f'''Table {table_number} ordered:
{food_names_in_menu_str}
{self.name} does not have in the menu:
{food_names_not_in_menu}
'''.rstrip()

    def order_drink(self, table_number, *args):
        table = self.__getting_table(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        drinks_in_menu = [self.__getting_drink_from_name(name) for name in args
                          if name in self.__getting_names_of_drink_in_drinks_menu()]

        [table.order_drink(drink) for drink in drinks_in_menu]

        drinks_not_in_menu_str = [name for name in args if name not in self.__getting_names_of_drink_in_drinks_menu()]

        drinks_name_in_menu = '\n'.join(repr(f) for f in drinks_in_menu)
        drinks_name_not_in_menu = '\n'.join(drinks_not_in_menu_str)
        return f'''Table {table_number} ordered:
{drinks_name_in_menu}
{self.name} does not have in the menu:
{drinks_name_not_in_menu}
        '''.rstrip()

    def leave_table(self, table_number):
        table = self.__getting_table(table_number)
        income = table.get_bill()
        self.total_income += income
        table.clear()
        return f'''Table: {table_number}
Bill: {income:.2f}      
'''.rstrip()

    def get_free_tables_info(self):
        free_tables = [table for table in self.tables_repository if not table.is_reserved]
        return '\n'.join(t.free_table_info() for t in free_tables)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"


