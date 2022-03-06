from project.rooms.room import Room


class AloneOld(Room):
    def __init__(self, family_name, pension):
        super().__init__(family_name, pension, 1)
        self.room_cost = 10

    def calculate_total_consumption(self):
        return self.room_cost

    def return_appliance(self):
        return 0
