from abc import ABC, abstractmethod


class BaseFish(ABC):
    __INVALID_NAME_MESSAGE = "Fish name cannot be an empty string."
    __INVALID_SPECIES_MESSAGE = "Fish species cannot be an empty string."
    __INVALID_PRICE_MESSAGE = "Price cannot be equal to or below zero."

    @classmethod
    def __validate_name(cls, name):
        if name.strip() == '':
            raise ValueError(cls.__INVALID_NAME_MESSAGE)

    @classmethod
    def __validate_species(cls, species):
        if species.strip() == '':
            raise ValueError(cls.__INVALID_SPECIES_MESSAGE)

    @classmethod
    def __validate_price(cls, price):
        if price <= 0:
            raise ValueError(cls.__INVALID_PRICE_MESSAGE)

    def __init__(self, name, species, size, price):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__validate_name(value)
        self.__name = value

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        self.__validate_species(value)
        self.__species = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__validate_price(value)
        self.__price = value

    @abstractmethod
    def eat(self):
        self.size += 5

    @abstractmethod
    def get_living_place(self):
        pass
