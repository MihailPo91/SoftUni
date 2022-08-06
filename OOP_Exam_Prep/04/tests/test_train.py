import unittest

from project.train.train import Train


class TestTrain(unittest.TestCase):
    NAME = 'Hippy train'
    CAPACITY = 10

    def setUp(self) -> None:
        self.train = Train(self.NAME, self.CAPACITY)

    def test_init(self):
        self.assertEqual(self.NAME, self.train.name)
        self.assertEqual(self.CAPACITY, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_with_full_capacity__expect_to_raise(self):
        passenger_name = 'Gosho'
        self.train.capacity = 0

        with self.assertRaises(ValueError) as error:
            self.train.add(passenger_name)

        self.assertEqual("Train is full", str(error.exception))

    def test_add_with_passenger_already_on_board__expect_to_raise(self):
        passenger_name = 'Gosho'
        self.train.add(passenger_name)

        with self.assertRaises(ValueError) as error:
            self.train.add(passenger_name)

        self.assertEqual(f"Passenger {passenger_name} Exists", str(error.exception))

    def test_add_happy_case_expect_to_work(self):
        passenger_name = 'Gosho'
        result = self.train.add(passenger_name)

        self.assertEqual(f"Added passenger {passenger_name}", result)

        self.assertEqual([passenger_name], self.train.passengers)

    def test_remove_when_trying_to_remove_someone_that_is_not_on_the_train__expect_raise(self):
        with self.assertRaises(ValueError) as error:
            self.train.remove('Gosho')

        self.assertEqual("Passenger Not Found", str(error.exception))

    def test_remove_happy_case_expect_buttery_smooth_removal(self):
        passenger_name = 'Gosho'
        self.train.add(passenger_name)

        self.assertEqual([passenger_name], self.train.passengers)

        result = self.train.remove(passenger_name)

        self.assertEqual(f"Removed {passenger_name}", result)
        self.assertEqual([], self.train.passengers)