from abc import ABC, abstractmethod


class Drink(ABC):
    __INVALID_NAME_MESSAGE = "Name cannot be empty string or white space!"
    __INVALID_PORTION_MESSAGE = "Portion cannot be less than or equal to zero!"
    __INVALID_BRAND_MESSAGE = "Brand cannot be empty string or white space!"

    @abstractmethod
    def __init__(self, name, portion, price, brand):
        self.name = name
        self.portion = portion
        self.price = price
        self.brand = brand

    @classmethod
    def __validate_name(cls, name):
        if name.strip() == '' or name is None:
            raise ValueError(cls.__INVALID_NAME_MESSAGE)

    @classmethod
    def __validate_portion(cls, portion):
        if portion <= 0:
            raise ValueError(cls.__INVALID_PORTION_MESSAGE)

    @classmethod
    def __validate_brand(cls, brand):
        if brand.strip() == '' or brand is None:
            raise ValueError(cls.__INVALID_BRAND_MESSAGE)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        self.__validate_portion(value)
        self.__portion = value

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        self.__validate_brand(value)
        self.__brand = value

    def __repr__(self):
        return f" - {self.name} {self.brand} - {self.portion:.2f}ml - {self.price:.2f}lv"


