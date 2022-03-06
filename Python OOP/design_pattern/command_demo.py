class Command:
    def execute(self):
        pass


class SumCommand(Command):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def execute(self):
        return self.x + self.y


class AddCommand(Command):
    def __init__(self, ll, value):
        self.ll = ll
        self.value = value

    def execute(self):
        self.ll.append(self.value)


class PrintCommand(Command):
    def __init__(self, ll):
        self.ll = ll

    def execute(self):
        print(self.ll)
        return self.ll


ll = []
commands = [
    SumCommand(ll, 3),
    AddCommand(ll, 7),
    PrintCommand(ll),
    AddCommand(ll, -7),
    PrintCommand(ll),
    AddCommand(ll, 11),
    PrintCommand(ll)
]

for c in commands:
    (c.execute())
