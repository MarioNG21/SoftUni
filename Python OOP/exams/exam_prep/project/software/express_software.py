from project.software.software import Software


class ExpressSoftware(Software):
    TYPE = "Express"

    def __init__(self, name, capacity_consumption, memory_consumption):
        super().__init__(name, self.TYPE, capacity_consumption, 2 * memory_consumption)
