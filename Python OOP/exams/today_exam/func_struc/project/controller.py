from typing import List

from project.car.car import Car
from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class CarFactory:
    @staticmethod
    def creating_car(car_type, model, speed_limit):
        if car_type == "MuscleCar":
            return MuscleCar(model, speed_limit)
        elif car_type == "SportsCar":
            return SportsCar(model, speed_limit)

        return None


class Controller:
    def __init__(self):
        self.cars: List[Car] = []
        self.drivers: List[Driver] = []
        self.races: List[Race] = []

    def __finding_car_by_type(self, car_type):
        for car in self.cars:
            if car.get_type_of_car() == car_type and car.is_taken:
                return True

        return False

    def __check_if_all_cars_are_taken(self):
        result = []
        for car in self.cars:
            result.append(car.is_taken)

        return all(result)

    def __finding_car_by_model(self, car_model):
        for car in self.cars:
            if car.model == car_model:
                return True
        return False

    def __finding_driver(self, driver_name):
        for driver in self.drivers:
            if driver.name == driver_name:
                return True

        return False

    def __finding_race(self, race_name):
        for race in self.races:
            if race.name == race_name:
                return True

        return False

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car = CarFactory().creating_car(car_type, model, speed_limit)
        if car is None:
            return
        if not self.__finding_car_by_model(car.model):
            self.cars.append(car)
            return f"{car_type} {model} is created."
        else:
            raise Exception(f"Car {model} is already created!")

    def create_driver(self, driver_name: str):
        driver = Driver(driver_name)
        if not self.__finding_driver(driver_name):
            self.drivers.append(driver)
            return f"Driver {driver.name} is created."
        else:
            raise Exception(f"Driver {driver_name} is already created!")

    def create_race(self, race_name: str):
        race = Race(race_name)
        if not self.__finding_race(race_name):
            self.races.append(race)
            return f"Race {race_name} is created."
        else:
            raise Exception(f"Race {race_name} is already created!")

    def add_car_to_driver(self, driver_name: str, car_type: str):
        if not self.__finding_driver(driver_name):
            raise Exception(f"Driver {driver_name} could not be found!")

        driver = [d for d in self.drivers if d.name == driver_name][-1]
        if not self.__finding_car_by_type(car_type) or self.__check_if_all_cars_are_taken():
            raise Exception(f"Car {'MuscleCar'} could not be found!")

        new_car = [c for c in self.cars if c.get_type_of_car() == car_type][-1]
        if driver.car is not None:
            if not new_car.is_taken:
                old_car_model = driver.car.model
                driver.car.is_taken = False
                self.cars.append(driver.car)

                driver.car = new_car
                new_car.is_taken = True
                self.cars.remove(new_car)
                return f"Driver {driver.name} changed his car from {old_car_model} to {new_car.model}."
        else:
            if not new_car.is_taken:
                driver.car = new_car
                new_car.is_taken = True
                self.cars.remove(new_car)
                return f"Driver {driver_name} chose the car {new_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        if not self.__finding_race(race_name):
            raise Exception(f"Race {race_name} could not be found!")
        race = [r for r in self.races if r.name == race_name][-1]

        if not self.__finding_driver(driver_name):
            raise Exception(f"Driver {driver_name} could not be found!")

        driver = [d for d in self.drivers if d.name == driver_name][-1]
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        if not self.__finding_race(race_name):
            raise Exception(f"Race {race_name} could not be found!")
        race = [r for r in self.races if r.name == race_name][-1]
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        else:
            counter = 0
            result = []
            for driver in sorted(race.drivers, key=lambda x: -x.car.speed_limit):
                driver.number_of_wins += 1
                result.append(
                    f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")
                counter += 1
                if counter == 3:
                    break

            return '\n'.join(result)

