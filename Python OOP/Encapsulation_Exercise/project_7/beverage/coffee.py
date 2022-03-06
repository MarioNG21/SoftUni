from project_7.beverage.hot_beverage import HotBeverage


class Coffee(HotBeverage):
    PRICE = 3.5
    MILLILITERS = 50

    def __init__(self, name, caffeine):
        super().__init__(name, Coffee.PRICE, Coffee.MILLILITERS)
        self.__caffeine = caffeine

    @property
    def caffeine(self):
        return self.__caffeine

    @caffeine.setter
    def caffeine(self, value):
        self.__caffeine = value
