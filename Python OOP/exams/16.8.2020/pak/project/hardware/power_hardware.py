from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware


class PowerHardware(Hardware):
    def __init__(self, name, capacity, memory):
        super().__init__(name, "Power", int(capacity * 0.25), int(memory + memory * 0.75))

    def get_type(self):
        return "Power"

