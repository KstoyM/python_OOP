from project_war_game.animal import Animal


class Dog(Animal):

    def make_sound(self):
        return "Woof!"

    @property
    def get_class(self):
        return self.__class__.__name__
    