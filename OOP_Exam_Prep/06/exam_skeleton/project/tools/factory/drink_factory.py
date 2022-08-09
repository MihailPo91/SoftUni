from project.drink.tea import Tea
from project.drink.water import Water
from project.tools.validator.validator import Validator


class DrinkFactory:
    valid_drink_types = {
        'Tea': Tea,
        'Water': Water
    }

    @staticmethod
    def create_drink(drink_type: str, name: str, portion: float, brand:str):
        if Validator.check_if_type_is_valid(drink_type, DrinkFactory.valid_drink_types):
            drink = DrinkFactory.valid_drink_types[drink_type](name, portion, brand)
            return drink
        return None
