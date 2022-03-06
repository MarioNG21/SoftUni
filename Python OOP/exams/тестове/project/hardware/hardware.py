from typing import List

from project.software.software import Software


class Hardware:
    def __init__(self, name, hardware_type, capacity, memory):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components: List[Software] = []

    def install(self, software: Software):
        if self.__enough_capacity >= software.capacity_consumption \
                and self.__enough_memory >= software.memory_consumption:

            self.software_components.append(software)
        else:
            raise Exception("Software cannot be installed")

    def uninstall(self, software: Software):
        self.software_components.remove(software)

    @property
    def __enough_capacity(self):
        return self.capacity - sum([s.capacity_consumption for s in self.software_components])

    @property
    def __enough_memory(self):
        return self.memory - sum([s.memory_consumption for s in self.software_components])
