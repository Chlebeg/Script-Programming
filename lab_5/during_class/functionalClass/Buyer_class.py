from abstractClass.Visitor_interface import Visitor
from functionalClass.BookForBuy_class import BookForBuy

class Buyer(Visitor):
    def __add__(self, book):
        if isinstance(book, BookForBuy):
            how_much = input("How much do you want to buy? ")
            if how_much == 0:
                return
            if not how_much:
                return
            how_much = int(how_much)
            if book.amount >= how_much:
                book.amount -= how_much
                book.sold += how_much
                self.history.append(f"bought {book.title} {book.author} amount:{how_much}, costed: {book.price * how_much}")
        else:
            print("This book is not for sell, try different one")
