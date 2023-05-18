from abstractClass.Book_abstract import Book

class BookForBorrow(Book):
    def __init__(self, author: str, title: str):
        super().__init__(author, title)
        self.pesel = None
        self.date_of_borrow = None
        self.date_of_return = None

    def __repr__(self):
        if self.date_of_borrow is not None:
            return f'id:{self.id} {self.author} "{self.title}" borrowed: {self.pesel}, {self.date_of_borrow}'
        elif self.date_of_return is not None:
            return f'id:{self.id} {self.author} "{self.title}" returned: {self.date_of_return}'
        else:
            return f'id:{self.id} {self.author} "{self.title}", not borrowed'