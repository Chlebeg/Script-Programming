import unittest
from Bigger_library_class import *

class Test_Bigger_Library(unittest.TestCase):

    def test_parseFileLine(self):
        library = Library('database.txt')
        library.parseFileLine()
        simmilar_to_book1 = Book("Book1", "Author1")
        simmilar_to_book2 = Book("Book2", "Author2")
        self.assertEqual(library.myBooks[0].title, simmilar_to_book1.title)
        self.assertEqual(library.myBooks[0].author, simmilar_to_book1.author)
        self.assertEqual(library.myBooks[1].title, simmilar_to_book2.title)
        self.assertEqual(library.myBooks[1].author, simmilar_to_book2.author)

    def test_find_my_book(self):
        library = Library('database.txt')
        library.parseFileLine()

        similar_to_book1 = Book("Book1", "Author1")
        function_result1 = library.findMyBook(1)
        self.assertTrue(library.findMyBook(1))
        self.assertEqual(function_result1.title, similar_to_book1.title)
        self.assertEqual(function_result1.author, similar_to_book1.author)

        similar_to_book2 = Book("Book2", "Author2")
        function_result2 = library.findMyBook(2)
        self.assertTrue(library.findMyBook(2))
        self.assertEqual(function_result2.title, similar_to_book2.title)
        self.assertEqual(function_result2.author, similar_to_book2.author)

        self.assertFalse(library.findMyBook(3))
        self.assertFalse(library.findMyBook(0))

    def test_find_my_reader(self):
        library = Library('database.txt')
        library.parseFileLine()

        similar_to_reader1 = Reader("Bomek", "Tojdys", "1")
        function_result1 = library.findMyReader(1)
        self.assertTrue(function_result1)
        self.assertEqual(function_result1.name, similar_to_reader1.name)
        self.assertEqual(function_result1.surname, similar_to_reader1.surname)

        similar_to_reader2 = Reader("Wacia", "Macia", "2")
        function_result2 = library.findMyReader(2)
        self.assertTrue(function_result2)
        self.assertEqual(function_result2.name, similar_to_reader2.name)
        self.assertEqual(function_result2.surname, similar_to_reader2.surname)

        self.assertFalse(library.findMyReader(3))
        self.assertFalse(library.findMyReader(0))

    def test_parse_input_line(self):
        library = Library('database.txt')
        library.parseFileLine()

        # borrow book with id: 1 as person with pesel: 1
        library.parseInputLine("1 + 1")
        borrowed_book1 = library.findMyBook(1)
        self.assertEqual(borrowed_book1.pesel, '1')

        library.parseInputLine("1 - 1")
        borrowed_book1 = library.findMyBook(1)
        self.assertEqual(borrowed_book1.pesel, None)


if __name__ == '__main__':
    unittest.main()