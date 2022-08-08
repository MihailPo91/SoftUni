class Validator:

    @staticmethod
    def astronaut_name_is_not_empty_string(name):
        if name.strip() == '':
            raise ValueError("Astronaut name cannot be empty string or whitespace!")

    @staticmethod
    def planet_name_is_not_empty_string(name):
        if name.strip() == '':
            raise ValueError("Planet name cannot be empty string or whitespace!")

    @staticmethod
    def is_valid_astronaut_type(valid_astronaut_types, astronaut_type):
        if astronaut_type not in valid_astronaut_types:
            raise Exception("Astronaut type is not valid!")

    @staticmethod
    def check_if_astronaut_name_is_in_repository(repository, name):
        if not repository.find_by_name(name):
            raise Exception(f"Astronaut {name} doesn't exist!")

    @staticmethod
    def check_if_planet_exists(repository, name):
        if not repository.find_by_name(name):
            raise Exception("Invalid planet name!")

    @staticmethod
    def check_if_there_are_any_suitable_astronauts(collection):
        if not collection:
            raise Exception("You need at least one astronaut to explore the planet!")
