class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, guests_count):
        possible_rooms = [r for r in self.rooms if r.number == room_number]
        room = possible_rooms[0]

        if room.taken_room(guests_count):
            return

        self.guests += guests_count

    def free_room(self, room_number):
        possible_rooms = [r for r in self.rooms if r.number == room_number]
        room = possible_rooms[0]
        self.guests -= room.guests


    def status(self):
        free_rooms = [str(r.number) for r in self.rooms if not r.is_taken]
        taken_rooms = [str(r.number) for r in self.rooms if r.is_taken]
        result = f"Hotel {self.name} has {self.guests} total guests" + '\n'
        result += f"Free rooms: {', '.join(free_rooms)}" + '\n'
        result += f"Taken rooms: {', '.join(taken_rooms)}"
        return result
