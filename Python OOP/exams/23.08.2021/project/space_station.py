from typing import List
from project.astronaut.astronaut import Astronaut
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository
from project.astronaut.astronaut_repository import AstronautRepository


class SpaceStation:
    ASTRONAUT_MAPPER = {
        'Biologist': Biologist,
        'Geodesist': Geodesist,
        'Meteorologist': Meteorologist,
    }

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions_count = 0
        self.unsuccessful_missions_count = 0

    @staticmethod
    def collecting_items_from_planet(planet: Planet, list_of_astronauts: List[Astronaut]):
        successful_missions_counter = 0
        unsuccessful_missions_counter = 0
        result = ''
        participated_astronaut = 0
        for astronaut in list_of_astronauts:
            while astronaut.oxygen > 0:
                if len(planet.items) > 0:
                    item = planet.items.pop()
                    astronaut.backpack.append(item)
                    astronaut.breathe()
                else:
                    break
        for astronaut in list_of_astronauts:
            if astronaut.backpack:
                participated_astronaut += 1

        if len(planet.items) == 0:
            successful_missions_counter += 1
            result += f"Planet: {planet.name} was explored."
            result += f"{participated_astronaut} astronauts participated in collecting items."
        else:
            result += "Mission is not completed."
            unsuccessful_missions_counter += 1
        return result, successful_missions_counter, unsuccessful_missions_counter

    @staticmethod
    def finding_the_top_5_astronauts(list_of_astronauts):
        winners = []
        for astronaut in sorted(list_of_astronauts, key=lambda x: -x.oxygen):
            if len(winners) < 5 and astronaut.oxygen > 30:
                winners.append(astronaut)
            else:
                break
        return winners

    def add_astronaut(self, astronaut_type, name):
        try:
            astronaut = self.ASTRONAUT_MAPPER[astronaut_type](name)
            return self.astronaut_repository.add(astronaut)

        except KeyError:
            raise Exception("Astronaut type is not valid!")

    def add_planet(self, name, items):
        if self.planet_repository.find_by_name(name) is None:
            planet = Planet(name)
            item_list = items.split(', ')
            self.planet_repository.add(planet)
            for i in item_list:
                planet.items.append(i)

            return f"Successfully added Planet: {name}."
        else:
            return f"{name} is already added."

    def retire_astronaut(self, name):
        try:
            astronaut = [a for a in self.astronaut_repository.astronauts if a.name == name][0]
            if self.astronaut_repository.remove(astronaut) is not None:
                return f"Astronaut {name} was retired!"
        except IndexError:
            raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name):
        try:
            planet = [p for p in self.planet_repository.planets if p.name == planet_name][0]
            suitable_astronauts = self.finding_the_top_5_astronauts(self.astronaut_repository.astronauts)
            if len(suitable_astronauts) == 0:
                raise Exception("You need at least one astronaut to explore the planet!")
            result, counter, unsuccessful_missions_counter = self.collecting_items_from_planet(planet,
                                                                                               suitable_astronauts)
            self.successful_missions_count += counter
            self.unsuccessful_missions_count += unsuccessful_missions_counter

            return result

        except IndexError:
            raise Exception("Invalid planet name!")

    def report(self):
        result = f"{self.successful_missions_count} successful missions!\n"
        result += f"{self.unsuccessful_missions_count} missions were not completed!\n"
        result += "Astronauts' info:\n"
        for astronaut in self.astronaut_repository.astronauts:
            items = ', '.join([i for i in astronaut.backpack])
            result += f"Name: {astronaut.name}\n"
            result += f"Oxygen: {astronaut.oxygen}\n"
            result += f"Backpack items: {items if items else 'none'}\n"

        return result.rstrip()

