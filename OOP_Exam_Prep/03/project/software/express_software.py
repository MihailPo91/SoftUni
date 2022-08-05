from project.software.software import Software


class ExpressSoftware(Software):
    TYPE = 'Express'

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self.TYPE, capacity_consumption, memory_consumption)

    @property
    def memory_consumption(self):
        return self.__memory_consumption

    @memory_consumption.setter
    def memory_consumption(self, value):
        self.__memory_consumption = value * 2