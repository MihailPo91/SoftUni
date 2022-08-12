from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar


class CarCreator:
    valid_car_types = {
        'MuscleCar': MuscleCar,
        'SportsCar': SportsCar
    }

    @staticmethod
    def create_car(car_type: str, model: str, speed_limit: int):
        car = CarCreator.valid_car_types[car_type](model, speed_limit)
        return car

