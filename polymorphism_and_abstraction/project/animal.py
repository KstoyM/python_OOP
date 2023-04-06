from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def make_sound(self):
        ...

    @property
    @abstractmethod
    def get_class(self):
        ...

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.get_class}"
