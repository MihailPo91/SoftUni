from project.table.table import Table
from project.tools.validator.validator import Validator


class OutsideTable(Table):
    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        min_number = 51
        max_number = 100
        Validator.check_if_value_in_range(
            value,
            min_number,
            max_number,
            "Outside table's number must be between 51 and 100 inclusive!")
        self.__table_number = value
