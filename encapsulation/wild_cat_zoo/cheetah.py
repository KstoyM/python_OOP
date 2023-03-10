from wild_cat_zoo.animal import Animal


class Cheetah(Animal):
    MONEY_FOR_CARE = 60

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender, Cheetah.MONEY_FOR_CARE)