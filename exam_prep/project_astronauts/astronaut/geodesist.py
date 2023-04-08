from project_astronauts.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    def __init__(self, name,  oxygen=50):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= 10