from abc import ABC, abstractmethod
from typing import List

from project_bakery.baked_food.baked_food import BakedFood
from project_bakery.drink.drink import Drink


class Table(ABC):
    def __init__(self, table_number, capacity):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders: List[BakedFood] = []
        self.drink_orders: List[Drink] = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Capacity has to be greater than 0!")
        self.__capacity = value

    def reserve(self, number_of_people):
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        bill = sum([d.price for d in self.drink_orders]) + sum([f.price for f in self.food_orders])
        return bill

    def clear(self):
        self.drink_orders.clear()
        self.food_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    @property
    @abstractmethod
    def table_type(self):
        ...

    def free_table_info(self):
        if not self.is_reserved:
            return f'Table: {self.table_number}\nType: {self.table_type}\nCapacity: {self.capacity}'