from project.decoration.decoration_repository import DecorationRepository
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.fish.saltwater_fish import SaltwaterFish
from project.fish.freshwater_fish import FreshwaterFish
from project.decoration.plant import Plant
from project.decoration.ornament import Ornament


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        valid_aquarium_types = ["FreshwaterAquarium", "SaltwaterAquarium"]

        if not self.__is_valid_type(aquarium_type, valid_aquarium_types):
            return "Invalid aquarium type."

        aquarium = self.__create_aquarium_object(aquarium_type, aquarium_name)

        self.aquariums.append(aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        valid_decoration_types = ["Ornament", "Plant"]
        if not self.__is_valid_type(decoration_type, valid_decoration_types):
            return "Invalid decoration type."

        decoration = eval(f'{decoration_type}()')

        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        decoration = self.decorations_repository.find_by_type(decoration_type)

        if decoration is None:
            return f"There isn't a decoration of type {decoration_type}."

        aquarium = self.__get_aquarium_by_name(aquarium_name)

        if aquarium is not None:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        valid_fish_types = ["FreshwaterFish", "SaltwaterFish"]

        if not self.__is_valid_type(fish_type, valid_fish_types):
            return f"There isn't a fish of type {fish_type}."

        fish = eval(f'{fish_type}({repr(fish_name)}, {repr(fish_species)}, {float(price)})')
        aquarium = self.__get_aquarium_by_name(aquarium_name)

        if aquarium is not None:
            return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__get_aquarium_by_name(aquarium_name)
        if aquarium is not None:
            aquarium.feed()
            return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__get_aquarium_by_name(aquarium_name)
        value_fish = sum([f.price for f in aquarium.fish])
        value_decoration = sum([d.price for d in aquarium.decorations])
        value = value_fish + value_decoration

        return f"The value of Aquarium {aquarium_name} is {value:.2f}."

    def report(self):
        output = ""

        for aquarium in self.aquariums:
            output += str(aquarium)

        return output.strip()

    @staticmethod
    def __is_valid_type(type, collection):
        if type in collection:
            return True
        return False

    @staticmethod
    def __create_aquarium_object(aquarium_type, aquarium_name):
        return eval(f'{aquarium_type}({repr(aquarium_name)})')

    def __get_aquarium_by_name(self, aquarium_name):
        for aq in self.aquariums:
            if aq.name == aquarium_name:
                return aq
        return None


#
# c = Controller()
# c.add_aquarium('SaltwaterAquarium', 'Kofa')
#
# print(c.add_fish('Kofa', 'SaltwaterFish', 'Pesho', 'barakuda', 10))
# print(c.add_fish('Kofa', 'FreshwaterFish', 'Cuci', 'sharan', 15))
# print(c.add_decoration('Ornament'))
# print(c.insert_decoration('Kofa', 'Ornament'))
# print(c.calculate_value('Kofa'))
