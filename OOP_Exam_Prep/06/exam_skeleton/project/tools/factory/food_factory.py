from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.tools.validator.validator import Validator


class FoodFactory:
    valid_food_types = {
        'Bread': Bread,
        'Cake': Cake
    }

    @staticmethod
    def create_food(food_type, name, price):
        if Validator.check_if_type_is_valid(food_type, FoodFactory.valid_food_types):
            food = FoodFactory.valid_food_types[food_type](name, price)

            return food
        return None
