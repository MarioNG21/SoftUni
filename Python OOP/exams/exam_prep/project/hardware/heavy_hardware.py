from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    TYPE = "Heavy"

    def __init__(self, name, capacity, memory):
        super().__init__(name, self.TYPE, (2 * capacity), int(memory * 0.75))
