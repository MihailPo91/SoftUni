from abc import ABC, abstractmethod

from project.tools.validators.validator import Validator


class Car(ABC):

    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken = False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        message = f"Model {value} is less than 4 symbols!"
        Validator.check_if_length_is_less_than_4(value, message)
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        message = f"Invalid speed limit! Must be between {self.min_speed_limit} and {self.max_speed_limit}!"
        Validator.check_if_value_in_range(value,
                                          self.min_speed_limit,
                                          self.max_speed_limit,
                                          message)
        self.__speed_limit = value

    @property
    @abstractmethod
    def min_speed_limit(self):
        pass

    @property
    @abstractmethod
    def max_speed_limit(self):
        pass
