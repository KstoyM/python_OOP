from wild_farm.animals.animal import Bird
from wild_farm.food import Meat, Vegetable, Fruit, Seed


class Owl(Bird):

    @staticmethod
    def make_sound():
        return "Hoot Hoot"

    @property
    def food_that_eats(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25

class Hen(Bird):

    @staticmethod
    def make_sound():
        return "Cluck"

    @property
    def food_that_eats(self):
        return [Meat, Vegetable, Fruit, Seed]

    @property
    def gained_weight(self):
        return 0.35