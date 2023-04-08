from typing import List

from project_bakery.baked_food.baked_food import BakedFood
from project_bakery.baked_food.bread import Bread
from project_bakery.baked_food.cake import Cake
from project_bakery.drink.drink import Drink
from project_bakery.drink.tea import Tea
from project_bakery.drink.water import Water
from project_bakery.table.inside_table import InsideTable
from project_bakery.table.outside_table import OutsideTable
from project_bakery.table.table import Table


class Bakery:
    POSSIBLE_FOOD_TYPES = {'Bread': Bread,
                           'Cake': Cake}

    POSSIBLE_DRINK_TYPES = {'Tea': Tea,
                            'Water': Water}

    POSSIBLE_TABLE_TYPES = {'InsideTable': InsideTable,
                            'OutsideTable': OutsideTable}

    def __init__(self, name):
        self.name = name
        self.food_menu: List[BakedFood] = []
        self.drinks_menu: List[Drink] = []
        self.tables_repository: List[Table] = []
        self.total_income = 0

    def find_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table
        return f"Could not find table {table_number}"

    def add_food(self, food_type, name, price):
        if food_type in self.POSSIBLE_FOOD_TYPES:
            for food in self.food_menu:
                if food.name == name:
                    raise Exception(f"{food_type} {name} is already in the menu!")
            self.food_menu.append(self.POSSIBLE_FOOD_TYPES[food_type](name, price))
            return f"Added {name} ({food_type}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type in self.POSSIBLE_DRINK_TYPES:
            for drink in self.drinks_menu:
                if drink.name == name:
                    raise Exception(f"{drink_type} {name} is already in the menu!")
            self.drinks_menu.append(self.POSSIBLE_DRINK_TYPES[drink_type](name, portion, brand))
            return f"Added {name} ({brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type in self.POSSIBLE_TABLE_TYPES:
            for table in self.tables_repository:
                if table.table_number == table_number:
                    raise Exception(f"Table {table_number} is already in the bakery!")
            self.tables_repository.append(self.POSSIBLE_TABLE_TYPES[table_type](table_number, capacity))
            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people):
        for table in self.tables_repository:
            if not table.is_reserved and table.capacity >= number_of_people:
                table.reserve(number_of_people)
                return f"Table {table.table_number} has been reserved for {number_of_people} people"
        else:
            return f"No available table for {number_of_people} people"

    def order_food(self, table_number, *food_list):
        table = self.find_table(table_number)
        if isinstance(table, Table):
            result = [f'Table {table_number} ordered:']
            food_not_in_menu = [f'{self.name} does not have in the menu:']
            for f in food_list:
                for avail_food in self.food_menu:
                    if f == avail_food.name:
                        table.order_food(avail_food)
                        result.extend([str(avail_food)])
            else:
                food_not_in_menu.extend([f])
            return '\n'.join(result + food_not_in_menu)
        else:
            return table

    def order_drink(self, table_number, *drinks_list):
        table = self.find_table(table_number)
        if isinstance(table, Table):
            result = [f'Table {table_number} ordered:']
            drinks_not_in_menu = [f'{self.name} does not have in the menu:']
            for d in drinks_list:
                for avail_drinks in self.drinks_menu:
                    if d == avail_drinks.name:
                        table.order_drink(avail_drinks)
                        result.extend([str(avail_drinks)])
            else:
                drinks_not_in_menu.extend([d])
            return '\n'.join(result + drinks_not_in_menu)
        else:
            return table

    def leave_table(self, table_number):
        table = self.find_table(table_number)
        if isinstance(table, Table):
            bill = table.get_bill()
            result = f'Table: {table.table_number}\nBill: {bill:.2f}'
            table.clear()
            self.total_income += bill
            return result
        else:
            return table

    def get_free_tables_info(self):
        result = []
        for table in self.tables_repository:
            result.extend([table.free_table_info()])
        return '\n'.join(result)

    def get_total_income(self):
        return f'Total income: {self.total_income:.2f}'
