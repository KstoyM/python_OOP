from project_bakery.baked_food.baked_food import BakedFood


class Bread(BakedFood):
    BREAD_PORTION = 200

    def __init__(self, name, price):
        super().__init__(name, self.BREAD_PORTION, price)

