from project.aquarium.base_aquarium import BaseAquarium
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class SaltwaterAquarium(BaseAquarium):
    CAPACITY = 25

    def __init__(self, name: str,):
        super().__init__(name, self.CAPACITY)

    def add_fish(self, fish: object):

        if not self.__capacity_is_enough(self.capacity, self.fish):
            return "Not enough capacity."

        if isinstance(fish, SaltwaterFish):  # isinstance(fish, SaltwaterFish):
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."
        return "Water not suitable."

    @staticmethod
    def __capacity_is_enough(capacity, collection):
        if len(collection) < capacity:
            return True
        return False
