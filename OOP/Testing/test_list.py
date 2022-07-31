import unittest

from Tests.extended_list import IntegerList


class ListTests(unittest.TestCase):

    def setUp(self) -> None:
        self.ll_test = IntegerList(1, 2, 3)

    def test_init__expect_int_value_to_be_added(self):
        test_list = IntegerList(1, 2)
        expected = [1, 2]

        self.assertEqual(expected, test_list. get_data())

    def test_init__with_wrong_type__expect_to_raise(self):
        test_list = IntegerList('a', 2)
        expected = [2]

        self.assertEqual(expected, test_list.get_data())

    def test_get_data__expect_to_return_correct_data(self):
        expected = [1, 2, 3]
        self.assertEqual(expected, self.ll_test.get_data())

    def test_add__expect_to_add_the_element_to_data(self):
        expected = [1, 2, 3, 4]
        self.ll_test.add(4)
        self.assertEqual(expected, self.ll_test.get_data())

    def test_add__expect_to_return_data_after_adding(self):
        actual = self.ll_test.add(4)
        expected = [1, 2, 3, 4]

        self.assertEqual(expected, actual)

    def test_add__with_wrong_type__expect_to_raise(self):
        with self.assertRaises(ValueError) as err:
            self.ll_test.add('hello')

        self.assertIsNotNone(err)

    def test_remove_index__with_correct_number__expect_to_remove_element_at_given_index(self):
        actual = self.ll_test.remove_index(2)
        expected = 3

        self.assertEqual(expected, actual)

    def test_remove_index__with_out_of_range_index__expect_to_raise(self):
        with self.assertRaises(IndexError) as err:
            self.ll_test.remove_index(3)

        self.assertIsNotNone(err)

    def test_get__with_correct_number__expect_to_return_correct_element(self):
        actual = self.ll_test.get(0)
        expected = 1

        self.assertEqual(expected, actual)

    def test_get__with_wrong_number__expect_to_raise(self):
        with self.assertRaises(IndexError) as err:
            self.ll_test.get(3)

        self.assertIsNotNone(err)

    def test_insert__with_correct_values__expect_to_return_correct_data(self):
        self.ll_test.insert(1, 4)
        actual = self.ll_test.get_data()
        expected = [1, 4, 2, 3]

        self.assertEqual(expected, actual)

    def test_insert__with_out_of_range_index__expect_to_raise(self):
        with self.assertRaises(IndexError) as err:
            self.ll_test.insert(4, 4)

        self.assertIsNotNone(err)

    def test_insert__with_incorrect_type__expect_to_raise(self):
        with self.assertRaises(ValueError) as err:
            self.ll_test.insert(1, 'hello')

        self.assertIsNotNone(err)

    def test_get_biggest__expect_to_get_highest_int_value_from_data(self):
        test_ll = IntegerList(1, 2, 4, 7, 12)

        actual = test_ll.get_biggest()
        expected = 12

        self.assertEqual(expected, actual)

    def test_get_index__expect_to_get_index_of_the_element(self):
        test_ll = IntegerList(1, 2, 4, 7, 12)

        actual = test_ll.get_index(7)
        expected = 3

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()


