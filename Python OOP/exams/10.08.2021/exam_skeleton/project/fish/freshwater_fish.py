from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    __LIVING_PLACE = "FreshwaterAquarium"

    def __init__(self, name, species, price):
        super().__init__(name, species, 3, price)

    # TO DO see how to make inital size
    def eat(self):
        self.size += 3

    def get_living_place(self):
        return "FreshwaterAquarium"
