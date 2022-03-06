from typing import List

import names as names

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

    def __finding_soft_comps(self, type_soft):
        result = []
        for software in self.software_components:
            if software.software_type == type_soft:
                result.append(software)

        return len(result)

    def __repr__(self):
        sum_of_memory_usage = sum([s.memory_consumption for s in self.software_components])
        sum_of_capacity_usage = sum([s.capacity_consumption for s in self.software_components])
        names = [s.name for s in self.software_components]
        result = f'''Hardware Component - {self.name}
Express Software Components: {self.__finding_soft_comps('Express')}
Light Software Components: {self.__finding_soft_comps("Light")}
Memory Usage: {sum_of_memory_usage} / {self.memory}
Capacity Usage: {sum_of_capacity_usage} / {self.capacity}
Type: {self.__class__.__name__}
Software Components: {', '.join(names) if names else None}
'''
        return result.rstrip()