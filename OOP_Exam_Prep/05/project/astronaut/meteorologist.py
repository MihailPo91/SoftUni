from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    OXYGEN = 90

    def __init__(self, name: str):
        super().__init__(name, oxygen=self.OXYGEN)

    def breathe(self):
        self.oxygen -= 15
