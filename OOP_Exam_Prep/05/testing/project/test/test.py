import unittest
from project.library import Library


class TestLibrary(unittest.TestCase):
    NAME = 'Orange'

    def setUp(self) -> None:
        self.library = Library(self.NAME)

    def test_init_name__with_empty_string__expect_to_raise(self):
        with self.assertRaises(ValueError) as error:
            library = Library('')

        self.assertEqual("Name cannot be empty string!", str(error.exception))

    def test_init_happy_case__expect_to_get_all_attributes(self):
        self.assertEqual(self.NAME, self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_add_book_when_author_doesnt_exist__expect_to_create_author_as_key_book_as_value(self):
        author = 'J.K. Rowling'
        book = 'Harry Potter'
        self.library.add_book(author, book)

        self.assertEqual(['Harry Potter'], self.library.books_by_authors[author])

    def test_add_book_when_author_already_there__expect_to_append_book(self):
        author = 'J.K. Rowling'
        book = 'Harry Potter'
        book2 = 'Cursed Child'

        self.library.add_book(author, book)
        self.assertEqual(['Harry Potter'], self.library.books_by_authors[author])
        self.library.add_book(author, book2)
        self.assertEqual(['Harry Potter', 'Cursed Child'], self.library.books_by_authors[author])

    def test_add_reader_when_reader_already_added_expect_boom_boom(self):
        reader = 'Mike'
        self.library.add_reader(reader)
        result = self.library.add_reader(reader)

        self.assertEqual(f"{reader} is already registered in the {self.library.name} library.", result)

    def test_add_reader_happy_case(self):
        reader = 'Mike'
        self.library.add_reader(reader)

        self.assertEqual([], self.library.readers[reader])

    def test_rent_book_if_invalid_reader__expect_return(self):
        reader = 'Mike'
        author = 'J.K. Rowling'
        book = 'Harry Potter'
        self.library.add_book(author, book)

        result = self.library.rent_book(reader, author, book)
        self.assertEqual(f"{reader} is not registered in the {self.library.name} Library.", result)

    def test_rent_book_if_invalid_author__expect_return(self):
        reader = 'Mike'
        author = 'J.K. Rowling'
        book = 'Harry Potter'
        self.library.add_reader(reader)

        result = self.library.rent_book(reader, author, book)
        self.assertEqual(f"{self.library.name} Library does not have any {author}'s books.", result)

    def test_rent_book_with_invalid_book__expect_raise(self):
        reader = 'Mike'
        author = 'J.K. Rowling'
        book = 'Harry Potter'
        book2 = 'Cursed Child'

        self.library.add_reader(reader)
        self.library.add_book(author, book)
        result = self.library.rent_book(reader, author, book2)

        self.assertEqual(f"""{self.library.name} Library does not have {author}'s "{book2}".""", result)

    def test_rent_book_happy_case__expect_to_add_book_to_reader_and_remove_from_library(self):
        reader = 'Mike'
        author = 'J.K. Rowling'
        book = 'Harry Potter'
        book2 = 'Cursed Child'
        self.library.add_reader(reader)
        self.library.add_book(author, book)
        self.library.add_book(author, book2)
        self.library.rent_book(reader, author, book)

        self.assertEqual([{'J.K. Rowling': 'Harry Potter'}], self.library.readers[reader])
        self.assertEqual(['Cursed Child'], self.library.books_by_authors[author])