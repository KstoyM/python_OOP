from abc import ABC, abstractmethod
from typing import List

from project.delicacies.delicacy import Delicacy


class Booth(ABC):

    def __init__(self, booth_number: int, capacity: int):
        self.booth_number = booth_number
        self.capacity = capacity
        self.delicacy_orders: List[Delicacy] = []
        self.price_for_reservation: float = 0
        self.is_reserved: bool = False

    @abstractmethod
    def reserve(self, number_of_people: int):
        ...
