from abstractClass.Visitor_interface import Visitor
from functionalClass.BookForBorrow_class import BookForBorrow
from datetime import datetime

class Borrower(Visitor):

    def __add__(self, book):
        if isinstance(book, BookForBorrow):
            if book.date_of_borrow is None:
                book.pesel = self.pesel
                book.date_of_borrow = f'{datetime.now()}'
                self.history.append(f"borrowed {book.title} {book.author} on {book.date_of_borrow}")
            else:
                print("This book is already borrowed, try again later")
        else:
            print("This book is not for borrow, try different one")

    def __sub__(self, book):
        if isinstance(book, BookForBorrow):
            if self.pesel == book.pesel:
                book.pesel = None
                book.date_of_return = f'{datetime.now()}'
                book.date_of_borrow = None
                self.history.append(f"returned {book.title} {book.author} on {book.date_of_return}")
            else:
                print("This account is currently not borrowing this book")
        else:
            print("This book is not for borrow, try different one")