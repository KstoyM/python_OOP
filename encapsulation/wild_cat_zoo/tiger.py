from wild_cat_zoo.animal import Animal


class Tiger(Animal):
    MONEY_FOR_CARE = 45

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender, Tiger.MONEY_FOR_CARE)