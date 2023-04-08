from abc import ABC, abstractmethod
from typing import List

from project.robots.base_robot import BaseRobot


class BaseService(ABC):
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.robots: List[BaseRobot] = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Service name cannot be empty!")
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")
        self.__capacity = value

    @property
    @abstractmethod
    def get_type(self):
        ...

    @abstractmethod
    def decrease_capacity(self):
        ...

    def details(self):
        result = f'{self.name} {self.get_type}:\n' \
                 f'Robots: '
        if self.robots:
            robots = " ".join([r.name for r in self.robots])
            result += robots
        else:
            result += 'none'
        return result # to_be_tested
