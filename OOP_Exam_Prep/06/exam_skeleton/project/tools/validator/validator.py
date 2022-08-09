class Validator:
    @staticmethod
    def check_if_name_is_valid(name, message):
        if name.strip() == '':
            raise ValueError(message)

    @staticmethod
    def check_if_value_is_0_or_below(value, message):
        if value <= 0:
            raise ValueError(message)

    @staticmethod
    def check_if_value_in_range(value, min_number, max_number, message):
        if value < min_number or value > max_number:
            raise ValueError(message)

    @staticmethod
    def check_if_type_is_valid(item_type, valid_types):
        if item_type in valid_types:
            return True
        return False

    @staticmethod
    def check_if_name_in_list(name, collection, message):
        if name in collection:
            raise Exception(message)
