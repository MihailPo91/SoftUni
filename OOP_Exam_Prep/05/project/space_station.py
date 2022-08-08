from collections import deque

from project.astronaut.astronaut_repository import AstronautRepository
from project.helpers.factory.astronaut_factory import AstronautFactory
from project.helpers.factory.planet_factory import PlanetFactory
from project.helpers.validator.validators import Validator
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:

    successful_missions = 0
    failed_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):

        if self.astronaut_repository.find_by_name(name):
            return f"{name} is already added."

        astronaut = AstronautFactory.create_astronaut(astronaut_type, name)
        self.astronaut_repository.add(astronaut)

        return f"Successfully added {astronaut_type}: {astronaut.name}."

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f"{name} is already added."

        planet = PlanetFactory.create_planet(name, items)

        self.planet_repository.add(planet)
        return f"Successfully added Planet: {planet.name}."

    def retire_astronaut(self, name: str):
        Validator.check_if_astronaut_name_is_in_repository(self.astronaut_repository, name)
        astronaut = self.astronaut_repository.find_by_name(name)

        self.astronaut_repository.remove(astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        Validator.check_if_planet_exists(self.planet_repository, planet_name)
        planet = self.__get_planet_by_name(planet_name)

        astronaut_team = deque([a for a in (sorted(self.astronaut_repository.astronauts,
                                            key=lambda a: -a.oxygen)) if a.oxygen > 30][:5])

        Validator.check_if_there_are_any_suitable_astronauts(astronaut_team)
        mission_success, participants = self.planet_exploration(planet, astronaut_team)

        if mission_success:
            self.successful_missions += 1
            return f"Planet: {planet_name} was explored. {participants} astronauts participated in collecting items."
        else:
            self.failed_missions += 1
            return "Mission is not completed."

    @staticmethod
    def planet_exploration(planet: Planet, team):
        counter = 0
        successful = True
        current_astronaut = team.popleft()
        counter += 1
        while planet.items:
            current_astronaut.backpack.append(planet.items.pop())
            current_astronaut.breathe()
            if current_astronaut.oxygen <= 0:
                if team:
                    current_astronaut = team.popleft()
                    counter += 1
                else:
                    successful = False
                    break
        return successful, counter

    def report(self):
        output = f"{self.successful_missions} successful missions!\n"
        output += f"{self.failed_missions} missions were not completed!\n"
        output += f" Astronauts' info:\n"
        for astronaut in self.astronaut_repository.astronauts:
            backpack = ', '.join(astronaut.backpack) if astronaut.backpack else 'none'
            output += f"Name: {astronaut.name}\n"
            output += f"Oxygen: {astronaut.oxygen}\n"
            output += f"Backpack items: {backpack}\n"

        return output.strip()

    def __get_planet_by_name(self, planet_name):
        for planet in self.planet_repository.planets:
            if planet.name == planet_name:
                return planet
        return None


ss = SpaceStation()

print(ss.add_astronaut('Biologist', 'Marko'))
