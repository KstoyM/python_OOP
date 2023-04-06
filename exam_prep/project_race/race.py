from typing import List

from project_race.driver import Driver


class Race:

    def __init__(self, name):
        self.name = name
        self.drivers: List[Driver] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("Name cannot be an empty string!")
        self.__name = value