class Book:
    id_counter = 1

    def __init__(self, author: str, title: str):
        self.id = Book.id_counter
        Book.id_counter += 1
        self.pesel = None
        self.author = author
        self.title = title
        self.date_of_borrow = None
        self.date_of_return = None

    def __str__(self):
        return f'id:{self.id} - {self.author} - "{self.title}"'

    def __repr__(self):
        if self.date_of_borrow is not None:
            return f'id:{self.id} {self.author} "{self.title}" borrower: {self.pesel}, {self.date_of_borrow}'
        elif self.date_of_return is not None:
            return f'id:{self.id} {self.author} "{self.title}" returned: {self.date_of_return}'
        else:
            return f'id:{self.id} {self.author} "{self.title}", not borrowed'
