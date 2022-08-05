import unittest

from project.factory.paint_factory import PaintFactory


class TestFactory(unittest.TestCase):
    NAME = 'TEST FACTORY'
    CAPACITY = 10

    def setUp(self) -> None:
        self.factory = PaintFactory(self.NAME, self.CAPACITY)

    def test_init(self):
        self.assertEqual(self.NAME, self.factory.name)
        self.assertEqual(self.CAPACITY, self.factory.capacity)
        self.assertEqual({}, self.factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)

    def test_add_ingredient__when_value_is_valid(self):
        product_type = "white"
        product_quantity = 5
        self.factory.add_ingredient(product_type, product_quantity)

        self.assertEqual({product_type: product_quantity}, self.factory.ingredients)

    def test_add_ingredient__when_value_is_NOT_valid__expect_to_raise(self):
        product_type = "trololo"
        product_quantity = 5

        with self.assertRaises(TypeError) as error:
            self.factory.add_ingredient(product_type, product_quantity)

        self.assertEqual(f"Ingredient of type {product_type} not allowed"
                         f" in {self.factory.__class__.__name__}", str(error.exception))

    def test_add_ingredient_and_can_add__when_not_enough_capacity__expect_to_raise(self):
        factory = PaintFactory(self.NAME, 0)
        with self.assertRaises(ValueError) as error:
            factory.add_ingredient('white', 1)

        self.assertEqual("Not enough space in factory", str(error.exception))

    def test_add_ingredient_correct_value__not_empty_dict__expect_to_add_value(self):
        product_type = "white"
        product_quantity = 5
        self.factory.add_ingredient(product_type, product_quantity)

        self.factory.add_ingredient(product_type, 3)

        self.assertEqual(8, self.factory.ingredients[product_type])

    def test_remove_ingredient__happy_case__expect_to_remove(self):
        product_type = "white"
        product_quantity = 5
        self.factory.add_ingredient(product_type, product_quantity)

        self.factory.remove_ingredient(product_type, 3)
        self.assertEqual(2, self.factory.ingredients[product_type])

        self.factory.remove_ingredient(product_type, 2)
        self.assertEqual(0, self.factory.ingredients[product_type])

    def test_remove_ingredient__when_no_such_ingredient_exist__expect_to_raise(self):
        product_type = "white"
        product_quantity = 5

        with self.assertRaises(KeyError) as error:
            self.factory.remove_ingredient(product_type, product_quantity)

        self.assertEqual("'No such ingredient in the factory'", str(error.exception))

    def test_remove_ingredient__when_the_amount_to_remove_is_higher_than_the_actual_amount__expect_raise(self):
        product_type = "white"
        product_quantity = 5
        self.factory.add_ingredient(product_type, product_quantity)

        with self.assertRaises(ValueError) as error:
            self.factory.remove_ingredient(product_type, 6)

        self.assertEqual("Ingredients quantity cannot be less than zero", str(error.exception))

    def test_products_property(self):
        product_type = "white"
        product_quantity = 5
        self.factory.add_ingredient(product_type, product_quantity)

        self.assertEqual({product_type: product_quantity}, self.factory.products)

    def test_repr__expect_correct_output(self):
        self.assertEqual('Factory name: TEST FACTORY with capacity 10.\n', repr(self.factory))