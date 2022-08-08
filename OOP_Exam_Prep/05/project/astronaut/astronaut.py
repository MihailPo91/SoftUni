from abc import ABC, abstractmethod
from project.helpers.validator.validators import Validator


class Astronaut(ABC):

    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.astronaut_name_is_not_empty_string(value)
        self.__name = value

    @abstractmethod
    def breathe(self):
        self.oxygen -= 10

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
