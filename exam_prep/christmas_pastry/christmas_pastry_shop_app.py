from typing import List

from christmas_pastry.booths.booth import Booth
from christmas_pastry.booths.open_booth import OpenBooth
from christmas_pastry.booths.private_booth import PrivateBooth
from christmas_pastry.delicacies.delicacy import Delicacy
from christmas_pastry.delicacies.gingerbread import Gingerbread
from christmas_pastry.delicacies.stolen import Stolen


class ChristmasPastryShopApp:

    def __init__(self):
        self.booths: List[Booth] = []
        self.delicacies: List[Delicacy] = []
        self.income: float = 0

    def add_delicacy(self, type_delicacy, name, price):
        if any(filter(lambda x: x.name == name, self.delicacies)):
            raise Exception(f"{name} already exists!")
        if type_delicacy not in ['Gingerbread', 'Stolen']:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")
        if type_delicacy == 'Gingerbread':
            delicacy = Gingerbread(name, price)
            self.delicacies.append(delicacy)
            return f"Added delicacy {name} - {type_delicacy} to the pastry shop."
        elif type_delicacy == 'Stolen':
            delicacy = Stolen(name, price)
            self.delicacies.append(delicacy)
            return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def find_booth_by_number(self, booth_number):
        booth = next(filter(lambda x: x.booth_number == booth_number, self.booths))
        return booth

    def add_booth(self, type_booth, booth_number, capacity):
        if any(filter(lambda x: x.booth_number == booth_number, self.booths)):
            raise Exception(f"Booth number {booth_number} already exists!")
        if type_booth not in ['Open Booth', "Private Booth"]:
            raise Exception(f"{type_booth} is not a valid booth!")
        if type_booth == 'Open Booth':
            booth = OpenBooth(booth_number, capacity)
            self.booths.append(booth)
            return f"Added booth number {booth_number} in the pastry shop."
        elif type_booth == 'Private Booth':
            booth = PrivateBooth(booth_number, capacity)
            self.booths.append(booth)
            return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people):
        for booth in self.booths:
            if booth.capacity >= number_of_people and not booth.is_reserved:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number, delicacy_name):
        if not any(filter(lambda x: x.booth_number == booth_number, self.booths)):
            raise Exception(f"Could not find booth {booth_number}!")
        if not any(filter(lambda x: x.name == delicacy_name, self.delicacies)):
            raise Exception(f"No {delicacy_name} in the pastry shop!")
        booth = self.find_booth_by_number(booth_number)
        delicacy = (next(filter(lambda x: x.name == delicacy_name, self.delicacies)))

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number):
        booth = self.find_booth_by_number(booth_number)
        bill = booth.price_for_reservation + sum(order.price for order in booth.delicacy_orders)
        self.income += bill
        booth.delicacy_orders.clear()
        booth.is_reserved = False
        booth.price_for_reservation = 0
        return f"Booth {booth_number}:\nBill: {bill:.2f}lv."

    def get_income(self):
        return f"Income: {self.income:.2f}lv."