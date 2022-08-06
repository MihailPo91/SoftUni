import abc

from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class BaseAquarium(abc.ABC):

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    @abc.abstractmethod
    def add_fish(self, fish: object):
        pass

    def remove_fish(self, fish: object):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration: object):
        self.decorations.append(decoration)

    def feed(self):
        [f.eat() for f in self.fish]

    def __str__(self):
        fish = [' '.join([f.name for f in self.fish])] if self.fish else None
        return f""""{self.name}:
Fish: {fish}
Decorations: {len(self.decorations)}
Comfort: {self.calculate_comfort()}"
"""

    @staticmethod
    def __capacity_is_enough(capacity, collection):
        if len(collection) < capacity:
            return True
        return False
