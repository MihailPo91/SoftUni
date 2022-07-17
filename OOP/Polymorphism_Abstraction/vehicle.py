from abc import ABC, abstractmethod
import unittest


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass
    
    @abstractmethod
    def refuel(self, fuel):
        pass
    

class Car(Vehicle):
    AC_ADDED_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    def drive(self, distance):
        fuel_to_consume = distance * (self.fuel_consumption + self.AC_ADDED_CONSUMPTION)
        if fuel_to_consume <= self.fuel_quantity:
            self.fuel_quantity -= fuel_to_consume

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    AC_ADDED_CONSUMPTION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    def drive(self, distance):
        fuel_to_consume = distance * (self.fuel_consumption + self.AC_ADDED_CONSUMPTION)
        if fuel_to_consume <= self.fuel_quantity:
            self.fuel_quantity -= fuel_to_consume

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95
        
    
car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)


# test car


class VehiclesTests(unittest.TestCase):
    def test_first_zero(self):
        car = Car(20, 5)
        car.drive(3)
        self.assertEqual(car.fuel_quantity, 2.299999999999997)
        car.refuel(10)
        self.assertEqual(car.fuel_quantity, 12.299999999999997)


if __name__ == '__main__':
    unittest.main()