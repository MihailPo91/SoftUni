import unittest

from worker import Worker

""""
•	Test if the worker is initialized with the correct name, salary, and energy
•	Test if the worker's energy is incremented after the rest method is called
•	Test if an error is raised if the worker tries to work with negative energy or equal to 0
•	Test if the worker's money is increased by his salary correctly after the work method is called
•	Test if the worker's energy is decreased after the work method is called	
•	Test if the get_info method returns the proper string with correct values
"""


class WorkerTests(unittest.TestCase):
    NAME = 'Test Worker'
    SALARY = 1024
    ENERGY = 1

    def setUp(self) -> None:
        self.worker = Worker(self.NAME, self.SALARY, self.ENERGY)

    def test_init__when_valid_props__expect_correct_values(self):
        self.assertEqual(self.NAME, self.worker.name)
        self.assertEqual(self.SALARY, self.worker.salary)
        self.assertEqual(self.ENERGY, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_rest__expect_energy_to_be_incremented(self):
        self.worker.rest()

        self.assertEqual(2, self.worker.energy)

    def test_work__when_energy_is_0__expect_to_raise(self):
        self.worker.work()

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertIsNotNone(ex)

    def test_work__when_enough_energy__expect_money_to_be_increased_by_salary(self):
        self.worker.work()

        self.assertEqual(self.SALARY, self.worker.money)

    def test_work__when_enough_energy__expect_energy_to_decrement(self):
        self.worker.work()

        self.assertEqual(0, self.worker.energy)

    def test_get_info__expect_correct_result(self):

        actual_info = self.worker.get_info()
        expected_info = f'{self.NAME} has saved 0 money.'

        self.assertEqual(expected_info, actual_info)


if __name__ == '__main__':
    unittest.main()
