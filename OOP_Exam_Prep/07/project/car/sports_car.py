from project.car.car import Car


class SportsCar(Car):
    def __init__(self, model, speed_limit):
        super().__init__(model, speed_limit)

    @property
    def car_type(self):
        return 'SportsCar'

    @property
    def min_speed_limit(self):
        return 400

    @property
    def max_speed_limit(self):
        return 600


sc = SportsCar('Skyline', 450)