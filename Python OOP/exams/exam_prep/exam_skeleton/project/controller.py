
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    AQUARIUM_MAPPER = {
        'FreshwaterAquarium': FreshwaterAquarium,
        'SaltwaterAquarium': SaltwaterAquarium,
    }

    DECORATION_MAPPER = {
        'Ornament': Ornament,
        'Plant': Plant
    }

    FISH_MAPPER = {
        'SaltwaterFish': SaltwaterFish,
        'FreshwaterFish': FreshwaterFish,
    }

    def __init__(self):
        self.aquariums = []
        self.decorations_repository = DecorationRepository()

    def add_aquarium(self, aquarium_type, aquarium_name):
        if aquarium_type in self.AQUARIUM_MAPPER:
            aquarium = self.AQUARIUM_MAPPER[aquarium_type](aquarium_name)
            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."

        return "Invalid aquarium type."

    def add_decoration(self, decoration_type):
        if decoration_type in self.DECORATION_MAPPER:
            decoration = self.DECORATION_MAPPER[decoration_type]()
            self.decorations_repository.add(decoration)
            return f"Successfully added {decoration_type}."

        return "Invalid decoration type."

    def insert_decoration(self, aquarium_name, decoration_type):
        try:
            aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
            decoration = \
                [d for d in self.decorations_repository.decorations if d.__class__.__name__ == decoration_type][0]

            aquarium.add_decoration(decoration)
            if self.decorations_repository.remove(decoration):
                return f"Successfully added {decoration_type} to {aquarium_name}."

        except IndexError:
            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name, fish_type, fish_name, fish_species, price):
        if fish_type not in self.FISH_MAPPER:
            return f"There isn't a fish of type {fish_type}."
        try:
            aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
            fish = self.FISH_MAPPER[fish_type](fish_name, fish_species, price)
            return aquarium.add_fish(fish)

        except IndexError:
            return "There isn't a aquarium with this name"

    def feed_fish(self, aquarium_name):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        fed_fish = aquarium.feed()
        return f"Fish fed: {fed_fish}"

    def calculate_value(self, aquarium_name):
        aquarium = [a for a in self.aquariums if a.name == aquarium_name][0]
        value_of_aquarium_fish = sum([fish.price for fish in aquarium.fish])
        value_of_aquarium_decoration = sum([decoration.price for decoration in aquarium.decorations])
        total_value = value_of_aquarium_fish + value_of_aquarium_decoration
        return f"The value of Aquarium {aquarium_name} is {total_value:.2f}."

    def report(self):
        result = ''
        for aquarium in self.aquariums:
            result += str(aquarium) + '\n'

        return result.rstrip()
