from typing import List

from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms: List[Room] = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total_consumption = 0
        for room in self.rooms:
            total_consumption += (room.calculate_total_consumption())
        return f"Monthly consumption: {total_consumption:.2f}$."

    def pay(self):
        result = []
        for room in self.rooms:
            if room.budget >= room.calculate_total_consumption():
                room.budget -= room.calculate_total_consumption()
                result.append(
                    f"{room.family_name} paid {room.calculate_total_consumption():.2f}$ and have {room.budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                result.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

        return '\n'.join(result)

    def status(self):
        result = f"Total population: {self.calculate_total_people_in_hotel()}\n"
        for room in self.rooms:
            result += f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$" \
                      f", Expenses: {room.expenses:.2f}$\n"
            if self.__check_if_there_are_kids_in_the_room(room):
                for idx, child in enumerate(room.children):
                    result += f"--- Child {idx + 1} monthly cost: {child.get_monthly_expense():.2f}$\n"
            result += f"--- Appliances monthly cost: {room.return_appliance():.2f}$\n"
        return result.rstrip()

    def calculate_total_people_in_hotel(self):
        total = 0
        for room in self.rooms:
            total += room.members_count

        return total

    @staticmethod
    def __check_if_there_are_kids_in_the_room(room: Room):
        if room.children:
            return True
        return False
