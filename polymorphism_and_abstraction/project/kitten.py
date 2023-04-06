from project.cat import Cat


class Kitten(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, gender='Female')

    def make_sound(self):
        return "Meow"

    @property
    def get_class(self):
        return self.__class__.__name__