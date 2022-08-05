from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    TYPE = 'Power'

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, self.TYPE, capacity, memory)

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__capacity = int(value * 0.25)

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = int(value * 1.75)
