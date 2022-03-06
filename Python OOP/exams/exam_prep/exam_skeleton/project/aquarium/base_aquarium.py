from abc import ABC
from typing import List

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Aquarium name cannot be an empty string.")

        self.__name = value

    def calculate_comfort(self):
        sum_of_comfort = sum([d.comfort for d in self.decorations])
        return sum_of_comfort

    def add_fish(self, fish):
        if len(self.fish) < self.capacity:  # Warning: this aquarium check
            if fish.AQUARIUM == self.__class__.__name__:
                self.fish.append(fish)
                return f"Successfully added {fish.__class__.__name__} to {self.name}."
            else:
                return "Water not suitable."

        return "Not enough capacity."

    def remove_fish(self, fish) -> None:
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        fish_counter = 0
        for fish in self.fish:
            fish.eat()
            fish_counter += 1
        return fish_counter

    def __str__(self) -> str:
        names = ' '.join([fish.name for fish in self.fish])
        result = f"{self.name}:\n"
        result += f"Fish: {names if names else 'none'}\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}"

        return result
