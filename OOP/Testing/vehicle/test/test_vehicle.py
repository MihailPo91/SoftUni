import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    FUEL = 100
    HORSE_POWER = 200
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test_init__expect_correct_data(self):
        fuel = 200
        horse_power = 300

        vehicle = Vehicle(fuel, horse_power)

        self.assertEqual(fuel, vehicle.fuel)
        self.assertEqual(horse_power, vehicle.horse_power)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, vehicle.fuel_consumption)
        self.assertEqual(fuel, vehicle.capacity)

    def test_drive__with_enough_fuel__expect_to_decrement_fuel(self):
        distance = 20
        self.vehicle.drive(distance)
        expected = self.FUEL - (distance * self.DEFAULT_FUEL_CONSUMPTION)
        actual = self.vehicle.fuel

        self.assertEqual(expected, actual)

    def test_drive__with_exact_fuel_needed_to_reach_0__expect_to_have_0_fuel(self):
        distance = 80
        self.vehicle.drive(distance)
        expected = self.FUEL - (distance * self.DEFAULT_FUEL_CONSUMPTION)
        actual = self.vehicle.fuel

        self.assertEqual(expected, actual)

    def test_drive__not_enough_fuel__expect_to_raise(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.drive(100)
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual('Not enough fuel', str(error.exception))

    def test_refuel__with_valid_amount__expect_to_increment_fuel(self):
        distance = 60
        self.vehicle.drive(distance)
        # fuel is 100 - 60 * 1.25, which is 25 left
        self.vehicle.refuel(70)  # refueling 70 -> 95 in the tank

        actual = self.vehicle.fuel
        expected = self.FUEL - (60 * self.DEFAULT_FUEL_CONSUMPTION) + 70

        self.assertEqual(expected, actual)

    def test_refuel__with_exact_amount__expect_to_increment_fuel_to_full_capacity(self):
        distance = 80
        self.vehicle.drive(distance)
        # fuel is 100 - 80 * 1.25, which is 0 left
        self.vehicle.refuel(self.vehicle.capacity)  # refueling 100 -> 100 in the tank  (max capacity)

        actual = self.vehicle.fuel
        expected = self.vehicle.capacity

        self.assertEqual(expected, actual)

    def test_refuel__with_invalid_amount__expect_to_raise(self):
        with self.assertRaises(Exception) as error:
            self.vehicle.refuel(self.vehicle.capacity + 1)

        self.assertEqual('Too much fuel', str(error.exception))

    def test_str__expect_correct_string(self):

        actual = str(self.vehicle)
        expected = f"The vehicle has {self.HORSE_POWER} " \
               f"horse power with {self.FUEL} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"

        self.assertEqual(expected, actual)
