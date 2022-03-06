class Player:
    def __init__(self, name, sprint, dribble, passing, shooting):
        self.name = name
        self.sprint = sprint
        self.dribble = dribble
        self.passing = passing
        self.shooting = shooting

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def sprint(self):
        return self.__sprint

    @sprint.setter
    def sprint(self, value):
        self.__sprint = value

    @property
    def dribble(self):
        return self.__dribble

    @dribble.setter
    def dribble(self, value):
        self.__dribble = value

    @property
    def passing(self):
        return self.__passing

    @passing.setter
    def passing(self, value):
        self.__passing = value

    @property
    def shooting(self):
        return self.__shooting

    @shooting.setter
    def shooting(self, value):
        self.__shooting = value

    def __str__(self):
        return f"Player: {self.__name}" + '\n' + f'Sprint: {self.__sprint}' + '\n' \
               + f"Dribble: {self.__dribble}" + '\n' + f"Passing: {self.__passing}" + '\n' \
               + f"Shooting: {self.__shooting}"
