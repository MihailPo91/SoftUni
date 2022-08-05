from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    TYPE = 'Heavy'

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, self.TYPE, capacity, memory)

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__capacity = value * 2

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = int(value * 0.75)
