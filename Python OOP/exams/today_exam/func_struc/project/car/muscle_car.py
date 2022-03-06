from project.car.car import Car


class MuscleCar(Car):
    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

    def get_min_speed_limit(self):
        return 250

    def get_max_speed_limit(self):
        return 450

    def get_type_of_car(self):
        return 'MuscleCar'

