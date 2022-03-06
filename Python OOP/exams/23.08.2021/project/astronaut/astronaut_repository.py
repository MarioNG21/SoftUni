from typing import List

from project.astronaut.astronaut import Astronaut


class AstronautRepository:
    def __init__(self):
        self.astronauts: List[Astronaut] = []  # Astronauts on the space ship

    def add(self, astronaut: Astronaut):
        if astronaut not in self.astronauts:
            self.astronauts.append(astronaut)
            return f"Successfully added {astronaut.__class__.__name__}: {astronaut.name}."

        return f"{astronaut.name} is already added."

    def remove(self, astronaut: Astronaut):
        if astronaut in self.astronauts:
            self.astronauts.remove(astronaut)
            return astronaut

    def find_by_name(self, name):
        for astronaut in self.astronauts:
            if astronaut.name == name:
                return astronaut
