import unittest
from Library_class import Library

class Test_Library(unittest.TestCase):

    def test_parseFileLine(self):
        library = Library('zbior.txt')
        library.parseFileLine()
        self.assertEqual(library.myBooks, {'Book1': 3, 'Book2': 2})
        self.assertEqual(library.borrowedBooks, {})

    def test_borrow_one(self):
        library = Library('zbior.txt')
        library.parseFileLine()
        library.borrow(['ja', 'Book1', '1'])
        self.assertEqual(library.myBooks, {'Book1': 2, 'Book2': 2})
        self.assertEqual(library.borrowedBooks, {'ja': {'Book1': 1}})

    def test_borrow_two(self):
        library = Library('zbior.txt')
        library.parseFileLine()
        library.borrow(['ja', 'Book1', '1'])
        library.borrow(['ja', 'Book2', '1'])
        self.assertEqual(library.myBooks, {'Book1': 2, 'Book2': 1})
        self.assertEqual(library.borrowedBooks, {'ja': {'Book1': 1, 'Book2': 1}})

    def test_borrow_by_two_accounts(self):
        library = Library('zbior.txt')
        library.parseFileLine()
        library.borrow(['ja', 'Book1', '1'])
        library.borrow(['ty', 'Book1', '1'])
        self.assertEqual(library.myBooks, {'Book1': 1, 'Book2': 2})
        self.assertEqual(library.borrowedBooks, {'ja': {'Book1': 1}, 'ty': {'Book1': 1}})

    def test_borrow_too_much(self):
        library = Library('zbior.txt')
        library.parseFileLine()
        self.assertFalse(library.borrow(['ja', 'Book1', '4']))

    def test_give_one(self):
        library = Library('zbior.txt')
        library.parseFileLine()
        library.give_back(['ja', 'Book1', '1'])
        self.assertEqual(library.myBooks, {'Book1': 4, 'Book2': 2})
        self.assertEqual(library.borrowedBooks, {'ja': {'Book1': -1}})

    def test_give_two(self):
        library = Library('zbior.txt')
        library.parseFileLine()
        library.give_back(['ja', 'Book1', '1'])
        library.give_back(['ja', 'Book2', '1'])
        self.assertEqual(library.myBooks, {'Book1': 4, 'Book2': 3})
        self.assertEqual(library.borrowedBooks, {'ja': {'Book1': -1, 'Book2': -1}})

    def test_give_sth_new(self):
        library = Library('zbior.txt')
        library.parseFileLine()
        library.give_back(['ja', 'Book3', '1'])
        self.assertEqual(library.myBooks, {'Book1': 3, 'Book2': 2, 'Book3': 1})
        self.assertEqual(library.borrowedBooks, {'ja': {'Book3': -1}})

    def test_borrow_and_give(self):
        library = Library('zbior.txt')
        library.parseFileLine()
        library.borrow(['ja', 'Book1', '1'])
        library.borrow(['ja', 'Book1', '-1'])
        self.assertEqual(library.myBooks, {'Book1': 3, 'Book2': 2})
        self.assertEqual(library.borrowedBooks, {'ja': {'Book1': 0}})

if __name__ == '__main__':
    unittest.main()