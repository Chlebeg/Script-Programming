from Book_class import Book
from datetime import datetime

class Reader:
    def __init__(self, name: str, surname: str, pesel: int):
        self.name = name
        self.surname = surname
        self.pesel = pesel

    def __str__(self):
        return f'{self.name} {self.surname}'

    def __repr__(self):
        return f'{self.name} {self.surname} - pesel:{self.pesel}'

    def __add__(self, other: Book):
        if other.date_of_borrow is None:
            other.pesel = self.pesel
            other.date_of_borrow = f'{datetime.now()}'
        else:
            print("This book is already borrowed, try again later")

    def __sub__(self, other: Book):
        if self.pesel == other.pesel:
            other.pesel = None
            other.date_of_return = f'{datetime.now()}'
            other.date_of_borrow = None
        else:
            print("This account is currently not borrowing this book")
