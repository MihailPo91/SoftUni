from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.helpers.validator.validators import Validator


class AstronautFactory:
    valid_astronaut_types = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist
    }

    @staticmethod
    def create_astronaut(astronaut_type: str, name: str):
        Validator.is_valid_astronaut_type(AstronautFactory.valid_astronaut_types, astronaut_type)
        astronaut = AstronautFactory.valid_astronaut_types[astronaut_type](name)
        return astronaut


