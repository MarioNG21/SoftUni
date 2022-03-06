from abc import ABC, abstractmethod

from main import House


# Factory method
class HouseFactory:
    def get_no_pool_house(self, floors_count, has_garage, rooms_count, balcon_count, town):
        return House(floors_count, has_garage, True, rooms_count, balcon_count, town, False)


# Simple factory

class HouseFactoryBase(ABC):
    @abstractmethod
    def get_house(self, *args, **kwargs):
        pass


class HouseInSofiaFactory(HouseFactoryBase):
    def get_house(self, floors_count, rooms_count, balcon_count):
        return House(floors_count, False, True, rooms_count, balcon_count, "Sofia", False)


class HouseWithoutPoolFactory(HouseFactoryBase):
    def get_house(self, floors_count, has_garage, rooms_count, balcon_count):
        return House(floors_count, has_garage, True, rooms_count, balcon_count, "Sofia", False)


house1 = House(1, False, False, 3, 0, False, "Sofia")

factory = HouseFactory()
print(factory.get_no_pool_house(3, True, 5, 2, "Sofia"))
print(HouseInSofiaFactory().get_house(3, 7, 19))
