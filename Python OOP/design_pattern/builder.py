from main import House


class HouseBuilder:
    rooms_count = 0
    floors_count = 1
    has_garage = False
    has_electricity = False
    balcon_count = 19
    town = "Haskovo"
    has_pool = False

    def with_rooms_count(self, rooms_count):
        self.rooms_count = rooms_count

    def with_floors_count(self, floors_count):
        self.floors_count = floors_count

    def with_garage(self):
        self.has_garage = True

    def with_electricity(self):
        self.has_electricity = True

    def with_balcon_count(self, balcon_count):
        self.balcon_count = balcon_count

    def with_town(self, town):
        self.town = town

    def with_pool(self):
        self.has_pool = True

    def build(self):
        return House(self.floors_count,
                     self.has_garage,
                     self.has_electricity,
                     self.rooms_count,
                     self.balcon_count,
                     self.has_pool,
                     self.town)


class HouseFactory:
    def get_house_in_burgas(self, floors_count, rooms_count, balcon_count):
        builder = HouseBuilder()
        builder.with_town('Burgas')
        builder.with_floors_count(floors_count)
        builder.with_rooms_count(rooms_count)
        builder.with_balcon_count(balcon_count)
        return builder.build()


builder1 = HouseBuilder()
builder1.with_town("Sofia")
builder1.with_floors_count(3)
builder1.with_electricity()
house = builder1.build()
print(house)
