import unittest
from project.pet_shop import PetShop


class TestPetShop(unittest.TestCase):
    NAME = "TEST SHOP"

    def setUp(self) -> None:
        self.shop = PetShop(self.NAME)

    def test_init(self):
        self.assertEqual(self.NAME, self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_add_food_when_quantity_less_or_equal_to_0__expect_raise(self):
        food_name = 'Nice Food'

        with self.assertRaises(ValueError) as error:
            self.shop.add_food(food_name, 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.shop.add_food(food_name, -2)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(error.exception))

    def test_add_food_when_food_not_yet_added__expect_food_as_key_0_as_value(self):
        food_name = 'Nice Food'
        result = self.shop.add_food(food_name, 5)
        self.assertEqual({food_name: 5}, self.shop.food)
        self.assertEqual(f"Successfully added {5:.2f} grams of {food_name}.", result)

        result2 = self.shop.add_food(food_name, 10)
        self.assertEqual({food_name: 15}, self.shop.food)
        self.assertEqual(f"Successfully added {10:.2f} grams of {food_name}.", result2)

    def test_add_pet_when_name_already_exists__expect_raise(self):
        pet_name = 'Shosho'
        self.shop.add_pet(pet_name)

        with self.assertRaises(Exception) as error:
            self.shop.add_pet(pet_name)

        self.assertEqual("Cannot add a pet with the same name", str(error.exception))

    def test_add_pet_happy_case(self):
        pet_name = 'Shosho'
        result = self.shop.add_pet(pet_name)
        self.assertEqual(f"Successfully added {pet_name}.", result)
        self.assertEqual([pet_name], self.shop.pets)

    def test_feed_pet_with_invalid_name__expect_raise(self):
        food_name = 'Nice Food'
        pet_name = 'Gosho'
        self.shop.add_food(food_name, 5)
        with self.assertRaises(Exception) as error:
            self.shop.feed_pet(food_name, pet_name)

        self.assertEqual(f"Please insert a valid pet name", str(error.exception))

    def test_feed_pet_with_invalid_food__expect_raise(self):
        pet_name = 'Shosho'
        result = self.shop.add_pet(pet_name)

        result = self.shop.feed_pet('Blabla', pet_name)
        self.assertEqual(f"You do not have {'Blabla'}", result)

    def test_feed_pet_when_food_is_not_enough(self):
        pet_name = 'Shosho'
        food_name = 'Nice Food'
        self.shop.add_pet(pet_name)
        self.shop.add_food(food_name, 50)
        result = self.shop.feed_pet(food_name, pet_name)
        self.assertEqual("Adding food...", result)
        self.assertEqual(1050, self.shop.food[food_name])

    def test_feed_pet_happy_case(self):
        pet_name = 'Shosho'
        food_name = 'Nice Food'
        self.shop.add_pet(pet_name)
        self.shop.add_food(food_name, 150)
        result = self.shop.feed_pet(food_name, pet_name)
        self.assertEqual(f"{pet_name} was successfully fed", result)
        self.assertEqual(50, self.shop.food[food_name])

    def test_repr(self):
        pet_name = 'Shosho'
        self.shop.add_pet(pet_name)
        expected = f'Shop {self.NAME}:\n' \
               f'Pets: {", ".join([pet_name])}'

        actual = repr(self.shop)

        self.assertEqual(expected, actual)
