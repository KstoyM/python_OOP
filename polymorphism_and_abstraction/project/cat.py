from project_war_game.animal import Animal


class Cat(Animal):

    def make_sound(self):
        return "Meow meow!"

    @property
    def get_class(self):
        return self.__class__.__name__