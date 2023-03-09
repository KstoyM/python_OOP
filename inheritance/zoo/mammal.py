from zoo.animal import Animal


class Mammal(Animal):
    pass

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
