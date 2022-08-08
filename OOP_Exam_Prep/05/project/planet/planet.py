from project.helpers.validator.validators import Validator


class Planet:
    def __init__(self, name):
        self.name = name
        self.items = []  # holds strings, not objects!

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.planet_name_is_not_empty_string(value)
        self.__name = value


