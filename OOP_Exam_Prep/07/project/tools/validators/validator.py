class Validator:

    @staticmethod
    def check_if_length_is_less_than_4(string, message):
        if len(string) < 4:
            raise ValueError(message)

    @staticmethod
    def check_if_value_in_range(value, min_value, max_value, message):
        if value < min_value or value > max_value:
            raise ValueError(message)

    @staticmethod
    def check_if_value_is_empty_string_or_whitespace(string, message):
        if string.strip() == '':
            raise ValueError(message)

    @staticmethod
    def check_if_driver_already_exists(name, collection, message):
        if name in collection:
            raise Exception(message)

    @staticmethod
    def check_if_model_already_exists(item, collection, message):
        if item in collection:
            raise Exception(message)

    @staticmethod
    def check_if_valid_car_type(car_type, valid_types):
        if car_type in valid_types:
            return True
        return False

    @staticmethod
    def check_if_race_already_exists(name, collection, message):
        for item in collection:
            if item.name == name:
                raise Exception(message)

    @staticmethod
    def check_if_value_in_list(name, list, message):
        if name not in list:
            raise Exception(message)

    @staticmethod
    def check_if_driver_has_car(driver, message):
        if not driver.car:
            raise Exception(message)

    @staticmethod
    def check_if_driver_was_in_race(driver, race):
        for participant in race.drivers:
            if driver == participant:
                return True
        return False

    @staticmethod
    def check_if_less_than_3_participants_in_race(collection, message):
        if len(collection) < 3:
            raise Exception(message)





