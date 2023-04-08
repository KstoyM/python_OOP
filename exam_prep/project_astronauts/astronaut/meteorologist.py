from project_astronauts.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    def __init__(self, name, oxygen=90):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= 15