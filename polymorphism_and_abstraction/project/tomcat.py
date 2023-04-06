from project_war_game.cat import Cat


class Tomcat(Cat):
    def __init__(self, name, age):
        super().__init__(name, age, gender='Male')

    def make_sound(self):
        return "Hiss"

    @property
    def get_class(self):
        return self.__class__.__name__