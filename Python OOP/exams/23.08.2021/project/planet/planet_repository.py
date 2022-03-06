from project.planet.planet import Planet


class PlanetRepository:
    def __init__(self):
        self.planets = []  # planets to be explored and will be added here

    def add(self, planet: Planet):
        self.planets.append(planet)

    def remove(self, planet: Planet):
        if planet in self.planets:
            self.planets.remove(planet)

    def find_by_name(self, name):
        for planet in self.planets:
            if planet.name == name:
                return planet
