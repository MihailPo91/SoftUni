from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable
from project.tools.validator.validator import Validator


class TableFactory:
    valid_table_types = {
        'InsideTable': InsideTable,
        'OutsideTable': OutsideTable
    }

    @staticmethod
    def create_table(table_type: str, table_number: int, capacity: int):
        if Validator.check_if_type_is_valid(table_type, TableFactory.valid_table_types):
            table = TableFactory.valid_table_types[table_type](table_number, capacity)
            return table
        return None
