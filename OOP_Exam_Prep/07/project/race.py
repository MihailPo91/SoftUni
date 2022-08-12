from project.tools.validators.validator import Validator


class Race:
    def __init__(self, name: str):
        self.name = name
        self.drivers = []  # Driver objects

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        message = "Name cannot be an empty string!"
        Validator.check_if_value_is_empty_string_or_whitespace(value, message)
        self.__name = value
