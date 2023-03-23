from typing import List

from project.computer_types.computer import Computer
from project.computer_types.desktop_computer import DesktopComputer
from project.computer_types.laptop import Laptop


class ComputerStoreApp:

    def __init__(self):
        self.warehouse: List[Computer] = []
        self.profits = 0

    def build_computer(self, type_computer, manufacturer, model, processor, ram):
        if type_computer == 'Desktop Computer':
            computer = DesktopComputer(manufacturer, model)
        elif type_computer == "Laptop":
            computer = Laptop(manufacturer, model)
        else:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        configuration = computer.configure_computer(processor, ram)
        self.warehouse.append(computer)

        return configuration

    def sell_computer(self, client_budget, wanted_processor, wanted_ram):
        for computer in self.warehouse:
            if computer.price <= client_budget and \
                    computer.processor == wanted_processor and \
                    computer.ram >= wanted_ram:

                self.profits += client_budget - computer.price
                self.warehouse.remove(computer)

                return f"{computer} sold for {client_budget}$."

        raise Exception("Sorry, we don't have a computer for you.")


computer_store = ComputerStoreApp()
print(computer_store.build_computer("Laptop", "Apple", "Macbook", "Apple M1 Pro", 64))
print(computer_store.sell_computer(10000, "Apple M1 Pro", 32))

