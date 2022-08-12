from project.tools.validators.validator import Validator


class Driver:
    def __init__(self, name: str):
        self.name = name
        self.car = None  # Car object
        self.number_of_wins = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        message = "Name should contain at least one character!"
        Validator.check_if_value_is_empty_string_or_whitespace(value, message)
        self.__name = value

