from abc import ABC, abstractmethod
from typing import List

from project.decoration.base_decoration import BaseDecoration
from project.fish.base_fish import BaseFish


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.decorations: List[BaseDecoration] = []
        self.fish: List[BaseFish] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    def add_fish(self, fish: BaseFish):
        if self.capacity == len(self.fish):
            return "Not enough capacity."
        elif fish.get_living_place() == self.__class__.__name__:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."
        else:
            return "Water not suitable."

    def remove_fish(self, fish):
        self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        [f.eat() for f in self.fish]

    def __str__(self):
        fish_names = [f.name for f in self.fish]
        return f'''{self.name}:
Fish: {' '.join(fish_names) if fish_names else "none"}
Decorations: {len(self.decorations)}
Comfort: {self.calculate_comfort()}
'''.strip()
