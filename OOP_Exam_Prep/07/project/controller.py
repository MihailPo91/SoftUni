from project.tools.factory.car_factory import CarCreator
from project.tools.factory.driver_factory import DriverCreator
from project.tools.factory.race_factory import RaceCreator
from project.tools.validators.validator import Validator


class Controller:
    def __init__(self):
        self.cars = []  # Car objects
        self.drivers = []  # Driver objects
        self.races = []  # Race objects

    def create_car(self, car_type: str, model: str, speed_limit: int):
        valid_types = ['MuscleCar', 'SportsCar']
        if Validator.check_if_valid_car_type(car_type, valid_types):
            message = f"Car {model} is already created!"
            Validator.check_if_model_already_exists(model, [car.model for car in self.cars], message)

            car = CarCreator.create_car(car_type, model, speed_limit)
            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        message = f"Driver {driver_name} is already created!"
        Validator.check_if_driver_already_exists(driver_name, [d.name for d in self.drivers], message)

        driver = DriverCreator.create_driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        message = f"Race {race_name} is already created!"
        Validator.check_if_race_already_exists(race_name, self.races, message)

        race = RaceCreator.create_race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        # Validator.check_if_value_in_list(driver_name,
        #                                  [d.name for d in self.drivers],
        #                                  f"Driver {driver_name} could not be found!")

        driver = self.__get_driver_by_name(driver_name, self.drivers, f"Driver {driver_name} could not be found!")

        if Validator.check_if_valid_car_type(car_type, ["MuscleCar", "SportsCar"]):
            available_cars = self.__check_if_available_cars(car_type, self.cars)
            if not available_cars:
                raise Exception(f"Car {car_type} could not be found!")
            car = available_cars.pop()  # TODO THIS MIGHT NOT GET THE PROPER CAR!!! CHECK LATER IF ERROR!

            if driver.car:
                old_car = driver.car
                driver.car.is_taken = False
                driver.car = car
                driver.car.is_taken = True
                return f"Driver {driver_name} changed his car from {old_car.model} to {driver.car.model}."

            driver.car = car
            driver.car.is_taken = True
            return f"Driver {driver_name} chose the car {driver.car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        # Validator.check_if_value_in_list(race_name,
        #                                  [r.name for r in self.races],
        #                                  f"Race {race_name} could not be found!")
        race = self.__get_race_by_name(race_name, self.races, f"Race {race_name} could not be found!")

        # Validator.check_if_value_in_list(driver_name,
        #                                  [d.name for d in self.drivers],
        #                                  f"Driver {driver_name} could not be found!")
        driver = self.__get_driver_by_name(driver_name, self.drivers, f"Driver {driver_name} could not be found!")
        Validator.check_if_driver_has_car(driver, f"Driver {driver_name} could not participate in the race!")
        if Validator.check_if_driver_was_in_race(driver, race):
            return f"Driver {driver_name} could not participate in the race!"

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        # Validator.check_if_value_in_list(race_name,
        #                                  [r.name for r in self.races],
        #                                  f"Race {race_name} could not be found!")
        race = self.__get_race_by_name(race_name, self.races, f"Race {race_name} could not be found!")
        Validator.check_if_less_than_3_participants_in_race(race.drivers,
                                                            f"Race {race_name} cannot start "
                                                            f"with less than 3 participants!")
        winning_drivers_sorted_by_speed = sorted(race.drivers, key=lambda driver: -driver.car.speed_limit)[:3]
        output = ''
        for winner in winning_drivers_sorted_by_speed:
            winner.number_of_wins += 1
            output += f"Driver {winner.name} wins the {race_name} race with a speed of {winner.car.speed_limit}.\n"

        return output.strip()

    @staticmethod
    def __check_if_available_cars(car_type, car_repository):
        available = []
        for car in car_repository:
            if car.car_type == car_type and not car.is_taken:
                available.append(car)
        return available

    @staticmethod
    def __get_driver_by_name(name, drivers_repository, message):
        for driver in drivers_repository:
            if driver.name == name:
                return driver
        raise Exception(message)

    @staticmethod
    def __get_race_by_name(name, races_repository, message):
        for race in races_repository:
            if race.name == name:
                return race
        raise Exception(message)

# c = Controller()
# print(c.create_car('MuscleCar', 'Mustang', 250))
# print(c.cars)
# print(c.create_car('MuscleCar', 'Mustangd', 250))
# print(c.car_type for c in c.cars)
