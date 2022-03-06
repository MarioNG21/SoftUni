from project.car.car import Car


class SportsCar(Car):
    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

    def get_min_speed_limit(self):
        return 400

    def get_max_speed_limit(self):
        return 600

    def get_type_of_car(self):
        return 'SportsCar'
