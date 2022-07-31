import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):

    def setUp(self) -> None:
        self.dog = Mammal('Maylo', 'dog', 'woof')

    def test_init__name__expect_to_be_correct(self):
        actual = self.dog.name
        expected = 'Maylo'

        self.assertEqual(expected, actual)

    def test_init__mammal_type__expect_to_be_correct(self):
        actual = self.dog.type
        expected = 'dog'

        self.assertEqual(expected, actual)

    def test_init__sound__expect_to_be_correct(self):
        actual = self.dog.sound
        expected = 'woof'

        self.assertEqual(expected, actual)

    def test_get_sound__expect_to_be_correct(self):
        actual = self.dog.make_sound()
        expected = f'{self.dog.name} makes woof'

        self.assertEqual(expected, actual)

    def test_get_kingdom__expect_to_be_correct(self):
        actual = self.dog.get_kingdom()
        expected = 'animals'

        self.assertEqual(expected, actual)

    def test_info__expect_correct_data_to_be_returned(self):
        actual = self.dog.info()
        expected = f"{self.dog.name} is of type {self.dog.type}"

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()