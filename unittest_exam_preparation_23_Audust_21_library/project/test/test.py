from unittest import TestCase, main

from project.library import Library


class LibraryTests(TestCase):

    def setUp(self) -> None:
        self.library = Library("Library")

    def test_correct_init(self):
        self.assertEqual("Library", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_name_can_not_be_empty_str_rises(self):

        with self.assertRaises(ValueError) as ve:
            self.library = Library("")
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_book_should_add_author_title(self):
        author = "Author"
        first_tittle = "Title1"
        second_tittle = "Title2"

        self.library.add_book(author, first_tittle)
        self.library.add_book(author, first_tittle)
        self.library.add_book(author, second_tittle)

        self.assertEqual(1, len(self.library.books_by_authors))
        self.assertTrue(author in self.library.books_by_authors)
        self.assertEqual([first_tittle, second_tittle], self.library.books_by_authors[author])

    def test_add_reader_should_add_reader(self):
        reader_name = "Reader"

        self.library.add_reader(reader_name)

        self.assertEqual(1, len(self.library.readers))
        self.assertTrue(reader_name in self.library.readers)
        self.assertEqual([], self.library.readers[reader_name])

    def test_add_reader_rises_if_reader_exist(self):
        reader_name = "Reader"

        self.library.add_reader(reader_name)
        result = self.library.add_reader(reader_name)

        self.assertEqual(f"{reader_name} is already registered in the {self.library.name} library.", result)

    def test_rent_book_if_reader_is_not_registered_return_error(self):
        reader_name = "Reader"
        result = self.library.rent_book(reader_name, "Author", "Title1")
        self.assertEqual(f"{reader_name} is not registered in the {self.library.name} Library.", result)

    def test_rent_book_if_author_is_not_registered_return_error(self):
        reader_name = "Reader"
        author_name = "Author"
        self.library.add_reader(reader_name)

        result = self.library.rent_book(reader_name, author_name, "Title1")
        self.assertEqual(f"{self.library.name} Library does not have any {author_name}'s books.", result)

    def test_rent_book_if_title_is_not_registered_return_error(self):
        reader_name = "Reader"
        author_name = "Author"
        invalid_title = "InvalidTitle"
        self.library.add_reader(reader_name)
        self.library.add_book(author_name, "random_title")

        result = self.library.rent_book(reader_name, author_name, invalid_title)
        self.assertEqual(f"""{self.library.name} Library does not have {author_name}'s "{invalid_title}".""", result)

    def test_rent_book_should_properly_rent_book(self):
        reader_name = "Reader"
        author_name = "Author"
        title = "Title"
        self.library.add_reader(reader_name)
        self.library.add_book(author_name, title)

        self.library.rent_book(reader_name, author_name, title)
        self.assertEqual([{author_name: title}], self.library.readers[reader_name])
        self.assertTrue(title not in self.library.books_by_authors[author_name])


if __name__ == "__main__":
    main()