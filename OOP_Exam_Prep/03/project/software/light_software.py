from project.software.software import Software


class LightSoftware(Software):
    TYPE = 'Light'

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self.TYPE, capacity_consumption, memory_consumption)

    @property
    def capacity_consumption(self):
        return self.__capacity_consumption

    @capacity_consumption.setter
    def capacity_consumption(self, value):
        self.__capacity_consumption = int(value * 1.5)

    @property
    def memory_consumption(self):
        return self.__memory_consumption

    @memory_consumption.setter
    def memory_consumption(self, value):
        self.__memory_consumption = int(value * 0.5)
