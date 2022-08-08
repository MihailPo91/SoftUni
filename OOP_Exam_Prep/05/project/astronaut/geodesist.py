from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    OXYGEN = 50

    def __init__(self, name: str):
        super().__init__(name, oxygen=self.OXYGEN)

    def breathe(self):
        self.oxygen -= 10
