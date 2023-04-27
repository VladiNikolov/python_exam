
from unittest import TestCase, main

from project.bookstore import Bookstore


class BookstoreTests(TestCase):
    def setUp(self) -> None:
        self.bookstore = Bookstore(13)
        # self.books = {
        #     "Book1": 3,
        #     "Book2": 5
        # }

    def test_correct_init(self):
        self.assertEqual(13, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore._Bookstore__total_sold_books)

    def test_setter_books_limit_raise(self):
        with self.assertRaises(ValueError) as ve:
            self.bookstore.books_limit = 0
        self.assertEqual(f"Books limit of 0 is not valid", str(ve.exception))

    def test_correct__len__method(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Book1": 3,
            "Book2": 5
        }
        # self.bookstore.availability_in_store_by_book_titles = self.books

        self.assertEqual(8, len(self.bookstore))

    def test_not_enough_space_for_book_rises_exception(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Book1": 3,
            "Book2": 5
        }
        # self.bookstore.availability_in_store_by_book_titles = self.books

        with self.assertRaises(Exception) as ex:
            self.bookstore.receive_book("Book3", 6)
        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test_add_new_book(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Book1": 3,
            "Book2": 5
        }
        # self.bookstore.availability_in_store_by_book_titles = self.books
        result = self.bookstore.receive_book("Book3", 2)

        self.assertEqual(f"2 copies of Book3 are available in the bookstore.", result)
        self.assertEqual({"Book1": 3, "Book2": 5, "Book3": 2,}, self.bookstore.availability_in_store_by_book_titles)

    def test_add_existing_book(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Book1": 3,
            "Book2": 5
        }
        result = self.bookstore.receive_book("Book2", 1)

        self.assertEqual(f"6 copies of Book2 are available in the bookstore.", result)

    def test_sell_book_if_not_exist_rises_exception(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Book1": 3,
            "Book2": 5
        }
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Book3", 1)
        self.assertEqual(f"Book Book3 doesn't exist!", str(ex.exception))

    def test_sell_book_more_copies_then_available_raises_exception(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Book1": 3,
            "Book2": 5
        }
        with self.assertRaises(Exception) as ex:
            self.bookstore.sell_book("Book1", 4)
        self.assertEqual(f"Book1 has not enough copies to sell. Left: 3", str(ex.exception))

    def test_successfully_selling_a_book(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Book1": 3,
            "Book2": 5
        }
        result = self.bookstore.sell_book("Book1", 2)
        self.assertEqual(f"Sold 2 copies of Book1", result)
        self.assertEqual(2, self.bookstore._Bookstore__total_sold_books)
        self.assertEqual({"Book1": 1, "Book2": 5}, self.bookstore.availability_in_store_by_book_titles)

    def test_str_(self):
        self.bookstore.availability_in_store_by_book_titles = {
            "Book1": 3,
            "Book2": 5
        }
        self.assertEqual(f"Total sold books: 0\n" + f"Current availability: 8\n" + f" - Book1: 3 copies\n" + f" - Book2: 5 copies", str(self.bookstore))












if __name__ == "__main__":
    main()