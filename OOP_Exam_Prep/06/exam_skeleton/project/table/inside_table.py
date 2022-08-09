from project.table.table import Table
from project.tools.validator.validator import Validator


class InsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        min_number = 1
        max_number = 50
        Validator.check_if_value_in_range(
            value,
            min_number,
            max_number,
            "Inside table's number must be between 1 and 50 inclusive!")
        self.__table_number = value
