from project.tools.factory.drink_factory import DrinkFactory
from project.tools.factory.food_factory import FoodFactory
from project.tools.factory.table_factory import TableFactory
from project.tools.validator.validator import Validator


class Bakery:
    def __init__(self, name: str):
        self.name = name
        self.food_menu = []  # food objects
        self.drinks_menu = []  # drink objects
        self.tables_repository = []  # table objects
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        Validator.check_if_name_is_valid(value, "Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        Validator.check_if_name_in_list(name, [f.name for f in self.food_menu],
                                        f"{food_type} {name} is already in the menu!")
        food = FoodFactory.create_food(food_type, name, price)

        if food is not None:
            self.food_menu.append(food)
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink (self, drink_type: str, name: str, portion: float, brand: str):
        Validator.check_if_name_in_list(name, [d.name for d in self.drinks_menu],
                                        f"{drink_type} {name} is already in the menu!")
        drink = DrinkFactory.create_drink(drink_type, name, portion, brand)

        if drink is not None:
            self.drinks_menu.append(drink)
            return f"Added {name} ({brand}) to the drink menu"

    def add_table (self, table_type: str, table_number: int, capacity: int):
        Validator.check_if_name_in_list(str(table_number), [str(t.table_number) for t in self.tables_repository],
                                        f"Table {table_number} is already in the bakery!")
        table = TableFactory.create_table(table_type, table_number, capacity)

        if table is not None:
            self.tables_repository.append(table)
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        table = self.__get_first_available_table_with_enough_capacity(number_of_people)
        if table is not None:
            table.reserve(number_of_people)
            return f"Table {table.table_number} has been reserved for {number_of_people} people"
        else:
            return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *food_names):
        table = self.__get_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        in_menu, out_menu = self.__check_if_items_in_menu([f.name for f in self.food_menu], food_names)
        for f in in_menu:
            table.order_food(self.__get_item_by_name(f, self.food_menu))

        output = f"Table {table_number} ordered:\n"
        for f in table.food_orders:
            output += repr(f) + '\n'
        output += f'{self.name} does not have in the menu:\n'
        for f in out_menu:
            output += f + '\n'
        return output.strip()

    def order_drink(self, table_number: int, *drink_names):
        table = self.__get_table_by_number(table_number)
        if table is None:
            return f"Could not find table {table_number}"

        in_menu, out_menu = self.__check_if_items_in_menu([d.name for d in self.drinks_menu], drink_names)
        for d in in_menu:
            table.order_drink(self.__get_item_by_name(d, self.drinks_menu))

        output = f"Table {table_number} ordered:\n"
        for d in table.drink_orders:
            output += repr(d) + '\n'
        output += f'{self.name} does not have in the menu:\n'
        for d in out_menu:
            output += d + '\n'
        return output.strip()

    def leave_table(self, table_number: int):
        table = self.__get_table_by_number(table_number)
        if table is not None:
            bill = table.get_bill()
            self.total_income += bill
            table.clear()
            return f"Table: {table_number}\nBill: {bill:.2f}"

    def get_free_tables_info(self):
        return '\n'.join([t.free_table_info() for t in self.tables_repository if not t.is_reserved])

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    @staticmethod
    def __check_if_items_in_menu(menu, collection):
        in_menu = []
        not_in_menu = []
        for item in collection:
            if item in menu:
                in_menu.append(item)
            else:
                not_in_menu.append(item)
        return in_menu, not_in_menu

    def __get_first_available_table_with_enough_capacity(self, number_of_people):
        for table in self.tables_repository:
            if table.capacity >= number_of_people and not table.is_reserved:
                return table
        return None

    def __get_table_by_number(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table
        return None

    @staticmethod
    def __get_item_by_name(item_name, menu):
        for item in menu:
            if item.name == item_name:
                return item
        return None


b = Bakery('Blabla')
print(b.add_food('Cake', 'Saher', 10))
print(b.add_drink('Tea', 'Green Tea', 200, 'Nestea'))
print(b.add_table('InsideTable', 45, 4))
print(b.add_table('InsideTable', 46, 4))
print(b.reserve_table(4))
print(b.reserve_table(4))
print(b.tables_repository)
print(b.order_food(45, 'Saher', 'Garash'))
print(b.order_drink(45, 'Green Tea', 'Black Tea'))
print(b.leave_table(45))
print(b.get_free_tables_info())
print(b.get_total_income())
# print(b.order_drink(45, 'Black Tea'))