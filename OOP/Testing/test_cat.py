import unittest

from Tests.cat import Cat

"""
•	Cat's size is increased after eating
•	Cat is fed after eating
•	Cat cannot eat if already fed, raises an error
•	Cat cannot fall asleep if not fed, raises an error
•	Cat is not sleepy after sleeping
"""


class CatTests(unittest.TestCase):

    NAME = "Test Cat"

    def setUp(self) -> None:
        self.cat = Cat(self.NAME)

    def test_eat__expect_size_to_increment(self):
        self.cat.eat()

        self.assertEqual(1, self.cat.size)

    def test_eat__expect_fed_is_True_after_eating(self):
        self.cat.eat()

        self.assertTrue(self.cat.fed)

    def test_eat__if_fed_already__expect_cannot_eat_again(self):
        self.cat.eat()

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertIsNotNone(ex)

    def test_sleep__if_not_fed__expect_cannot_fall_asleep(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertIsNotNone(ex)

    def test_sleep__expect_sleepy_is_False_after_sleep(self):
        self.cat.eat()
        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
