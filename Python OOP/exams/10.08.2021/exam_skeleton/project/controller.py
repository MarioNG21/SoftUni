from typing import List

from project.aquarium.base_aquarium import BaseAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class AquariumFactory:
    @staticmethod
    def creating_aquariums(aquarium_type, aquarium_name):
        if aquarium_type == "FreshwaterAquarium":
            return FreshwaterAquarium(aquarium_name)
        elif aquarium_type == 'SaltwaterAquarium':
            return SaltwaterAquarium(aquarium_name)
        return


class DecorationFactory:
    @staticmethod
    def creating_decorations(decoration_type):
        if decoration_type == "Plant":
            return Plant()

        elif decoration_type == "Ornament":
            return Ornament()

        return


class FishFactory:
    @staticmethod
    def creating_fish(fish_type, fish_name, species, price):
        if fish_type == 'FreshwaterFish':
            return FreshwaterFish(fish_name, species, price)
        elif fish_type == "SaltwaterFish":
            return SaltwaterFish(fish_name, species, price)

        return


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums: List[BaseAquarium] = []

    def __finding_aquarium(self, aquarium_name):
        for aquarium in self.aquariums:
            if aquarium.name == aquarium_name:
                return aquarium

    def add_aquarium(self, aquarium_type, aquarium_name):
        aquarium = AquariumFactory().creating_aquariums(aquarium_type, aquarium_name)
        if aquarium is None:
            return "Invalid aquarium type."

        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type):
        decoration = DecorationFactory().creating_decorations(decoration_type)
        if decoration is None:
            return "Invalid decoration type."

        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name, decoration_type):
        aquarium = self.__finding_aquarium(aquarium_name)
        decoration = self.decorations_repository.find_by_type(decoration_type)
        if aquarium is not None and decoration != "None":
            aquarium.add_decoration(decoration)
            if self.decorations_repository.remove(decoration):
                return f"Successfully added {decoration_type} to {aquarium_name}."

        else:
            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        fish = FishFactory().creating_fish(fish_type, fish_name, fish_species, price)
        aquarium = self.__finding_aquarium(aquarium_name)
        if fish is None:
            return f"There isn't a fish of type {fish_type}."
        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name):
        aquarium = self.__finding_aquarium(aquarium_name)
        counter = 0
        for fish in aquarium.fish:
            fish.eat()
            counter += 1
        return f"Fish fed: {counter}"

    def calculate_value(self, aquarium_name):
        aquarium = self.__finding_aquarium(aquarium_name)
        sum_of_decorations = sum([dec.price for dec in aquarium.decorations])
        sum_of_fish = sum([fish.price for fish in aquarium.fish])
        total = sum_of_decorations + sum_of_fish
        return f"The value of Aquarium {aquarium_name} is {total:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += str(aquarium) + '\n'

        return result.strip()

