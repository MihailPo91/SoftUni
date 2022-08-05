import unittest

from project.plantation import Plantation  # TODO FIX THIS ONE OR IT WONT WORK !!!!!!!!!!!


class TestPlantation(unittest.TestCase):
    SIZE = 5

    def setUp(self) -> None:
        self.plantation = Plantation(self.SIZE)

    def test_init(self):
        self.assertEqual(self.SIZE, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_init_size__with_invalid_value__expect_to_raise(self):
        with self.assertRaises(ValueError) as error:
            plantation = Plantation(-2)

        self.assertEqual("Size must be positive number!", str(error.exception))

    def test_hire_worker__with_worker_already_hired__expect_to_raise(self):
        self.plantation.hire_worker('Gosho')
        with self.assertRaises(ValueError) as error:
            self.plantation.hire_worker('Gosho')

        self.assertEqual("Worker already hired!", str(error.exception))

    def test_hire_worker__with_valid_worker__expect_to_add(self):
        worker_name = 'Gosho'
        result = self.plantation.hire_worker(worker_name)

        self.assertEqual(f"{worker_name} successfully hired.", result)
        self.assertEqual(['Gosho'], self.plantation.workers)

    def test_len_expect_correct_value_returned(self):
        plants = {'Gosho': ['rose', 'lilly', 'daisy'], 'Pesho': ['tomato', 'potato']}
        self.plantation.plants = plants
        actual_result = len(self.plantation)
        expected_result = sum([len(value) for value in plants.values()])

        self.assertEqual(expected_result, actual_result)

    def test_planting__with_invalid_worker__expect_to_raise(self):
        worker = 'Gosho'
        with self.assertRaises(ValueError) as error:
            self.plantation.planting(worker, 'test_plant')

        self.assertEqual(f"Worker with name {worker} is not hired!", str(error.exception))

    def test_planting__len_greater_than_size__expect_to_raise(self):
        plants = {'Gosho': ['rose', 'lilly', 'daisy'], 'Pesho': ['tomato', 'potato']}
        self.plantation.workers = ['Gosho', 'Pesho']
        self.plantation.plants = plants

        with self.assertRaises(ValueError) as error:
            self.plantation.planting('Gosho', 'cucumber')

        self.assertEqual("The plantation is full!", str(error.exception))

    def test_planting__when_first_plant_is_planted__expect_to_create_key_value_in_plants(self):
        self.plantation.workers = ['Gosho', 'Pesho']

        result = self.plantation.planting('Gosho', 'rose')

        self.assertEqual(f"Gosho planted it's first rose.", result)
        self.assertEqual({'Gosho': ['rose']}, self.plantation.plants)

    def test_planting__when_already_are_plants__expect_to_append_to_plants(self):
        self.plantation.workers = ['Gosho', 'Pesho']
        self.plantation.planting('Gosho', 'rose')
        result = self.plantation.planting('Gosho', 'daisy')

        self.assertEqual({'Gosho': ['rose', 'daisy']}, self.plantation.plants)
        self.assertEqual(f"Gosho planted daisy.", result)

    def test_str__expect_correct_result(self):
        plants = {'Gosho': ['rose', 'lilly', 'daisy'], 'Pesho': ['tomato', 'potato']}
        self.plantation.workers = ['Gosho', 'Pesho']
        self.plantation.plants = plants
        actual_result = str(self.plantation)

        expected_result = 'Plantation size: 5\nGosho, Pesho\n' \
                          'Gosho planted: rose, lilly, daisy\nPesho planted: tomato, potato'

        self.assertEqual(expected_result, actual_result)

    def test_repr__expect_correct_result(self):
        self.plantation.workers = ['Gosho', 'Pesho']

        actual_result = repr(self.plantation)
        expected_result = 'Size: 5\nWorkers: Gosho, Pesho'

        self.assertEqual(expected_result, actual_result)
