from unittest import TestCase, main

from project.library import Library  # да сложа project


class LibraryTest(TestCase):
    def setUp(self):
        self.library = Library('Haskovo')

    def test_library_initialized_all_attributes(self):
        self.assertEqual('Haskovo', self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_library_by_name_should_raise_exception(self):
        with self.assertRaises(ValueError) as ex:
            self.library.name = ''
        self.assertEqual('Name cannot be empty string!', str(ex.exception))

    def test_library_name_should_return_new_name(self):
        self.assertEqual("Haskovo", self.library.name)
        self.library.name = "Pesho"
        self.assertEqual('Pesho', self.library.name)

    def test_add_book_when_the_author_is_not_registered_should_return_new_value_in_books_by_authors(self):
        book_author = 'King'
        book_title = "IT"
        expected_result = {book_author: [book_title]}
        self.library.add_book(book_author, book_title)
        self.assertEqual(expected_result, self.library.books_by_authors)
        self.assertTrue(book_title in self.library.books_by_authors[book_author])
        self.assertTrue(book_author in self.library.books_by_authors)

    def test_add_book_when_the_author_is_registered_should_return_new_value_in_books_by_authors(self):
        self.library.add_book('King', 'IT')
        second_author = "King"
        book_title = 'Kujo'
        expected_books = ["IT", "Kujo"]
        self.library.add_book(second_author, book_title)
        self.assertEqual(expected_books, self.library.books_by_authors[second_author])
        self.assertTrue(book_title in self.library.books_by_authors[second_author])

    def test_add_book_when_author_is_registered_and_book_is_registered_already_should_return_same_as_before_result(
            self):
        book_author = 'King'
        book_title = "IT"
        self.library.add_book(book_author, book_title)
        second_author = "King"
        book_title2 = 'IT'
        expected_books = ["IT"]
        self.library.add_book(second_author, book_title2)
        self.assertEqual(expected_books, self.library.books_by_authors[book_author])

    def test_add_reader_when_reader_is_not_register_should_return_new_value(self):
        name = 'Pesho'
        result = self.library.add_reader(name)
        self.assertEqual([], self.library.readers[name])
        self.assertEqual(None, result)

    def test_add_reader_when_reader_already_registered_should_return_str(self):
        name = "Pesho"
        self.library.add_reader(name)
        result = self.library.add_reader(name)
        self.assertEqual(f"{name} is already registered in the {self.library.name} library.", result)

    def test_rent_book_when_reader_name_doesnt_exist_in_the_readers_dict_should_return_string(self):
        name = "Gosho"
        book_author = 'King'
        book_title = "IT"
        self.library.add_book(book_author, book_title)
        result = self.library.rent_book(name, book_author, book_title)
        self.assertEqual(f"{name} is not registered in the {self.library.name} Library.", result)
        self.assertTrue(book_author in self.library.books_by_authors)
        self.assertTrue(book_title in self.library.books_by_authors[book_author])

    def test_rent_book_when_book_author_is_not_registered_should_return_str(self):
        name = "Gosho"
        book_author = 'King'
        book_title = "IT"
        self.library.add_reader(name)
        result = self.library.rent_book(name, book_author, book_title)
        self.assertEqual(f"{self.library.name} Library does not have any {book_author}'s books.", result)
        self.assertTrue(name in self.library.readers)

    def test_rent_book_when_the_book_title_is_not_in_library_should_return_str(self):
        name = "Gosho"
        book_author = 'King'
        book_title = "IT"
        self.library.add_reader(name)
        self.library.add_book(book_author, book_title)
        self.assertEqual([book_title], self.library.books_by_authors[book_author])
        second_book_title = 'Kujo'
        result = self.library.rent_book(name, book_author, second_book_title)
        self.assertEqual(f"""{self.library.name} Library does not have {book_author}'s "{second_book_title}".""", result)

    def test_rent_book_when_everything_is_registered_already(self):
        name = "Gosho"
        book_author = 'King'
        book_title = "IT"
        expected_idx = 0
        expected_reader_result = {name: [{book_author: book_title}]}

        self.library.add_reader(name)
        self.library.add_book(book_author, book_title)
        self.assertEqual([], self.library.readers[name])

        self.library.rent_book(name, book_author, book_title)
        self.assertEqual(expected_reader_result, self.library.readers)
        self.assertTrue(book_title in self.library.readers[name][0].values())

        self.assertTrue(book_title not in self.library.books_by_authors[book_author])


if __name__ == '__main__':
    main()
